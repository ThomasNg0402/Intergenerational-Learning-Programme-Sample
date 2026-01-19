import streamlit as st
from streamlit import components
import base64
import os

# Page configuration
st.set_page_config(
    page_title="ILP Workshop Registration",
    page_icon="🎓",
    layout="wide"
)

# Function to encode images to base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

# Load images
rainbow_keychain = get_base64_image("img/rainbow_keychain.png")
origami_cats = get_base64_image("img/origami_cats.png")
printer_3d = get_base64_image("img/3d_printer.jpg")

# HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ILP Workshop Registration</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }}

        .page {{
            display: none;
        }}

        .page.active {{
            display: block;
        }}

        /* Header */
        header {{
            background: white;
            padding: 20px;
            border-bottom: 2px solid #e0e0e0;
        }}

        .header-content {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            gap: 20px;
        }}

        .search-box {{
            border: 2px solid #8b2332;
            padding: 10px 15px;
            border-radius: 5px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .search-box input {{
            border: none;
            outline: none;
            color: #8b2332;
            font-size: 14px;
        }}

        .logo {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .logo-circle {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 2px solid #8b2332;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #8b2332;
            font-weight: bold;
        }}

        .logo-text {{
            color: #333;
            font-size: 16px;
        }}

        /* Course Listing */
        .course-grid {{
            max-width: 1200px;
            margin: 40px auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 0 20px;
        }}

        .course-card {{
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            cursor: pointer;
            transition: transform 0.2s;
        }}

        .course-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }}

        .course-image {{
            width: 100%;
            height: 200px;
            object-fit: cover;
        }}

        .course-info {{
            padding: 20px;
        }}

        .course-title {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #333;
        }}

        .course-provider {{
            font-style: italic;
            color: #666;
            margin-bottom: 10px;
        }}

        .stars {{
            color: #ffd700;
        }}

        /* Course Details */
        .course-details {{
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
        }}

        .description-box {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            margin-bottom: 30px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .details-box {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .details-box h2 {{
            margin-bottom: 20px;
            color: #333;
        }}

        .detail-row {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #e0e0e0;
        }}

        .detail-item {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .detail-label {{
            font-weight: bold;
            color: #333;
        }}

        .cta-button {{
            background: #8b2332;
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-size: 16px;
            cursor: pointer;
            display: block;
            margin: 30px auto;
            transition: background 0.3s;
        }}

        .cta-button:hover {{
            background: #6d1b27;
        }}

        /* Registration Form */
        .registration-container {{
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }}

        .form-section {{
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}

        .section-header {{
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 25px;
        }}

        .icon-circle {{
            width: 50px;
            height: 50px;
            background: #e8d9ff;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #7c3aed;
            font-size: 24px;
        }}

        .section-title {{
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }}

        .form-group {{
            margin-bottom: 20px;
        }}

        .form-label {{
            display: block;
            margin-bottom: 8px;
            color: #333;
            font-weight: 500;
        }}

        .form-input {{
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 14px;
            color: #333;
        }}

        .form-input:focus {{
            outline: none;
            border-color: #7c3aed;
        }}

        .checkbox-group {{
            display: flex;
            align-items: center;
            gap: 10px;
            margin-top: 15px;
        }}

        .checkbox-group input[type="checkbox"] {{
            width: 20px;
            height: 20px;
            cursor: pointer;
        }}

        .submit-button {{
            width: 100%;
            background: #7c3aed;
            color: white;
            border: none;
            padding: 15px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            margin-top: 10px;
            transition: background 0.3s;
        }}

        .submit-button:hover {{
            background: #6d28d9;
        }}

        .participants-section {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 300px;
        }}

        .empty-state {{
            text-align: center;
            color: #999;
        }}

        .empty-icon {{
            font-size: 60px;
            color: #ddd;
            margin-bottom: 20px;
        }}

        .back-button {{
            background: #666;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            margin: 20px;
        }}

        .back-button:hover {{
            background: #555;
        }}

        .participant-list {{
            width: 100%;
        }}

        .participant-item {{
            background: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 10px;
            border-left: 4px solid #7c3aed;
        }}

        .participant-name {{
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
        }}

        .participant-email {{
            color: #666;
            font-size: 14px;
        }}

        .wheelchair-badge {{
            display: inline-block;
            background: #e8d9ff;
            color: #7c3aed;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 12px;
            margin-top: 5px;
        }}
    </style>
</head>
<body>
    <!-- Page 1: Course Listing and Details -->
    <div id="coursePage" class="page active">
        <header>
            <div class="header-content">
                <div class="search-box">
                    <span>Type to Search</span>
                    <span>🔍</span>
                </div>
                <div class="logo">
                    <div class="logo-circle">ILP</div>
                    <div class="logo-text">Intergenerational Learning Programme (ILP)</div>
                </div>
            </div>
        </header>

        <div class="course-grid">
            <div class="course-card">
                <img src="data:image/png;base64,{rainbow_keychain}" alt="Braided Bliss Workshop" class="course-image">
                <div class="course-info">
                    <div class="course-title">Braided Bliss: T-Shirt Keychain Workshop</div>
                    <div class="course-provider">Family Central</div>
                    <div class="stars">☆☆☆☆☆</div>
                </div>
            </div>

            <div class="course-card">
                <img src="data:image/png;base64,{origami_cats}" alt="Napkin Origami" class="course-image">
                <div class="course-info">
                    <div class="course-title">Napkin Origami Folding</div>
                    <div class="course-provider">Family Central</div>
                    <div class="stars">☆☆☆☆☆</div>
                </div>
            </div>

            <div class="course-card" onclick="showDetails()">
                <img src="data:image/jpeg;base64,{printer_3d}" alt="3D Printing" class="course-image">
                <div class="course-info">
                    <div class="course-title">智能设计 - 3D 打印和建模 3D Printing & Modelling</div>
                    <div class="course-provider">En Community Services Society (ECSS)</div>
                    <div class="stars">☆☆☆☆☆</div>
                </div>
            </div>
        </div>

        <div id="detailsSection" style="display: none;">
            <div class="course-details">
                <div class="description-box">
                    <p>In partnership with students from West Spring Primary School, you will learn to make braided keychains from old T-shirts. Suited for interested beginners, you will gain hands-on experience turning old T-shirts into works of art, in the form of vibrant and braided keychains, personalised to your own liking. By the end of the session, you will be able to make your very own creative keychains, made from old and recycled T-shirts. You will also be able to share your creations with friends and family!</p>
                </div>

                <div class="details-box">
                    <h2>Course Details</h2>
                    
                    <div class="detail-row">
                        <div class="detail-item">
                            <span class="detail-label">💲 Full Fee</span>
                            <span>Free</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">⏰ Duration</span>
                            <span>3 hours over 1 session</span>
                        </div>
                    </div>

                    <div class="detail-row">
                        <div class="detail-item">
                            <span class="detail-label">👤 Provider</span>
                            <span>Family Central</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">📞 Contact</span>
                            <span>9685 4812</span>
                        </div>
                    </div>

                    <div class="detail-row">
                        <div class="detail-item">
                            <span class="detail-label">✉️ Email</span>
                            <span>ilp@fycs.org</span>
                        </div>
                        <div class="detail-item">
                            <span class="detail-label">👨‍🏫 Trainer</span>
                            <span>Trainer's profile is currently not available.</span>
                        </div>
                    </div>

                    <p style="text-align: center; font-style: italic; margin: 30px 0;">Kindly head over to course site for exact details</p>

                    <button class="cta-button" onclick="showRegistration()">
                        Click Here to Course Provider's Website
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- Page 2: Registration Form -->
    <div id="registrationPage" class="page">
        <button class="back-button" onclick="showCourse()">← Back to Course</button>
        
        <div class="registration-container">
            <div class="form-section">
                <div class="section-header">
                    <div class="icon-circle">👥+</div>
                    <h2 class="section-title">Add Participant</h2>
                </div>

                <form id="registrationForm">
                    <div class="form-group">
                        <label class="form-label">Full Name</label>
                        <input type="text" class="form-input" id="participantName" placeholder="Enter participant name" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Email Address</label>
                        <input type="email" class="form-input" id="participantEmail" placeholder="Enter email address" required>
                    </div>

                    <div class="checkbox-group">
                        <input type="checkbox" id="wheelchair" name="wheelchair">
                        <label for="wheelchair">Wheelchair accessibility required</label>
                    </div>

                    <button type="submit" class="submit-button">
                        👥+ Register Participant
                    </button>
                </form>
            </div>

            <div class="form-section participants-section">
                <div class="section-header">
                    <div class="icon-circle">👥</div>
                    <h2 class="section-title">Participants</h2>
                </div>

                <div id="participantsList" class="empty-state">
                    <div class="empty-icon">👥</div>
                    <p>No participants registered yet</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        let participants = [];

        function showDetails() {{
            document.getElementById('detailsSection').style.display = 'block';
            window.scrollTo({{ top: document.getElementById('detailsSection').offsetTop - 20, behavior: 'smooth' }});
        }}

        function showRegistration() {{
            document.getElementById('coursePage').classList.remove('active');
            document.getElementById('registrationPage').classList.add('active');
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function showCourse() {{
            document.getElementById('registrationPage').classList.remove('active');
            document.getElementById('coursePage').classList.add('active');
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function updateParticipantsList() {{
            const listContainer = document.getElementById('participantsList');
            
            if (participants.length === 0) {{
                listContainer.innerHTML = `
                    <div class="empty-state">
                        <div class="empty-icon">👥</div>
                        <p>No participants registered yet</p>
                    </div>
                `;
            }} else {{
                let html = '<div class="participant-list">';
                participants.forEach((p, index) => {{
                    html += `
                        <div class="participant-item">
                            <div class="participant-name">${{p.name}}</div>
                            <div class="participant-email">${{p.email}}</div>
                            ${{p.wheelchair ? '<div class="wheelchair-badge">♿ Wheelchair Required</div>' : ''}}
                        </div>
                    `;
                }});
                html += '</div>';
                listContainer.innerHTML = html;
            }}
        }}

        document.getElementById('registrationForm').addEventListener('submit', function(e) {{
            e.preventDefault();
            
            const name = document.getElementById('participantName').value;
            const email = document.getElementById('participantEmail').value;
            const wheelchair = document.getElementById('wheelchair').checked;
            
            participants.push({{
                name: name,
                email: email,
                wheelchair: wheelchair
            }});
            
            updateParticipantsList();
            
            // Clear form
            document.getElementById('participantName').value = '';
            document.getElementById('participantEmail').value = '';
            document.getElementById('wheelchair').checked = false;
            
            alert('Participant registered successfully!');
        }});
    </script>
</body>
</html>
"""

# Render the HTML
components.v1.html(html_content, height=800, scrolling=True)    