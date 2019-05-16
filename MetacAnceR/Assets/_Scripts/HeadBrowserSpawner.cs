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
            return null;
        }

    }
}