"""Maakt de ATS-vriendelijke Word-templates voor The Gap-Proof Résumé Kit.
Gebruik: python3 make_docx.py <uitvoermap>
Eén kolom, geen tabellen/tekstvakken/afbeeldingen, contactgegevens in de hoofdtekst."""
import sys
from pathlib import Path
from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x14, 0x21, 0x3D)
GREY = RGBColor(0x55, 0x5D, 0x6E)
out = Path(sys.argv[1] if len(sys.argv) > 1 else '.')
out.mkdir(parents=True, exist_ok=True)


def new_doc():
    d = Document()
    for s in d.sections:
        s.top_margin = s.bottom_margin = Cm(1.8)
        s.left_margin = s.right_margin = Cm(2.0)
    st = d.styles['Normal']
    st.font.name = 'Calibri'
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
    st.font.size = Pt(10.5)
    st.paragraph_format.space_after = Pt(2)
    st.paragraph_format.line_spacing = 1.1
    return d


def bottom_border(p):
    pPr = p._p.get_or_add_pPr()
    b = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    for k, v in (('w:val', 'single'), ('w:sz', '6'), ('w:space', '1'), ('w:color', '14213D')):
        bottom.set(qn(k), v)
    b.append(bottom)
    pPr.append(b)


def name_block(d, name, title, contact):
    p = d.add_paragraph()
    r = p.add_run(name); r.bold = True; r.font.size = Pt(20); r.font.color.rgb = NAVY
    p.paragraph_format.space_after = Pt(0)
    p = d.add_paragraph(); r = p.add_run(title); r.font.size = Pt(11.5); r.font.color.rgb = GREY
    p.paragraph_format.space_after = Pt(0)
    p = d.add_paragraph(contact); p.paragraph_format.space_after = Pt(6)


def heading(d, text):
    p = d.add_paragraph()
    r = p.add_run(text.upper()); r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NAVY
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(4)
    bottom_border(p)


def role(d, title, org, dates, bullets):
    p = d.add_paragraph()
    r = p.add_run(title); r.bold = True
    p.add_run(f', {org}' if org else '')
    p.add_run(f'  |  {dates}').font.color.rgb = GREY
    p.paragraph_format.space_before = Pt(4)
    for b in bullets:
        d.add_paragraph(b, style='List Bullet')


def para(d, text):
    d.add_paragraph(text)


CONTACT = '[City, Country]  |  [phone]  |  [email]  |  linkedin.com/in/[yourname]'
GAP_BULLETS = ['[Course or certificate you completed, year]',
               '[Freelance, volunteer or project work and one result]']
JOB_BULLETS = ['[Action verb] + [what you did] + [result with a number]',
               '[Action verb] + [what you did] + [result with a number]',
               '[Action verb] + [what you did] + [result with a number]']


def resume_classic():
    d = new_doc()
    name_block(d, '[Your Name]', '[Target Job Title]', CONTACT)
    heading(d, 'Summary')
    para(d, '[Role] with [number] years of experience in [field]. Strongest in [skill] and [skill], '
            'with a track record of [type of result]. Looking for a [target role] position at a [type of company].')
    heading(d, 'Experience')
    role(d, '[Gap line from the Gap Explanation Bank]', '', '[Mon Year] – Present', GAP_BULLETS)
    role(d, '[Job Title]', '[Company]', '[Mon Year] – [Mon Year]', JOB_BULLETS)
    role(d, '[Job Title]', '[Company]', '[Mon Year] – [Mon Year]', JOB_BULLETS[:2])
    heading(d, 'Education')
    para(d, '[Degree or qualification], [School]  |  [Year]')
    heading(d, 'Skills')
    para(d, '[Skill], [skill], [skill], [tool], [tool], [language]')
    d.save(out / 'Resume-1-Classic.docx')


def resume_experienced():
    d = new_doc()
    name_block(d, '[Your Name]', '[Target Job Title]', CONTACT)
    heading(d, 'Summary')
    para(d, '[Senior role] with [number]+ years in [field], leading [teams / budgets / programmes]. '
            'Known for [strength] and [strength]. Recent results include [headline result].')
    heading(d, 'Key Achievements')
    for _ in range(3):
        d.add_paragraph('[Biggest result of your career, with a number]', style='List Bullet')
    heading(d, 'Experience')
    role(d, '[Gap line from the Gap Explanation Bank]', '', '[Mon Year] – Present', GAP_BULLETS)
    role(d, '[Job Title]', '[Company]', '[Mon Year] – [Mon Year]', JOB_BULLETS + ['[Action verb] + [what you did] + [result]'])
    role(d, '[Job Title]', '[Company]', '[Mon Year] – [Mon Year]', JOB_BULLETS)
    role(d, '[Job Title]', '[Company]', '[Year] – [Year]', JOB_BULLETS[:2])
    heading(d, 'Earlier Experience')
    para(d, '[Job Title], [Company]  |  [Year] – [Year]')
    para(d, '[Job Title], [Company]  |  [Year] – [Year]')
    heading(d, 'Education & Certifications')
    para(d, '[Degree], [School]  |  [Year]')
    para(d, '[Certification], [Provider]  |  [Year]')
    heading(d, 'Skills')
    para(d, '[Skill], [skill], [skill], [tool], [tool], [tool], [language]')
    d.save(out / 'Resume-2-Experienced.docx')


def resume_career_change():
    d = new_doc()
    name_block(d, '[Your Name]', '[New Target Job Title]', CONTACT)
    heading(d, 'Summary')
    para(d, '[Old role] moving into [new field], bringing [number] years of [transferable skill]. '
            'Recently completed [course / project] in [new field]. Strongest in [skill] and [skill].')
    heading(d, 'Relevant Skills')
    for s in ('[Skill the new job asks for]: [where you used it and the result]',
              '[Skill the new job asks for]: [where you used it and the result]',
              '[Skill the new job asks for]: [where you used it and the result]'):
        d.add_paragraph(s, style='List Bullet')
    heading(d, 'Projects & Training')
    role(d, '[Course / certificate]', '[Provider]', '[Year]', ['[Project you did and what it shows]'])
    role(d, '[Project or freelance work in the new field]', '', '[Mon Year] – Present', ['[What you did and one result]'])
    heading(d, 'Experience')
    role(d, '[Gap line from the Gap Explanation Bank]', '', '[Mon Year] – Present', GAP_BULLETS[:1])
    role(d, '[Job Title]', '[Company]', '[Mon Year] – [Mon Year]',
         ['[Result that uses a transferable skill]', '[Result that uses a transferable skill]'])
    role(d, '[Job Title]', '[Company]', '[Mon Year] – [Mon Year]', ['[Result that uses a transferable skill]'])
    heading(d, 'Education')
    para(d, '[Degree or qualification], [School]  |  [Year]')
    d.save(out / 'Resume-3-Career-Change.docx')


def letter(filename, paragraphs):
    d = new_doc()
    p = d.add_paragraph(); r = p.add_run('[Your Name]'); r.bold = True; r.font.size = Pt(16); r.font.color.rgb = NAVY
    para(d, CONTACT)
    para(d, '')
    para(d, '[Date]')
    para(d, '[Hiring manager name, if known]\n[Company]')
    para(d, '')
    para(d, 'Dear [Name / Hiring Manager],')
    for t in paragraphs:
        p = d.add_paragraph(t); p.paragraph_format.space_after = Pt(8)
    para(d, 'Kind regards,')
    para(d, '[Your Name]')
    d.save(out / filename)


def letters():
    letter('Cover-Letter-A-Recent-Layoff.docx', [
        "I'm applying for the [job title] role at [company]. [One specific reason you want this job: something from the job ad, their product or recent news.]",
        "In my [number] years as a [role] at [previous company], I [result that matches the job ad]. I also [second result], which is directly relevant to [requirement from the job ad].",
        "After my role was eliminated in [previous company]'s restructuring in [month], I've been looking specifically for a position where I can [what you do best], which is what drew me to this one.",
        "I'd welcome the chance to talk about how I could help [company] with [their goal or challenge]. Thank you for your time and consideration.",
    ])
    letter('Cover-Letter-B-Longer-Gap.docx', [
        "I'm writing to apply for the [job title] position at [company]. [One specific reason this company or role appeals to you.]",
        "Over [number] years in [field], I [strongest result]. At [previous company], I [second result that matches the job ad].",
        "Since my role at [previous company] ended in [month year], I've used the time to [course / certificate] and [freelance / volunteer / project work], which has kept my [skill] current and added [new skill].",
        "I'm ready to commit fully to a team again, and I'd be glad to discuss how my experience fits what you're looking for. Thank you for considering my application.",
    ])
    letter('Cover-Letter-C-Career-Pivot.docx', [
        "I'm excited to apply for the [job title] role at [company]. After [number] years in [old field], I'm moving into [new field], and [company] is exactly where I'd like to make that move because [specific reason].",
        "In my previous work I [result using a transferable skill]. That experience with [transferable skill] maps directly onto [requirement in the job ad].",
        "To prepare for this move, I completed [course] and [project / freelance work], where I [what you did and the result].",
        "I'd love to show you how a background in [old field] can be an advantage in this role. Thank you for your time.",
    ])


def example():
    d = new_doc()
    name_block(d, 'Dana Reyes', 'Marketing Coordinator',
               'Austin, TX  |  (555) 010-0199  |  dana.reyes@example.com  |  linkedin.com/in/danareyes-example')
    heading(d, 'Summary')
    para(d, 'Marketing coordinator with 6 years in B2B software. Strongest in email and social campaigns that bring in '
            'qualified leads. Looking for a marketing role at a growing SaaS company.')
    heading(d, 'Experience')
    role(d, 'Career transition: job search and upskilling', '', 'Feb 2026 – Present',
         ['Completed HubSpot Email Marketing Certification (2026)',
          'Freelance email campaigns for 2 local businesses; one newsletter reached a 41% open rate'])
    role(d, 'Marketing Coordinator', 'BrightPath Software', 'Mar 2019 – Feb 2026',
         ['Grew LinkedIn followers from 2,000 to 9,500 in 18 months with a weekly content plan',
          'Ran monthly email campaigns that generated around 120 qualified leads per quarter',
          'Coordinated 6 trade-show events with the sales team, each delivered on budget'])
    role(d, 'Marketing Assistant', 'Lumen Creative Agency', 'Jun 2017 – Feb 2019',
         ['Wrote and scheduled social posts for 8 client accounts',
          'Built a shared content calendar that the whole agency adopted'])
    heading(d, 'Education')
    para(d, 'B.A. Communications, University of Texas at Austin  |  2017')
    heading(d, 'Skills')
    para(d, 'Email marketing, social media strategy, HubSpot, Mailchimp, Canva, Google Analytics, copywriting, event coordination')
    d.save(out / 'Example-Resume-Filled.docx')


resume_classic(); resume_experienced(); resume_career_change(); letters(); example()
print('DOCX files written to', out)
