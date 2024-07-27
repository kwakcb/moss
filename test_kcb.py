import streamlit as st
import streamlit.components.v1 as components

# 제목을 표시합니다
st.title("ktMOS")

ip_address = st.text_input("Enter the IP address:")

# 여러 개의 추가 텍스트 정의
additional_texts = [
    "sh arp pon | inc ",
    "sh epon ip-macs all all | inc ",
]


# IP 주소가 입력된 경우에만 처리
if ip_address:
    # 각 추가 텍스트와 IP 주소 결합하여 출력
    for text in additional_texts:
        combined_text = text + ip_address
        st.write(combined_text)

# 코드 블록을 표시합니다
st.code("DB 작업중.....")
st.code("Link 현행화.....")
st.code("★장비교체 완료 NeOSS, NMS, SDN")

# 리스트박스에 표시할 항목 목록 정의
options = ["NOC_광레벨불", "NOC_PLK_PSU교체", "NOC_PSU교체", "NOC_민원처리"]

# 리스트박스 생성
selected_option = st.selectbox("BS HEAD", options)

# 클립보드로 복사 버튼 생성
if st.button("Copy to Clipboard"):
    # JavaScript 코드와 HTML을 통해 클립보드 복사 기능 구현
    components.html(
        f"""
        <script>
        function copyToClipboard(text) {{
            navigator.clipboard.writeText(text).then(function() {{
                console.log('Copying to clipboard was successful!');
            }}, function(err) {{
                console.error('Could not copy text: ', err);
            }});
        }}
        copyToClipboard("{selected_option}");
        </script>
        """,
        height=0,
    )


# 선택된 항목을 화면에 표시
st.write(f"{selected_option}")
