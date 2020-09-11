from django.db import models
import datetime


class Region(models.Model):
    name = models.CharField(max_length=200)


class University(models.Model):
    address = models.CharField(max_length=255)
    affilation_name = models.CharField(max_length=255)
    author_count = models.IntegerField(default=0)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    date_created = models.DateField()
    document_count = models.IntegerField(default=0)
    eid = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)
    org_domain = models.CharField(max_length=200)
    org_type = models.CharField(max_length=200)
    org_url = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    scopus_affiliation_link = models.CharField(max_length=200)
    search_link = models.CharField(max_length=200)
    self_link = models.CharField(max_length=200)
    state = models.ForeignKey(Region, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)


class Author(models.Model):
    affilation_current = models.ForeignKey(University, on_delete=models.CASCADE)
    citation_count = models.IntegerField(default=0)
    cited_by_count = models.IntegerField(default=0)
    coauthor_count = models.IntegerField(default=0)
    coauthor_link = models.CharField(max_length=255)
    date_created = models.DateField()
    document_count = models.IntegerField(default=0)
    eid = models.CharField(max_length=200)
    given_name = models.CharField(max_length=200)
    h_index = models.CharField(max_length=100)
    identifier = models.CharField(max_length=100)
    indexed_name = models.CharField(max_length=100)
    initials = models.CharField(max_length=100)
    orc_id = models.CharField(max_length=100)
    publication_range = models.CharField(max_length=100)
    scopus_author_link = models.CharField(max_length=255)
    search_link = models.CharField(max_length=255)
    self_link = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255, default='')
    russian_fullname = models.CharField(max_length=255, default='')
    job_category = models.CharField(max_length=255, default='')
    job_position = models.CharField(max_length=255, default='')
    job_unit = models.CharField(max_length=255, default='')
    job_parent_unit = models.CharField(max_length=255, default='')
    job_rate = models.CharField(max_length=255, default='0.0')
    type_employment = models.CharField(max_length=255, default='')
    date_birth = models.DateField(default=datetime.date(1900, 1, 1))
    last_degree = models.CharField(max_length=255, default='')
    phd = models.BooleanField(default=False)
    last_academic_title = models.CharField(max_length=255, default='')
    relevant = models.BooleanField(default=False)


class Journal(models.Model):
    sourcetitle = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=200)
    type_journal = models.CharField(max_length=100)
    issn = models.CharField(max_length=100)
    source_id = models.IntegerField(null=True)
    cnt_publications = models.IntegerField(default=0)


class Document(models.Model):
    eid = models.CharField(max_length=200)
    doi = models.CharField(max_length=200)
    pii = models.CharField(max_length=200, default="-1")
    pubmed_id = models.CharField(max_length=200)
    title = models.CharField(max_length=255)
    subtype = models.CharField(max_length=200)
    # subtype_description = models.CharField(max_length=200)
    creator = models.ForeignKey(Author, on_delete=models.CASCADE)
    author_count = models.IntegerField(default=0)
    cover_date = models.DateField()
    cover_display_date = models.CharField(max_length=200)
    publication_name = models.CharField(max_length=255)
    issn = models.ForeignKey(Journal, on_delete=models.CASCADE)
    source_id = models.CharField(max_length=200)
    eIssn = models.CharField(max_length=200)
    aggregation_type = models.CharField(max_length=200)
    volume = models.CharField(max_length=100, default="0")
    issue_identifier = models.CharField(max_length=200)
    article_number = models.CharField(max_length=200)
    page_range = models.CharField(max_length=200, default="-1")
    description = models.TextField()
    authkeywords = models.TextField()
    citedby_count = models.IntegerField(default=0)
    openaccess = models.IntegerField(default=0)
    fund_acr = models.CharField(max_length=200)
    fund_no = models.CharField(max_length=200)
    fund_sponsor = models.CharField(max_length=200)
    citation_by_year = models.TextField(default="")
    citation_by_year_with_self = models.TextField(default="")


class Subject(models.Model):
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=255)


class DocumentSubject(models.Model):
    id_doc = models.ForeignKey(Document, on_delete=models.CASCADE, default=0)
    id_sub = models.ForeignKey(Subject, on_delete=models.CASCADE, default=0)


class AuthorJournal(models.Model):
    id_auth = models.ForeignKey(Author, on_delete=models.CASCADE, default=0)
    id_journal = models.ForeignKey(Journal, on_delete=models.CASCADE, default=0)


class AuthorUniversity(models.Model):
    id_auth = models.ForeignKey(Author, on_delete=models.CASCADE, default=0)
    id_university = models.ForeignKey(University, on_delete=models.CASCADE, default=0)


class DocumentAuthorUniversity(models.Model):
    id_doc = models.ForeignKey(Document, on_delete=models.CASCADE, default=0, null=True)
    id_auth = models.ForeignKey(Author, on_delete=models.CASCADE, default=0, null=True)
    id_university = models.ForeignKey(University, on_delete=models.CASCADE, default=0, null=True)


class AuthorSubject(models.Model):
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    id_sub = models.ForeignKey(Subject, on_delete=models.CASCADE)


class DocumentUniversityAffiliations(models.Model):
    id_doc = models.ForeignKey(Document, on_delete=models.CASCADE, default=0, null=True)
    id_university = models.ForeignKey(University, on_delete=models.CASCADE, default=0, null=True)


class Rankings(models.Model):
    name = models.CharField(max_length=255)


class UniversityRankPlace(models.Model):
    id_university = models.ForeignKey(University, on_delete=models.CASCADE, default=0)
    id_ranking = models.ForeignKey(Rankings, on_delete=models.CASCADE, default=0)
    year = models.IntegerField(default=0)
    place = models.CharField(max_length=255, default="")


class UniversityRankCriteria(models.Model):
    id_university = models.ForeignKey(University, on_delete=models.CASCADE, default=0)
    id_ranking = models.ForeignKey(Rankings, on_delete=models.CASCADE, default=0)
    criteria = models.CharField(max_length=255, default="")
    score = models.FloatField(default=0.0)


class DateCitationCount(models.Model):
    date = models.DateField(auto_now=True)
    citation_count = models.IntegerField(default=0)
    self_citation_count = models.IntegerField(default=0)
