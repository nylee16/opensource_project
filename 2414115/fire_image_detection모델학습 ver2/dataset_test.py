"""
import os

base = r'C:/Users/admin/2414115/firedetection-6'
print('data.yaml:', os.path.exists(os.path.join(base, 'data.yaml')))
print('train/images:', os.path.exists(os.path.join(base, 'train', 'images')))
print('train/labels:', os.path.exists(os.path.join(base, 'train', 'labels')))
print('valid/images:', os.path.exists(os.path.join(base, 'valid', 'images')))
print('valid/labels:', os.path.exists(os.path.join(base, 'valid', 'labels')))
"""

import os
import glob

def check_dataset_structure(dataset_path):
    """
    YOLOv8 데이터셋 구조와 파일 존재 여부를 확인하는 함수
    """
    print(f"=== 데이터셋 구조 확인: {dataset_path} ===\n")
    
    # 1. 기본 폴더 존재 확인
    folders_to_check = ['train', 'valid', 'test']
    subfolders_to_check = ['images', 'labels']
    
    for folder in folders_to_check:
        folder_path = os.path.join(dataset_path, folder)
        print(f"📁 {folder}/ 폴더:")
        print(f"   존재 여부: {os.path.exists(folder_path)}")
        
        if os.path.exists(folder_path):
            for subfolder in subfolders_to_check:
                subfolder_path = os.path.join(folder_path, subfolder)
                exists = os.path.exists(subfolder_path)
                print(f"   📁 {folder}/{subfolder}/ 존재: {exists}")
                
                if exists:
                    # 이미지 파일 개수 확인
                    if subfolder == 'images':
                        img_files = glob.glob(os.path.join(subfolder_path, "*.jpg")) + \
                                   glob.glob(os.path.join(subfolder_path, "*.jpeg")) + \
                                   glob.glob(os.path.join(subfolder_path, "*.png"))
                        print(f"      📷 이미지 파일 개수: {len(img_files)}")
                        if len(img_files) > 0:
                            print(f"      📷 첫 번째 이미지: {os.path.basename(img_files[0])}")
                    
                    # 라벨 파일 개수 확인
                    elif subfolder == 'labels':
                        label_files = glob.glob(os.path.join(subfolder_path, "*.txt"))
                        print(f"      🏷️  라벨 파일 개수: {len(label_files)}")
                        if len(label_files) > 0:
                            print(f"      🏷️  첫 번째 라벨: {os.path.basename(label_files[0])}")
        print()
    
    # 2. data.yaml 파일 확인
    yaml_files = ['data.yaml', 'data.yml', 'data']
    yaml_found = False
    
    print("📄 설정 파일 확인:")
    for yaml_name in yaml_files:
        yaml_path = os.path.join(dataset_path, yaml_name)
        if os.path.exists(yaml_path):
            print(f"   ✅ {yaml_name} 존재")
            yaml_found = True
            
            # data.yaml 내용 미리보기
            try:
                with open(yaml_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print(f"   📝 {yaml_name} 내용 (처음 10줄):")
                    lines = content.split('\n')[:10]
                    for i, line in enumerate(lines, 1):
                        print(f"      {i:2}: {line}")
                    if len(content.split('\n')) > 10:
                        print(f"      ... (총 {len(content.splitlines())}줄)")
            except Exception as e:
                print(f"   ❌ 파일 읽기 오류: {e}")
            break
    
    if not yaml_found:
        print("   ❌ data.yaml 파일을 찾을 수 없습니다")
    
    print()
    
    # 3. 이미지-라벨 매칭 확인
    print("🔗 이미지-라벨 매칭 확인:")
    for folder in folders_to_check:
        images_path = os.path.join(dataset_path, folder, 'images')
        labels_path = os.path.join(dataset_path, folder, 'labels')
        
        if os.path.exists(images_path) and os.path.exists(labels_path):
            img_files = glob.glob(os.path.join(images_path, "*.jpg")) + \
                       glob.glob(os.path.join(images_path, "*.jpeg")) + \
                       glob.glob(os.path.join(images_path, "*.png"))
            
            matched = 0
            unmatched_images = []
            
            for img_file in img_files:
                img_name = os.path.splitext(os.path.basename(img_file))[0]
                label_file = os.path.join(labels_path, f"{img_name}.txt")
                if os.path.exists(label_file):
                    matched += 1
                else:
                    unmatched_images.append(img_name)
            
            print(f"   📁 {folder}/:")
            print(f"      총 이미지: {len(img_files)}")
            print(f"      매칭된 라벨: {matched}")
            print(f"      매칭 비율: {matched/len(img_files)*100 if img_files else 0:.1f}%")
            
            if unmatched_images and len(unmatched_images) <= 5:
                print(f"      매칭되지 않은 이미지: {unmatched_images}")
            elif len(unmatched_images) > 5:
                print(f"      매칭되지 않은 이미지: {unmatched_images[:5]}... (총 {len(unmatched_images)}개)")

if __name__ == '__main__':
    # 데이터셋 경로 설정
    dataset_path = r'C:/Users/admin/2414115 - ver2/firedetection-7'
    
    # 데이터셋 구조 확인 실행
    check_dataset_structure(dataset_path)
    
    print("\n" + "="*60)
    print("💡 문제 해결 팁:")
    print("1. 모든 폴더가 존재해야 합니다 (train, valid, test)")
    print("2. 각 폴더 안에 images와 labels 하위폴더가 있어야 합니다")
    print("3. 이미지와 라벨 파일명이 정확히 일치해야 합니다")
    print("4. data.yaml 파일이 firedetection-7 폴더에 있어야 합니다")
    print("5. 매칭 비율이 100%에 가까워야 정상입니다")
