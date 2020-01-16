import factory

from . import models

def ProjectFactory(session):
    class _ProjectFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = models.Project
            sqlalchemy_session_persistence = "commit"
            sqlalchemy_session = session

        id = factory.Sequence(lambda n: "%d" % n)
        name = factory.Faker("text", max_nb_chars=100)

    return _ProjectFactory

def StudyFactory(session):
    class _StudyFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = models.Study
            sqlalchemy_session_persistence = "commit"
            sqlalchemy_session = session

        id = factory.Sequence(lambda n: "%d" % n)
        name = factory.Faker("text", max_nb_chars=80)
        description = factory.Faker("text", max_nb_chars=100)

    return _StudyFactory

def SubstudyFactory(session):
    class _SubstudyFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = models.Substudy
            sqlalchemy_session_persistence = "commit"
            sqlalchemy_session = session

        id = factory.Sequence(lambda n: "%d" % n)
        study_id = RelatedFactory(StudyFactory)
        name = factory.Faker("text", max_nb_chars=80)
        description = factory.Faker("text", max_nb_chars=100)
        cell_of_origin = factory.Faker("text", max_nb_chars=100)
        tissue_hierarchy = factory.Faker("text", max_nb_chars=100)

    return _SubstudyFactory

def SubstudyTissueFactory(session):
    class _SubstudyTissueFactory(factory.alchemy.SQLAlchemyModelFactory):
        class Meta:
            model = models.SubstudyTissue
            sqlalchemy_session_persistence = "commit"
            sqlalchemy_session = session

        substudy_id = RelatedFactory(SubstudyFactory)
        tissue = factory.Faker("text", max_nb_chars=100)

    return _SubstudyTissueFactory