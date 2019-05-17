using UnityEngine;
using UnityEngine.UI;

namespace ZenFulcrum.EmbeddedBrowser
{
    [RequireComponent(typeof(Browser))]
    public class HeadBrowserSpawner : MonoBehaviour, INewWindowHandler
    {
        public Transform spawnPosition;
        public float size;
        public Camera cameraForNewWindow;

        public void Start()
        {
            GetComponent<Browser>().SetNewWindowHandler(Browser.NewWindowAction.NewBrowser, this);
        }

        public Browser CreateBrowser(Browser parent)
        {
            //var ball = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            //ball.AddComponent<Rigidbody>();
            //ball.transform.localScale = new Vector3(size, size, size);
            //ball.transform.position = spawnPosition.position;

            //var browser = ball.AddComponent<Browser>();
            //browser.UIHandler = null;
            //browser.Resize(110, 110);

            //return browser;

            var newCanvas = new GameObject("Canvas");
            Canvas c = newCanvas.AddComponent<Canvas>();
            c.renderMode = RenderMode.WorldSpace;
            // lisää event camera
            c.worldCamera = cameraForNewWindow;

            newCanvas.AddComponent<CanvasScaler>();
            newCanvas.AddComponent<GraphicRaycaster>();

            var browser = newCanvas.AddComponent<Browser>();
            browser.UIHandler = null;
            browser.Resize(750, 750);
            return browser;
        }

    }
}