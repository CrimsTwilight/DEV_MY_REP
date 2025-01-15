"""
Управление системой аренды недвижимости.

Цель занятия:
Студенты создадут систему управления арендой недвижимости с использованием SQLAlchemy ORM.
Они будут работать с моделями, связанными через сложные отношения,
реализуют запросы с агрегациями, и применят транзакции для обработки аренды.

Система должна поддерживать следующие сущности:

Пользователь (User):
Имя (name)
Электронная почта (email)
Список договоров аренды (связь с Lease)

Объект недвижимости (Property):
Адрес (address)
Тип недвижимости (residential/commercial)
Стоимость аренды (rent_price)

Договор аренды (Lease):
Дата начала (start_date)
Дата окончания (end_date)
Арендатор (User)
Объект недвижимости (Property)
Статус (активен/завершён)

Платёж (Payment):
Сумма (amount)
Дата платежа (payment_date)
Договор аренды (Lease)

Бизнес-правила:
Один пользователь может арендовать несколько объектов недвижимости,
но не более одного договора аренды на один объект в одно и то же время.
Договор аренды может быть активирован только после внесения первого платежа.
Если договор завершён, объект недвижимости снова становится доступным для аренды.
При удалении пользователя все его договоры и платежи также должны быть удалены.


ЗАДАЧА
Добавление данных:
Добавить пользователей, объекты недвижимости и договоры.

Бизнес-логика:
Реализовать функцию для внесения платежа по договору.
Реализовать логику завершения договора (статус "completed").

Сложные запросы:
Найти всех пользователей, которые не внесли ни одного платежа.
Вывести объекты недвижимости, которые были арендованы более 3 раз.

Транзакции:
Обеспечить атомарность операций при создании договора и внесении первого платежа.

Расширение:
Добавить сущность "Агент" и реализовать комиссию для агентов от суммы аренды.
"""
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Enum, Float, Date, ForeignKey, Boolean, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import IntegrityError


Base = declarative_base()


def create_db_session():
    engine = create_engine('sqlite:///rental_system.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


# Пользователь
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    leases = relationship('Lease', back_populates='user', cascade='all, delete')


# Объект недвижимости
class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    address = Column(String)
    property_type = Column(Enum('Жилая', 'Коммерческая', name='property_type'), default='Жилая')
    rent_price = Column(Float)
    leases = relationship('Lease', back_populates='property', cascade='all, delete')


# Договор аренды
class Lease(Base):
    __tablename__ = 'leases'
    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Enum('Активен', 'Завершён', name='lease_status'), default='Активен')
    user_id = Column(Integer, ForeignKey('users.id'))
    property_id = Column(Integer, ForeignKey('properties.id'))
    user = relationship('User', back_populates='leases')
    property = relationship('Property', back_populates='leases')
    payments = relationship('Payment', back_populates='lease', cascade='all, delete')


# Платёж
class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    payment_date = Column(Date)
    lease_id = Column(Integer, ForeignKey('leases.id'))
    lease = relationship('Lease', back_populates='payments')


# Добавить пользователя
def add_user(session, name, email):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()


# Добавить объект недвижимости
def add_property(session, address, property_type, rent_price):
    property = Property(address=address, property_type=property_type, rent_price=rent_price)
    session.add(property)
    session.commit()


# Создать договор аренды
def create_lease(session, user_id, property_id, start_date):
    existing_lease = session.query(Lease).filter(Lease.property_id == property_id,
                                                 Lease.status == 'Активен').first()
    if existing_lease:
        raise ValueError("Недвижимость уже сдана в аренду.")
    lease = Lease(user_id=user_id, property_id=property_id, start_date=start_date)
    session.add(lease)
    session.commit()
    return lease


# Произвести оплату
def make_payment(session, lease_id, amount):
    lease = session.query(Lease).filter(Lease.id == lease_id).first()
    if not lease:
        raise ValueError("Договор аренды не найден.")
    if Lease.status == 'Завершён':
        raise ValueError("Невозможно внести оплату за завершённую аренду.")
    payment = Payment(lease_id=lease_id, amount=amount)
    session.add(payment)
    lease.status = 'Активен'
    session.commit()


# Подписать договор аренды
def complete_lease(session, lease_id, end_date):
    lease = session.query(Lease).filter(Lease.id == lease_id).first()
    if not lease:
        raise ValueError("Договор аренды не найден.")
    lease.status = 'Завершён'
    lease.end_date = end_date
    session.commit()


# Получить пользователей без платежей
def get_users_without_payments(session):
    return (
        session.query(User)
        .join(Lease, isouter=True)
        .join(Payment, isouter=True)
        .filter(Payment.id == None)
        .all()
    )


# Получить объекты недвижимости, арендованные более n раз
def get_properties_leased_more_than(session, times):
    return (
        session.query(Property)
        .join(Lease)
        .group_by(Property.id)
        .having(func.count(Lease.id) > times)
        .all()
    )


if __name__ == "__main__":
    session = create_db_session()

    try:
        add_user(session, 'Pavel', 'pavel@gmail.com')
        add_user(session, 'Anton', 'anton@mail.ru')

        add_property(session, 'Лесная 16/1', 'Жилая', 350)
        add_property(session, 'Комсомольская 45', 'Коммерческая', 500)

        lease = create_lease(session, 1, 1,
                             datetime.strptime('2024.01.01', '%Y.%m.%d').date())
        make_payment(session, lease_id=lease.id, amount=350)
        complete_lease(session, lease_id=lease.id,
                       end_date=datetime.strptime('2024.02.02', '%Y.%m.%d').date())

        users_without_payment = get_users_without_payments(session)
        print("Пользователи без платежей:", [user.name for user in users_without_payment])

        popular_properties = get_properties_leased_more_than(session, 0)
        print("Популярные объекты недвижимости:", [prop.address for prop in popular_properties])

    except IntegrityError as e:
        session.rollback()
        print("Ошибка:", e)

    except Exception as e:
        session.rollback()
        print("Ошибка:", e)

    finally:
        session.close()
