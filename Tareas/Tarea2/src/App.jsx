import { useEffect, useRef } from 'react'

function App() {
  const videoRef = useRef(null);

  useEffect(() => {
    let stream = null;

    const enableStream = async () => {
      try {
        if (navigator.mediaDevices.getUserMedia) {
          stream = await navigator.mediaDevices.getUserMedia({ video: true });
          if (videoRef.current) videoRef.current.srcObject = stream;
        }
      } catch (err) {
        console.error("Error al acceder a la cámara: ", err);
      }
    };

    enableStream();

    return () => {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }
    };
  }, []);

  return (
    <>
      <div >
        <div className="d-flex justify-content-center">
          <p style={{'font-size': '50px', 'font-weight': 'bold', 'text-align': 'center'}}>José Luis Reynoso Tiu <br /> 201345126 </p>
        </div>
        <div className="d-flex justify-content-center">
          <video ref={videoRef} width="auto" height="auto" autoPlay></video>
        </div>
      </div>

    </>
  )
}

export default App
