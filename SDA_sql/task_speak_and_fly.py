from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Sequence, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# association table for relation many to many
student_course = Table('student_course', Base.metadata,
                       Column('student_id', ForeignKey('students.student_id'), primary_key=True),
                       Column('course_id', ForeignKey('courses.course_id'), primary_key=True))


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, Sequence('student_id_seq'), primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    PESEL = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String(150), nullable=False)

    course = relationship('Course', secondary=student_course, back_populates='students')

    def __repr__(self):
        return f"Student({self.first_name} {self.last_name}, pesel: {self.PESEL}, " \
               f"phone: {self.phone}, address: {self.address})\n"


class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, Sequence('course_id_seq'), primary_key=True)
    lessons_hours = Column(Integer, nullable=False)
    description = Column(String(50))
    start_date = Column(String(50))
    end_date = Column(String(50))
    price = Column(Integer)

    language_id = Column(Integer, ForeignKey('languages.language_id', ondelete="CASCADE"))
    level_id = Column(Integer, ForeignKey('levels.level_id', ondelete="CASCADE"))
    category_id = Column(Integer, ForeignKey('categories.category_id', ondelete="CASCADE"))

    languages = relationship('Language', back_populates='course')
    levels = relationship('Level', back_populates='course')
    categories = relationship('Category', back_populates='course')
    students = relationship('Student', secondary=student_course, back_populates='course')

    def __repr__(self):
        return f"Course(lessons_hours: {self.lessons_hours}, description:{self.description}, " \
               f"start_date: {self.start_date}, end_date: {self.end_date}, price: {self.price})," \
               f"lang_id: {self.language_id}, level_id: {self.level_id}, cat_id: {self.categories}\n"


class Level(Base):
    __tablename__ = 'levels'

    level_id = Column(Integer, Sequence('level_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))

    course = relationship('Course', back_populates='levels')

    def __repr__(self):
        return f"Level({self.name})\n"


class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, Sequence('category_id_seq'), primary_key=True)
    name = Column(String(100), nullable=False)

    course = relationship('Course', back_populates='categories')

    def __repr__(self):
        return f"Category({self.name})\n"


class Language(Base):
    __tablename__ = 'languages'

    language_id = Column(Integer, Sequence('language_id_seq'), primary_key=True)
    name = Column(String(100))

    course = relationship('Course', back_populates='languages')

    def __repr__(self):
        return f"Languages({self.name})\n"


students_data = (
    {"first_name": "Marek", "last_name": "Zegarek", "PESEL": 90041912345, "phone": 501123456, "address": "Krakow"},
    {"first_name": "Jacek", "last_name": "Placek", "PESEL": 91041912345, "phone": 502123456, "address": "Katowice"},
    {"first_name": "Jan", "last_name": "Nowak", "PESEL": 92041912345, "phone": 503123456, "address": "Warszawa"},
    {"first_name": "Jan", "last_name": "Kowalski", "PESEL": 93041912345, "phone": 504123456, "address": "Wrocław"},
    {"first_name": "Jadzia", "last_name": "Nowak", "PESEL": 94041912345, "phone": 505123456, "address": "Poznań"},
)

languages_data = (
    {"name": "English"},
    {"name": "Spanish"},
    {"name": "Greek"},
    {"name": "Italian"},
    {"name": "French"}
)

levels_data = (
    {"name": "A1"},
    {"name": "A2"},
    {"name": "B1"},
    {"name": "B2"},
    {"name": "C1"},
    {"name": "C2"}
)

categories_data = (
    {"name": "Regular"},
    {"name": "Evening"},
    {"name": "Weekend"},
    {"name": "Remote"}
)

courses_data = (
    {
        "lessons_hours": 280,
        "description": "best course",
        "start_date": "20-09-2020",
        "end_date": "20-06-2021",
        "price": 10000,
        "language_id": 1,
        "level_id": 2,
        "category_id": 3,
    },
    {
        "lessons_hours": 250,
        "description": "good price",
        "start_date": "20-10-2020",
        "end_date": "20-07-2021",
        "price": 8000,
        "language_id": 2,
        "level_id": 4,
        "category_id": 4,
    },
    {
        "lessons_hours": 320,
        "description": "free dictionary",
        "start_date": "20-11-2020",
        "end_date": "20-08-2021",
        "price": 12000,
        "language_id": 3,
        "level_id": 5,
        "category_id": 1,
    },
    {
        "lessons_hours": 340,
        "description": "be master",
        "start_date": "20-12-2020",
        "end_date": "20-09-2021",
        "price": 14000,
        "language_id": 4,
        "level_id": 6,
        "category_id": 1,
    },
    {
        "lessons_hours": 270,
        "description": "join now",
        "start_date": "20-01-2021",
        "end_date": "20-10-2021",
        "price": 9000,
        "language_id": 5,
        "level_id": 3,
        "category_id": 2,
    },
)


def create_base():
    Base.metadata.create_all(engine)


def create_students_obj(data):
    return [Student(**student) for student in data]


def create_languages_obj(data):
    return [Language(**lang) for lang in data]


def create_levels_obj(data):
    return [Level(**level) for level in data]


def create_categories_obj(data):
    return [Category(**category) for category in data]


def create_courses_obj(data):
    return [Course(**course) for course in data]


def add_students_to_db():
    session.add_all(create_students_obj(students_data))
    session.commit()


def add_languages_to_db():
    session.add_all(create_languages_obj(languages_data))
    session.commit()


def add_levels_to_db():
    session.add_all(create_levels_obj(levels_data))
    session.commit()


def add_categories_to_db():
    session.add_all(create_categories_obj(categories_data))
    session.commit()


def add_courses_to_db():
    session.add_all(create_courses_obj(courses_data))
    session.commit()


def add_all_data():
    add_students_to_db()
    add_languages_to_db()
    add_levels_to_db()
    add_categories_to_db()
    add_courses_to_db()


def show_tables():
    return (session.query(Student).all(),
            session.query(Language).all(),
            session.query(Level).all(),
            session.query(Category).all(),
            session.query(Course).all(),)


if __name__ == "__main__":
    create_base()
    add_all_data()
    session.commit()
    print(show_tables())
