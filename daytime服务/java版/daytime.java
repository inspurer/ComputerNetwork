/**
 * Ubuntu下编写自己的DAYTIME客户端，并在互联网上找一个DAYTIME服务器连接，
 * 验证结果，打印代码和运行的输出结果。
 * www.unpbook.com
 */

import java.io.*;
import java.net.*;
public class daytimetest {
 
    /**
     * @param args
     */
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        String sHostName;
        /*
         * Get the name of the server from the command line. No entry,use
         * tock.usno.navy.mil
         */
        if(args.length>0){
            sHostName = args[0];
        }
        else{
        	//"www.time.ac.cn" 或 "time.nist.gov"
            sHostName = "time.nist.gov";
        }
        /*
         * Opeb a socket to port 13. Prepare to receive the Daytime information.
         */
        try{
            Socket oSocket = new Socket(sHostName,13);
            InputStream oTimeStream =oSocket.getInputStream();
            StringBuffer oTime = new StringBuffer();
             
            // Fetch the Daytime information.
            int iCharacter;
            while((iCharacter = oTimeStream.read()) != -1){
                oTime.append((char)iCharacter);
            }
            // Convert Daytime to a String and output.
            String sTime = oTime.toString().trim();
            System.out.println("It's:" + sTime + "at " + sHostName + ".");
            oTimeStream.close();
            oSocket.close();
             
        }catch (UnknownHostException e){
            System.err.print(e);
        }catch (IOException e){
            System.err.print(e);
        }
    }
}