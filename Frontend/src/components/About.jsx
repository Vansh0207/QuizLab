import { useNavigate } from "react-router-dom";

export default function About() {
    const navigate = useNavigate();

    return (
        <div className="bg-black min-h-screen flex flex-col items-center py-12 px-4">
            {/* Hero Section */}
            <section className="text-center mb-12">
                <h1 className="text-4xl font-bold text-pink-600">About QuizLab</h1>
                <p className="mt-4 text-lg text-white max-w-2xl">
                    Transform your learning experience with AI-powered transcription, summarization, and quizzes! 
                    Earn points and redeem them on various platforms.
                </p>
            </section>

            {/* Card Container */}
            <div className="grid md:grid-cols-3 gap-8 max-w-6xl w-full">
                {/* AI-Powered Learning Card */}
                <div className="bg-black rounded-lg shadow-lg overflow-hidden transition-transform transform hover:scale-105 hover:shadow-xl">
                    <img src="/about1.jpeg" alt="AI Technology" className="w-full h-60 object-cover" />
                    <div className="p-6">
                        <h2 className="text-2xl font-semibold text-pink-500">AI-Powered Learning</h2>
                        <p className="mt-3 text-white">
                            Our advanced AI extracts audio from videos, transcribes them, and summarizes key points. 
                            This helps learners quickly grasp essential concepts.
                        </p>
                    </div>
                </div>

                {/* Brain & Tech Card */}
                <div className="bg-black rounded-lg shadow-lg overflow-hidden transition-transform transform hover:scale-105 hover:shadow-xl">
                    <img src="/about2.jpeg" alt="Brain & Technology" className="w-full h-60 object-cover" />
                    <div className="p-6">
                        <h2 className="text-2xl font-semibold text-pink-500">Enhance Knowledge Retention</h2>
                        <p className="mt-3 text-white">
                            By utilizing AI-driven summaries, your brain processes information efficiently. 
                            Structured insights ensure better memory recall.
                        </p>
                    </div>
                </div>

                {/* Quiz Engagement Card */}
                <div className="bg-black rounded-lg shadow-lg overflow-hidden transition-transform transform hover:scale-105 hover:shadow-xl">
                    <img src="/about3.jpeg" alt="Quiz Engagement" className="w-full h-60 object-cover" />
                    <div className="p-6">
                        <h2 className="text-2xl font-semibold text-pink-500">Engaging Quizzes</h2>
                        <p className="mt-3 text-white">
                            Our AI-generated quizzes make learning interactive! 
                            Answer questions, test your understanding, and earn redeemable points.
                        </p>
                    </div>
                </div>
            </div>

            {/* Call to Action */}
            <section className="text-center mt-12">
                <h2 className="text-3xl font-bold text-white">Ready to Elevate Your Learning?</h2>
                <p className="mt-3 text-lg text-white">Start transcribing, summarizing, and earning rewards today!</p>
                <button
                    onClick={() => navigate("/")}
                    className="mt-5 bg-pink-600 text-white px-6 py-3 rounded-full font-semibold shadow-md hover:bg-pink-700 transition-all cursor-pointer"
                >
                    Get Started
                </button>
            </section>
        </div>
    );
}