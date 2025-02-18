import streamlit as st
from itertools import combinations
import random

# Define the voting functions here (first_past_the_post, approval_voting, preferential_voting, condorcet_method, borda_count)

def first_past_the_post(candidates, votes):
    try:
        vote_counts = {candidate: 0 for candidate in candidates}
        for vote in votes:
            if vote not in candidates:
                raise ValueError(f"Invalid vote: {vote} is not a valid candidate.")
            vote_counts[vote] += 1

        max_votes = max(vote_counts.values())
        winners = [candidate for candidate, votes in vote_counts.items() if votes == max_votes]

        return winners, vote_counts
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def approval_voting(candidates, votes):
    try:
        approval_counts = {candidate: 0 for candidate in candidates}
        
        for vote in votes:
            for candidate in vote:
                if candidate not in candidates:
                    raise ValueError(f"Invalid vote: {candidate} is not a valid candidate.")
                approval_counts[candidate] += 1
        
        winner = max(approval_counts, key=approval_counts.get)
        
        return winner, approval_counts
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def preferential_voting(candidates, votes):
    try:
        while True:
            vote_counts = {candidate: 0 for candidate in candidates}
            for vote in votes:
                if vote and vote[0] not in candidates:
                    raise ValueError(f"Invalid vote: {vote[0]} is not a valid candidate.")
                if vote:
                    vote_counts[vote[0]] += 1
            
            total_votes = sum(vote_counts.values())
            for candidate, count in vote_counts.items():
                if count > total_votes / 2:
                    return candidate, vote_counts
            
            min_votes = min(vote_counts.values())
            for candidate, count in vote_counts.items():
                if count == min_votes:
                    candidates.remove(candidate)
                    break
            
            for vote in votes:
                if candidate in vote:
                    vote.remove(candidate)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def condorcet_method(candidates, votes):
    try:
        pairwise_counts = {candidate: {opponent: 0 for opponent in candidates if opponent != candidate} for candidate in candidates}
        
        for vote in votes:
            for i, candidate in enumerate(vote):
                if candidate not in candidates:
                    raise ValueError(f"Invalid vote: {candidate} is not a valid candidate.")
                for opponent in vote[i+1:]:
                    pairwise_counts[candidate][opponent] += 1
        
        for candidate in candidates:
            if all(pairwise_counts[candidate][opponent] > pairwise_counts[opponent][candidate] for opponent in candidates if opponent != candidate):
                return candidate, pairwise_counts
        
        return "No Condorcet Winner", pairwise_counts
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

def borda_count(candidates, votes):
    try:
        borda_scores = {candidate: 0 for candidate in candidates}
        
        for vote in votes:
            for rank, candidate in enumerate(vote):
                if candidate not in candidates:
                    raise ValueError(f"Invalid vote: {candidate} is not a valid candidate.")
                points = len(candidates) - rank - 1
                borda_scores[candidate] += points
        
        max_score = max(borda_scores.values())
        winners = [candidate for candidate, score in borda_scores.items() if score == max_score]
        
        return winners, borda_scores
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None

# Fireworks animation using HTML/JavaScript
def fireworks_animation():
    fireworks_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fireworks</title>
        <style>
            body, html {
                margin: 0;
                padding: 0;
                overflow: hidden;
                height: 100%;
                background-color: black;
            }
            canvas {
                display: block;
            }
        </style>
    </head>
    <body>
        <canvas id="fireworks"></canvas>
        <script>
            const canvas = document.getElementById('fireworks');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const fireworks = [];
            const particles = [];

            class Firework {
                constructor() {
                    this.x = Math.random() * canvas.width;
                    this.y = canvas.height;
                    this.color = `hsl(${Math.random() * 360}, 100%, 50%)`;
                    this.vy = -Math.random() * 4 - 2;
                    this.exploded = false;
                }

                update() {
                    this.y += this.vy;
                    if (this.vy < 0 && this.y < canvas.height / 2 + Math.random() * 100) {
                        this.exploded = true;
                        this.explode();
                    }
                }

                explode() {
                    for (let i = 0; i < 100; i++) {
                        particles.push(new Particle(this.x, this.y, this.color));
                    }
                }

                draw() {
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, 3, 0, Math.PI * 2);
                    ctx.fillStyle = this.color;
                    ctx.fill();
                }
            }

            class Particle {
                constructor(x, y, color) {
                    this.x = x;
                    this.y = y;
                    this.color = color;
                    this.vx = Math.random() * 6 - 3;
                    this.vy = Math.random() * 6 - 3;
                    this.alpha = 1;
                }

                update() {
                    this.x += this.vx;
                    this.y += this.vy;
                    this.alpha -= 0.01;
                }

                draw() {
                    ctx.save();
                    ctx.globalAlpha = this.alpha;
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, 2, 0, Math.PI * 2);
                    ctx.fillStyle = this.color;
                    ctx.fill();
                    ctx.restore();
                }
            }

            function animate() {
                ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                if (Math.random() < 0.05) {
                    fireworks.push(new Firework());
                }

                fireworks.forEach((firework, index) => {
                    firework.update();
                    firework.draw();
                    if (firework.exploded) {
                        fireworks.splice(index, 1);
                    }
                });

                particles.forEach((particle, index) => {
                    particle.update();
                    particle.draw();
                    if (particle.alpha <= 0) {
                        particles.splice(index, 1);
                    }
                });

                requestAnimationFrame(animate);
            }

            animate();
        </script>
    </body>
    </html>
    """
    st.components.v1.html(fireworks_html, height=600)

# Streamlit App
def main():
    st.title("🗳 Voting Systems App 🗳")
    
    st.sidebar.header("⚙ Settings")
    voting_system = st.sidebar.selectbox(
        "Choose a voting system 🎲",
        ["First Past the Post", "Approval Voting", "Preferential Voting", "Condorcet Method", "Borda Count"]
    )
    
    st.sidebar.header("👥 Set Number of Candidates and Voters")
    num_candidates = st.sidebar.number_input("Number of Candidates 🧑‍🤝‍🧑", min_value=1, value=3, step=1)
    num_voters = st.sidebar.number_input("Number of Voters 🗳", min_value=1, value=5, step=1)
    
    st.header("📝 Input Candidates")
    candidates = []
    for i in range(num_candidates):
        candidate = st.text_input(f"Candidate {i+1} �", value=f"Candidate {i+1}")
        candidates.append(candidate)
    
    st.header("📥 Input Votes")
    votes = []
    for i in range(num_voters):
        st.subheader(f"Voter {i+1} 👤")
        if voting_system == "First Past the Post":
            vote = st.selectbox(f"Select a candidate for Voter {i+1} 🗳", candidates)
            votes.append(vote)
        elif voting_system == "Approval Voting":
            vote = st.multiselect(f"Select approved candidates for Voter {i+1} ✅", candidates)
            votes.append(vote)
        elif voting_system == "Preferential Voting":
            vote = st.multiselect(f"Rank candidates for Voter {i+1} (in order of preference) 📊", candidates)
            votes.append(vote)
        elif voting_system == "Condorcet Method":
            vote = st.multiselect(f"Rank candidates for Voter {i+1} (in order of preference) 📊", candidates)
            votes.append(vote)
        elif voting_system == "Borda Count":
            vote = st.multiselect(f"Rank candidates for Voter {i+1} (in order of preference) 📊", candidates)
            votes.append(vote)
    
    if st.button("🚀 Run Voting System"):
        if voting_system == "First Past the Post":
            winners, vote_counts = first_past_the_post(candidates, votes)
        elif voting_system == "Approval Voting":
            winners, approval_counts = approval_voting(candidates, votes)
        elif voting_system == "Preferential Voting":
            winners, vote_counts = preferential_voting(candidates, votes)
        elif voting_system == "Condorcet Method":
            winners, pairwise_counts = condorcet_method(candidates, votes)
        elif voting_system == "Borda Count":
            winners, borda_scores = borda_count(candidates, votes)
        
        st.header("🏆 Results")
        if winners:
            st.write(f"The winner(s) is/are: 🎉 {winners} 🎉")
            fireworks_animation()  # Trigger fireworks animation
        else:
            st.write("No winner could be determined. 🤷‍♂")
        
        if voting_system == "First Past the Post":
            st.write("Vote Counts: 📊", vote_counts)
        elif voting_system == "Approval Voting":
            st.write("Approval Counts: ✅", approval_counts)
        elif voting_system == "Preferential Voting":
            st.write("Vote Counts: 📊", vote_counts)
        elif voting_system == "Condorcet Method":
            st.write("Pairwise Counts: 🤼", pairwise_counts)
        elif voting_system == "Borda Count":
            st.write("Borda Scores: 🏅", borda_scores)

if __name__ == "__main__":
    main()