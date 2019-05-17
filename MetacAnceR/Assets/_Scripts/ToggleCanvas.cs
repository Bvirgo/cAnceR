using UnityEngine;

public class ToggleCanvas : MonoBehaviour
{

    public void ToggleVisibility()
    {
        Canvas c = gameObject.GetComponent<Canvas>();
        if (c.enabled)
        {
            c.enabled = false;
        }
        else
        {
            c.enabled = true;
        }
    }
}
