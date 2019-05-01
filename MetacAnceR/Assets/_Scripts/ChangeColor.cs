using UnityEngine;

public class ChangeColor : MonoBehaviour
{

    private Renderer rend;
    private Color colorAtStartUp;
    private bool onOrOff = false;

    [SerializeField]
    private Color colorToTurnTo = Color.white;


    public void ToggleColor()
    {

        if (!onOrOff)
        {
            onOrOff = true;
            rend.material.color = colorToTurnTo;
        }
        else
        {
            onOrOff = false;
            rend.material.color = colorAtStartUp;
        }

    }
    private void Start()
    {
        rend = gameObject.GetComponent<Renderer>();
        colorAtStartUp = rend.material.color;
    }
}
