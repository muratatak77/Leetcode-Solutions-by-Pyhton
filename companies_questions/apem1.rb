class Server
  attr_accessor :ip, :link

  def initialize(ip)
    @ip = ip
    @link = nil
  end
end


# server1 -> server2 -> server3 -> server1

def find_loop(server1)
    server = server1
    
    i = 0
    while server.link do

        begin
          
            server = server.link
            
            print("server ip : ", server.ip)
            puts""

            if server.link == server1
                return true
            end

        if i == 100
            puts "i : 100"
            break
        end
        i+= 1

        rescue Exception => e

            
        end
    end

    print("server ip : ", server.ip)
    puts""

    return false

    #server1 -> server2 -> server3 -> server2
    
    #{
    #server1:server2
    #server2:server3
    #server3:server1
    #}
        
    # server.link = server2 
    
    # there is a loop > server1 -> server2 -> server3 -> server1
    #  return true
    #no loop
    #  return flalse
    
end


server1 = Server.new('0.0.0.0')
server2 = Server.new('0.0.0.1')
server3 = Server.new('0.0.0.2')
server4 = Server.new('0.0.0.3')

server1.link = server2
server2.link = server3
server3.link = server2


res = find_loop(server4)
print("res : ", res)
puts ""
