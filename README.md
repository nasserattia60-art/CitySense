🔥 Inspiration

The inspiration came from a problem we all face: people move to new cities for study, work, or travel… and then discover unexpected surprises like noise, insects, poor water quality, or unsafe neighborhoods. There’s no platform that gives a real, honest, holistic picture of life quality in any neighborhood — you might know the weather, but not the pollution. You might see beautiful photos, but not crime waves. You might love a place online, then regret living there.

So we built CitySense to solve that.

CitySense analyzes any city or neighborhood and generates a detailed AI-powered urban quality report, showing everything that actually matters before choosing where to live.

🚀 What CitySense provides

CitySense doesn’t stop at basic city data — it reveals what people really need to know:

Noise level variations day vs night

Air & water quality indicators

Mosquito and insect density patterns

Traffic congestion + roadwork alerts

Neighborhood safety & crime probability

Average rent prices & cost of living

Weather behavior + seasonal patterns

Verified user reviews & local insights

A visual AI heatmap showing livability score


With one search — you know the full picture.

🛠 How we built it

We built CitySense using a scalable, AI-first architecture designed to handle data in motion:

Component	Technology

Core Framework	Django
Frontend	HTML, CSS, JavaScript
Weather & environmental data	Open-Meteo API + scraped datasets
Real-time streams	Confluent Kafka (for heatmap processing)
AI layer	LLM summarization + anomaly detection


The system collects raw data → filters it → detects anomalies → generates a clean AI summary optimized for human decisions.


⛓ Challenges we faced

Urban analytics is complex. Our main challenges were:

Collecting reliable data for cities with limited public datasets

Integrating multiple APIs smoothly under time pressure

Building a real-time heatmap using Confluent streams

Making AI summaries consistent, verifiable & bias-free

Designing a simple UI for a massive data model

Ensuring fast performance despite large geographic layers

Balancing visual design vs analytical depth


But we pushed through each one — fast.

🏆 Achievements we’re proud of

Built a fully operational MVP in a very short time

One of the first address-level city analyzers in the region

Designed a clean and intuitive UX for a complex concept

Successfully integrated AI with live streaming data

Created a visual heatmap that makes city risks instantly noticeable

Turned raw messy data → into clarity that anyone can understand


We didn’t just build a tool —
we built a decision-making engine.

📚 What we learned

Real-time analytics at city scale is harder than it looks

AI is powerful — but requires careful prompting and validation

Users value trust & credibility more than fancy UI

GIS data must be simplified for speed and usability

Good data visualization can replace 20 paragraphs of text

Insight is more valuable than raw numbers


🔮 What’s next

We’re just getting started.
Next step is expanding CitySense into a global intelligent atlas:

Support for more cities and districts worldwide

Richer layers: weather, safety, pollution, water health, services

AI-powered housing recommendations

Predictive climate-risk modeling

Launching a dedicated mobile app

Personalized user dashboards + favorites tracking

Bilingual interface for international adoption


CitySense isn’t a website —
it’s the future of how humans choose where to live.
