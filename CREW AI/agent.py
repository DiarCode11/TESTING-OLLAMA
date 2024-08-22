import os
from crewai import Agent, Task, Crew
from langchain_community.chat_models import ChatOllama

# LLM from Ollama
local_model = "gemma2"
llm = ChatOllama(model=local_model)

def write_blog(topic, llm):
  # Create Researcher agent
  researcher = Agent(
      role='Analis Riset Senior',
      goal=f"Menemukan penelitian tentang {topic}",
      backstory="""Anda bekerja di perusahaan riset terkemuka.
      Keahlian Anda terletak pada mengidentifikasi tren yang sedang berkembang, melakukan riset, dan menemukan informasi baru.
      Anda ahli dalam menganalisis data yang kompleks dan menyajikan wawasan yang dapat ditindaklanjuti.""",
      verbose=True,
      allow_delegation=False,
      llm=llm
  )

  # Create Writer agent
  writer = Agent(
      role='Kreator Konten',
      goal=f"Membuat konten yang menarik tentang {topic}",
      backstory="""Anda adalah seorang Kreator Konten terkenal, dikenal dengan artikel-artikel Anda yang informatif dan menarik.
      Anda mengubah konsep yang kompleks menjadi narasi yang menarik.""",
      verbose=True,
      allow_delegation=False,
      llm=llm
  )

  # Create tasks for your agents
  task1 = Task(
    description=f"Lakukan analisis komprehensif tentang {topic}",
    expected_output="Laporan analisis dalam bentuk bullet poin",
    agent=researcher
  )

  task2 = Task(
    description=f"""Dengan menggunakan wawasan yang diberikan, buatlah blog post yang menarik
    yang menyoroti topik {topic}.
    Tulisan Anda harus informatif namun mudah dipahami, cocok untuk semua audiens, mudah dimengerti.
    Buat terdengar keren, hindari kata-kata kompleks agar tidak terdengar seperti AI..""",
    expected_output="Blog post lengkap setidaknya 4 paragraf menggunakan bahasa indonesia",
    agent=writer
  )

  # Instantiate your crew with a sequential process
  crew = Crew(
      agents=[researcher, writer],
      tasks=[task1, task2],
      verbose=True, 
  )

  # Get your crew to work!
  result = crew.kickoff()
  return result

response = write_blog('apa itu cincin api megatrust', llm)
print(response)