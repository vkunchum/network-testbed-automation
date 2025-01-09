import os
import subprocess

def deploy_vm(vm_name, cpu, memory, disk_size, iso_path):
        print(f"Deploying {vm_name}...")
            os.system(f"VBoxManage createvm --name {vm_name} --register")
                os.system(f"VBoxManage modifyvm {vm_name} --cpus {cpu} --memory {memory} --vram 16")
                    os.system(f"VBoxManage createhd --filename {vm_name}.vdi --size {disk_size}")
                        os.system(f"VBoxManage storagectl {vm_name} --name 'SATA Controller' --add sata --controller IntelAhci")
                            os.system(f"VBoxManage storageattach {vm_name} --storagectl 'SATA Controller' --port 0 --device 0 --type hdd --medium {vm_name}.vdi")
                                os.system(f"VBoxManage storageattach {vm_name} --storagectl 'SATA Controller' --port 1 --device 0 --type dvddrive --medium {iso_path}")
                                    os.system(f"VBoxManage modifyvm {vm_name} --nic1 nat")
                                        os.system(f"VBoxManage startvm {vm_name}")

                                        if __name__ == "__main__":
                                                deploy_vm("Test-VM", 2, 2048,
                                                          20000,
                                                          "/path/to/iso")

