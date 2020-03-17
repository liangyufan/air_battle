package ui;

import javax.swing.*;
import java.awt.*;

public class JFrameGame extends JFrame {
    public JFrameGame() throws HeadlessException {
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.setTitle("Java飞机大战");
        this.setSize(600, 800);
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension screenSize = toolkit.getScreenSize();
        this.setLocation((screenSize.width - this.getWidth()) / 2, (screenSize.height - this.getHeight()) / 2);
        this.setContentPane(new JPanelGame());
    }
}
