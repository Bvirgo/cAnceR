using UnityEngine;

namespace ZenFulcrum.EmbeddedBrowser
{
    [RequireComponent(typeof(Browser))]
    public class HeadBrowserSpawner : MonoBehaviour, INewWindowHandler
    {
        public Transform spawnPosition;
        public float size;

        public void Start()
        {
            GetComponent<Browser>().SetNewWindowHandler(Browser.NewWindowAction.NewBrowser, this);
        }

        public Browser CreateBrowser(Browser parent)
        {
            var ball = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            ball.AddComponent<Rigidbody>();
            ball.transform.localScale = new Vector3(size, size, size);
            ball.transform.position = spawnPosition.position;

            var browser = ball.AddComponent<Browser>();
            browser.UIHandler = null;
            browser.Resize(110, 110);

            return browser;
        }

    }
}