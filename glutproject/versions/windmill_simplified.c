#include <GL/glut.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>


float x_angle = 0.0;
float y_angle = 0.0;
float z_angle = 0.0;
float c=1.0;

GLfloat pos[] = { 0.0, 0.0, -10.0, 1.0 };
GLfloat white[] = { 2.5, 2.5, 6.0, 6.0 };
GLfloat red[] = { 0.3, .4, 0.2, 1.0 };
GLfloat deep_blue[] = { 1.6, 0.5, 0.1, 1.0 };
GLfloat shiny[] = { 30.0 };
GLfloat dull[] = { 0.0 };

GLUquadricObj *Cylinder;
enum { X, Y, Z } axis = X;



void mouse_button (int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON )
{
		axis=Z; c=c+0.4;
                      printf("WIND SPEED INCREASE\t SPEED=%fKm/Hr\n\n",c*1.5);
                      glutPostRedisplay();
	}
        else if (button == GLUT_RIGHT_BUTTON )
{
                      axis = Z; c=c-0.4;
                      printf("WIND SPEED DECREASE\t SPEED=%fKm/Hr\n\n",c*1.5);
                      glutPostRedisplay();
}
}

void spin(void)
{
         switch (axis)
                  {
                      case X: x_angle += 1.0;
                                   break;
                      case Y: y_angle += 1.0;
                                   break;
                      case Z: z_angle += c ;
                                   break;
                      default: break;
                  }
         glutPostRedisplay();
}

void display (void)
{
 

	   Cylinder = gluNewQuadric();
    	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    	glMatrixMode(GL_MODELVIEW);
    	glLoadIdentity();
    	glEnable(GL_TEXTURE_2D);
      //Bottom
      
  	 
   
   	glMaterialfv(GL_FRONT, GL_AMBIENT, white);


  	glBegin(GL_QUADS);
   		glNormal3f(0.0, 1.0f, 0.0f);
   		glTexCoord2f(0.0f, 0.0f);
 		glVertex3f(-25.0,-25.0,-44);
  		glTexCoord2f(0.0f, 1.0f);
   		glVertex3f(-25.0,25.0,-44);
   		glTexCoord2f(1.0f, 1.0f);
   		glVertex3f(25.0,25.0,-44);
   		glTexCoord2f(1.0f, 0.0f);
   		glVertex3f(25.0,-25.0,-44);
   	glEnd();

   	glDisable(GL_TEXTURE_2D);
   	glRotatef(0.0,0.0,1.0,0.0);
   	gluCylinder(Cylinder,.4,.4,4,16,20);
  	glMaterialfv(GL_FRONT, GL_AMBIENT, red);
   	

   	glPushMatrix();
   	glutSolidTorus (1.4, 1.4,  6,  6);
   	glutSolidCube(2.5);
   	glPushMatrix();
   	glTranslatef(0.0,-2.0,0.0);
   

   	glPushMatrix();
   	glRotatef(90.0,1.0,0.0,0.0);
  	 glTranslatef(0.0,0.0,-2.0);
   	gluCylinder(Cylinder,1.0,1.5,27,50,50);
   	glPopMatrix();
   	glPopMatrix();
   	glRotatef(z_angle, 0.0, 0.0, 1.0);
   	glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, red);
   	glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, red);

  	glPushMatrix();
   	glTranslatef(0.0,0.0,1.5);
   	glutSolidCone(1.5,2.5,50,50);
   	glPopMatrix();

   	glPushMatrix();		//blade 1
  	 glTranslatef(0.0,0.0,2.2);
   	glRotatef(90.0,1.0,0.0,0.0);
  	 glPushMatrix();
   	glRotatef(120,0.0,1.0,0.0);
   	glutSolidCone(0.9, 16.0, 15, 15);
   	glPopMatrix();
   	glPopMatrix();

   	glPushMatrix();		//blade 2
   	glTranslatef(0.0,0.0,2.2);
   	glRotatef(90.0,1.0,0.0,0.0);
   	glPushMatrix();
   	glRotatef(-120,0.0,1.0,0.0);
   	glutSolidCone(0.9, 16.0, 15, 15);
   	glPopMatrix();
  	 glPopMatrix();

  	 glPushMatrix();		 //blade 3 
   	glTranslatef(0.0,0.0,2.2);
  	 glRotatef(90.0,1.0,0.0,0.0);
   	glutSolidCone(0.9, 16.0, 15, 15);
   	glPopMatrix();
   
    
   	glutSwapBuffers();
    
}

void init (void)
{
        glMatrixMode(GL_PROJECTION);
        glOrtho(-25.0, 25.0, -25.0, 25.0, -250.0, 250.0);
        glEnable(GL_LIGHTING);
        glEnable(GL_LIGHT0);
        //glEnable(GL_LIGHT1);
       
}


 

int main (int argc, char *argv[ ])
{
glutInit(&argc, argv);
	       glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE);
       	glutInitWindowSize(500, 500);
       	glutInitWindowPosition(100, 50);
       	glutCreateWindow("SIMULATION OF WINDMILL");
       	glutIdleFunc(spin);
      	glutDisplayFunc(display);
       	glutMouseFunc(mouse_button);
        init();
	       glEnable(GL_DEPTH_TEST);
       	glutMainLoop();
        return 0;
}



