from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1402_1 ._SN',
        MapName             = 'Bose',
        Location            = 'T1402.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1402   ._SN',
            'ED6_DT21/T1402_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_715C",         # 03, 3
        "Function_4_723D",         # 04, 4
        "Function_5_7292",         # 05, 5
        "Function_6_72FC",         # 06, 6
        "Function_7_7329",         # 07, 7
        "Function_8_7365",         # 08, 8
        "Function_9_7397",         # 09, 9
        "Function_10_73D3",        # 0A, 10
        "Function_11_740F",        # 0B, 11
        "Function_12_744B",        # 0C, 12
        "Function_13_7487",        # 0D, 13
        "Function_14_74BE",        # 0E, 14
        "Function_15_765C",        # 0F, 15
        "Function_16_79D2",        # 10, 16
        "Function_17_7D48",        # 11, 17
        "Function_18_80BE",        # 12, 18
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x17, 0x3)
    OP_A1(0x18, 0x4)
    OP_A1(0x19, 0x5)
    OP_A1(0x1A, 0x6)
    OP_A1(0x1B, 0x7)
    OP_A1(0x1C, 0x8)
    OP_A1(0x1D, 0x9)
    OP_A1(0x1E, 0xA)
    OP_A1(0x1F, 0xB)
    OP_A1(0x20, 0xC)
    OP_A1(0x21, 0xD)
    OP_A1(0x22, 0xE)
    OP_A1(0x23, 0xF)
    OP_A1(0x24, 0x10)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_72(0x5, 0x20)
    OP_72(0x6, 0x20)
    OP_72(0x7, 0x20)
    OP_72(0x8, 0x20)
    OP_72(0x9, 0x20)
    OP_72(0xA, 0x20)
    OP_72(0xB, 0x20)
    OP_72(0xC, 0x20)
    OP_72(0xD, 0x20)
    OP_72(0xE, 0x20)
    OP_72(0xF, 0x20)
    OP_72(0x10, 0x20)
    OP_D2(0x70020, 0x70028, 0x0)
    OP_D2(0x70050, 0x70058, 0x1)
    OP_D2(0x70060, 0x70068, 0x2)
    OP_D2(0x70070, 0x70078, 0x3)
    OP_D2(0x270398, 0x27039C, 0x4)
    OP_D2(0x2701E7, 0x2701EC, 0x5)
    OP_D2(0x2701EE, 0x2701F3, 0x6)
    OP_D2(0x70150, 0x70154, 0x7)
    OP_D2(0x2701D2, 0x2701D7, 0x8)
    OP_D2(0x270202, 0x270207, 0x9)
    OP_D2(0x70120, 0x70124, 0xA)
    OP_D2(0x2701E6, 0x2701EB, 0xB)
    OP_D2(0x60108, 0x6010D, 0xC)
    OP_D2(0x2701D3, 0x2701D8, 0xD)
    OP_D2(0x70142, 0x70146, 0xE)
    OP_D2(0x270080, 0x270084, 0xF)
    OP_D2(0x26023D, 0x260242, 0x10)
    OP_D2(0x270399, 0x27039D, 0x11)
    OP_D2(0x70021, 0x70029, 0x12)
    OP_D2(0x70051, 0x70059, 0x13)
    OP_D2(0x70061, 0x70069, 0x14)
    OP_D2(0x70071, 0x70079, 0x15)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 560)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 2)
    SetChrChipByIndex(0xB, 3)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xE, 6)
    SetChrChipByIndex(0xF, 7)
    SetChrChipByIndex(0x10, 8)
    SetChrChipByIndex(0x27, 9)
    SetChrChipByIndex(0x28, 9)
    SetChrChipByIndex(0x29, 9)
    SetChrChipByIndex(0x2A, 9)
    SetChrChipByIndex(0x2B, 9)
    SetChrChipByIndex(0x2C, 9)
    SetChrChipByIndex(0x2D, 9)
    SetChrChipByIndex(0x2E, 9)
    SetChrChipByIndex(0x2F, 9)
    SetChrChipByIndex(0x30, 9)
    SetChrChipByIndex(0x31, 9)
    SetChrChipByIndex(0x32, 9)
    SetChrChipByIndex(0x33, 9)
    SetChrChipByIndex(0x34, 9)
    SetChrChipByIndex(0x35, 9)
    SetChrChipByIndex(0x36, 9)
    SetChrChipByIndex(0x37, 9)
    SetChrChipByIndex(0x38, 9)
    SetChrChipByIndex(0x39, 9)
    SetChrChipByIndex(0x3A, 9)
    SetChrChipByIndex(0x3B, 9)
    SetChrChipByIndex(0x3C, 9)
    SetChrChipByIndex(0x3D, 9)
    SetChrChipByIndex(0x3E, 9)
    SetChrChipByIndex(0x3F, 9)
    SetChrChipByIndex(0x40, 9)
    SetChrChipByIndex(0x41, 9)
    SetChrChipByIndex(0x42, 9)
    SetChrChipByIndex(0x43, 9)
    SetChrChipByIndex(0x44, 9)
    SetChrChipByIndex(0x45, 9)
    SetChrChipByIndex(0x46, 9)
    SetChrChipByIndex(0x47, 9)
    SetChrChipByIndex(0x48, 9)
    SetChrChipByIndex(0x49, 9)
    SetChrChipByIndex(0x4A, 9)
    SetChrChipByIndex(0x4B, 9)
    SetChrChipByIndex(0x4C, 9)
    SetChrChipByIndex(0x4D, 9)
    SetChrChipByIndex(0x4E, 9)
    SetChrChipByIndex(0x4F, 9)
    SetChrChipByIndex(0x50, 9)
    SetChrChipByIndex(0x51, 9)
    SetChrChipByIndex(0x52, 9)
    SetChrChipByIndex(0x53, 9)
    SetChrChipByIndex(0x54, 9)
    SetChrChipByIndex(0x55, 9)
    SetChrChipByIndex(0x56, 9)
    SetChrChipByIndex(0x57, 9)
    SetChrChipByIndex(0x58, 9)
    SetChrChipByIndex(0x59, 9)
    SetChrChipByIndex(0x5A, 9)
    SetChrChipByIndex(0x5B, 9)
    SetChrChipByIndex(0x5C, 9)
    SetChrChipByIndex(0x5D, 9)
    SetChrChipByIndex(0x5E, 9)
    SetChrChipByIndex(0x5F, 9)
    SetChrChipByIndex(0x60, 9)
    SetChrChipByIndex(0x61, 9)
    SetChrChipByIndex(0x62, 9)
    SetChrChipByIndex(0x63, 9)
    SetChrChipByIndex(0x64, 9)
    SetChrChipByIndex(0x65, 9)
    SetChrChipByIndex(0x66, 9)
    SetChrChipByIndex(0x67, 9)
    SetChrChipByIndex(0x68, 9)
    SetChrChipByIndex(0x69, 9)
    SetChrChipByIndex(0x6A, 9)
    SetChrChipByIndex(0x6B, 9)
    SetChrChipByIndex(0x6C, 9)
    SetChrChipByIndex(0x6D, 9)
    SetChrChipByIndex(0x6E, 9)
    SetChrChipByIndex(0x6F, 9)
    SetChrChipByIndex(0x70, 9)
    SetChrChipByIndex(0x71, 9)
    SetChrChipByIndex(0x72, 9)
    SetChrChipByIndex(0x73, 9)
    SetChrChipByIndex(0x74, 9)
    SetChrChipByIndex(0x75, 9)
    SetChrChipByIndex(0x76, 9)
    SetChrChipByIndex(0x77, 9)
    SetChrChipByIndex(0x78, 9)
    SetChrChipByIndex(0x79, 9)
    SetChrChipByIndex(0x7A, 9)
    SetChrChipByIndex(0x7B, 9)
    SetChrChipByIndex(0x7C, 9)
    SetChrChipByIndex(0x7D, 9)
    SetChrChipByIndex(0x7E, 9)
    SetChrChipByIndex(0x15, 10)
    SetChrChipByIndex(0x16, 10)
    SetChrChipByIndex(0x11, 11)
    SetChrPos(0x17, -7460, 0, 104890, 0)
    SetChrPos(0x18, 3360, 0, 104630, 0)
    SetChrPos(0x19, -7650, 0, 119070, 0)
    SetChrPos(0x1A, 3510, 0, 119050, 0)
    SetChrPos(0x1B, -18530, 0, 108310, 0)
    SetChrPos(0x1C, 15560, 0, 109270, 0)
    SetChrPos(0x1D, -19230, 0, 123310, 0)
    SetChrPos(0x1E, 14300, 0, 123350, 0)
    SetChrPos(0x1F, -8090, 0, 133010, 0)
    SetChrPos(0x20, 3690, 0, 132830, 0)
    SetChrPos(0x21, 2670, 0, 149120, 0)
    SetChrPos(0x22, -8410, 0, 149060, 0)
    SetChrPos(0x23, -19940, 0, 140900, 0)
    SetChrPos(0x24, 12450, 0, 140010, 0)
    SetChrPos(0x27, -7630, 0, 157450, 180)
    SetChrPos(0x28, -5660, -50, 157450, 180)
    SetChrPos(0x29, -3630, 0, 157450, 180)
    SetChrPos(0x2A, -1730, 90, 157450, 180)
    SetChrPos(0x2B, 230, -30, 157450, 180)
    SetChrPos(0x2C, 2070, -30, 157450, 180)
    SetChrPos(0x2D, -7630, 40, 159600, 180)
    SetChrPos(0x2E, -5660, 20, 159600, 180)
    SetChrPos(0x2F, -3630, -20, 159600, 180)
    SetChrPos(0x30, -1730, 50, 159600, 180)
    SetChrPos(0x31, 230, -20, 159600, 180)
    SetChrPos(0x32, 2070, -50, 159600, 180)
    SetChrPos(0x33, -7630, 30, 161750, 180)
    SetChrPos(0x34, -5660, 10, 161750, 180)
    SetChrPos(0x35, -3630, 20, 161750, 180)
    SetChrPos(0x36, -1730, 70, 161750, 180)
    SetChrPos(0x37, 230, -10, 161750, 180)
    SetChrPos(0x38, 2070, -30, 161750, 180)
    SetChrPos(0x39, -7630, -20, 163900, 180)
    SetChrPos(0x3A, -5660, -40, 163900, 180)
    SetChrPos(0x3B, -3630, -40, 163900, 180)
    SetChrPos(0x3C, -1730, 40, 163900, 180)
    SetChrPos(0x3D, 230, -40, 163900, 180)
    SetChrPos(0x3E, 2070, -20, 163900, 180)
    SetChrPos(0x3F, -7630, -40, 166050, 180)
    SetChrPos(0x40, -5660, 0, 166050, 180)
    SetChrPos(0x41, -3630, 30, 166050, 180)
    SetChrPos(0x42, -1730, 60, 166050, 180)
    SetChrPos(0x43, 230, 10, 166050, 180)
    SetChrPos(0x44, 2070, -20, 166050, 180)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    ClearChrFlags(0x40, 0x80)
    ClearChrFlags(0x41, 0x80)
    ClearChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    SetChrFlags(0x27, 0x200)
    SetChrFlags(0x28, 0x200)
    SetChrFlags(0x29, 0x200)
    SetChrFlags(0x2A, 0x200)
    SetChrFlags(0x2B, 0x200)
    SetChrFlags(0x2C, 0x200)
    SetChrFlags(0x2D, 0x200)
    SetChrFlags(0x2E, 0x200)
    SetChrFlags(0x2F, 0x200)
    SetChrFlags(0x30, 0x200)
    SetChrFlags(0x31, 0x200)
    SetChrFlags(0x32, 0x200)
    SetChrFlags(0x33, 0x200)
    SetChrFlags(0x34, 0x200)
    SetChrFlags(0x35, 0x200)
    SetChrFlags(0x36, 0x200)
    SetChrFlags(0x37, 0x200)
    SetChrFlags(0x38, 0x200)
    SetChrFlags(0x39, 0x200)
    SetChrFlags(0x3A, 0x200)
    SetChrFlags(0x3B, 0x200)
    SetChrFlags(0x3C, 0x200)
    SetChrFlags(0x3D, 0x200)
    SetChrFlags(0x3E, 0x200)
    SetChrFlags(0x3F, 0x200)
    SetChrFlags(0x40, 0x200)
    SetChrFlags(0x41, 0x200)
    SetChrFlags(0x42, 0x200)
    SetChrFlags(0x43, 0x200)
    SetChrFlags(0x44, 0x200)
    SetChrFlags(0x45, 0x200)
    SetChrFlags(0x46, 0x200)
    SetChrFlags(0x47, 0x200)
    SetChrFlags(0x48, 0x200)
    SetChrFlags(0x49, 0x200)
    SetChrFlags(0x4A, 0x200)
    SetChrFlags(0x4B, 0x200)
    SetChrFlags(0x4C, 0x200)
    SetChrFlags(0x4D, 0x200)
    SetChrFlags(0x4E, 0x200)
    SetChrFlags(0x4F, 0x200)
    SetChrFlags(0x50, 0x200)
    SetChrFlags(0x51, 0x200)
    SetChrFlags(0x52, 0x200)
    SetChrFlags(0x53, 0x200)
    SetChrFlags(0x54, 0x200)
    SetChrFlags(0x55, 0x200)
    SetChrFlags(0x56, 0x200)
    SetChrFlags(0x57, 0x200)
    SetChrFlags(0x58, 0x200)
    SetChrFlags(0x59, 0x200)
    SetChrFlags(0x5A, 0x200)
    SetChrFlags(0x5B, 0x200)
    SetChrFlags(0x5C, 0x200)
    SetChrFlags(0x5D, 0x200)
    SetChrFlags(0x5E, 0x200)
    SetChrFlags(0x5F, 0x200)
    SetChrFlags(0x60, 0x200)
    SetChrFlags(0x61, 0x200)
    SetChrFlags(0x62, 0x200)
    SetChrFlags(0x63, 0x200)
    SetChrFlags(0x64, 0x200)
    SetChrFlags(0x65, 0x200)
    SetChrFlags(0x66, 0x200)
    SetChrFlags(0x67, 0x200)
    SetChrFlags(0x68, 0x200)
    SetChrFlags(0x69, 0x200)
    SetChrFlags(0x6A, 0x200)
    SetChrFlags(0x6B, 0x200)
    SetChrFlags(0x6C, 0x200)
    SetChrFlags(0x6D, 0x200)
    SetChrFlags(0x6E, 0x200)
    SetChrFlags(0x6F, 0x200)
    SetChrFlags(0x70, 0x200)
    SetChrFlags(0x71, 0x200)
    SetChrFlags(0x72, 0x200)
    SetChrFlags(0x73, 0x200)
    SetChrFlags(0x74, 0x200)
    SetChrFlags(0x75, 0x200)
    SetChrFlags(0x76, 0x200)
    SetChrFlags(0x77, 0x200)
    SetChrFlags(0x78, 0x200)
    SetChrFlags(0x79, 0x200)
    SetChrFlags(0x7A, 0x200)
    SetChrFlags(0x7B, 0x200)
    SetChrFlags(0x7C, 0x200)
    SetChrFlags(0x7D, 0x200)
    SetChrFlags(0x7E, 0x200)
    SetChrPos(0x15, 1600, -20, 50600, 315)
    SetChrPos(0x16, -3370, 30, 50630, 315)
    SetChrPos(0xF, -1440, 40, 53120, 315)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x101, -2540, 40, 55190, 270)
    SetChrPos(0x102, 360, 80, 47660, 315)
    SetChrPos(0x8, -1530, 20, 46400, 315)
    SetChrPos(0x9, 1350, 50, 45360, 315)
    SetChrPos(0xB, 0, 80, 44800, 315)
    SetChrPos(0xA, 610, -30, 46380, 315)
    SetChrPos(0xC, -810, 10, 55140, 270)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xE, -3380, -40, 95890, 270)
    SetChrPos(0xD, -1930, 50, 94710, 270)
    SetChrPos(0x10, -1500, 20, 97080, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x27, -3900, 20, 98320, 270)
    SetChrPos(0x28, 40, 10, 98140, 270)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 330)
    OP_70(0x2, 0x1AE)
    OP_A1(0x25, 0x2)
    SetChrPos(0x25, -38270, 26200, 57080, 30)
    OP_A1(0x26, 0x11)
    SetChrPos(0x26, -38270, 5000, 57080, 30)
    OP_75(0x11, 0x0, 0x0)
    OP_74(0x11, 0x0, 0x7)
    LoadEffect(0x0, "map\\mp021_00.eff")
    LoadEffect(0x1, "map\\onsen00.eff")
    OP_48()
    OP_89(0x11, -29500, 28800, 67950, 90)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x40)
    SetChrBattleFlags(0x11, 0x20)
    OP_48()
    ClearChrFlags(0x11, 0x4)
    OP_22(0x125, 0x1, 0x50)
    ClearMapFlags(0x100000)
    OP_6D(-36460, 10220, 60860, 0)
    OP_67(0, 15110, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(132000, 0)
    OP_6E(500, 0)
    FadeToBright(1000, 0)
    OP_43(0x25, 0x0, 0x1, 0x4)
    OP_43(0x26, 0x0, 0x1, 0x5)

    def lambda_BC2():
        OP_6D(-35940, -30, 58750, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC2)

    def lambda_BDA():
        OP_67(0, 6930, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BDA)

    def lambda_BF2():
        OP_6B(5550, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_BF2)

    def lambda_C02():
        OP_6C(227000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C02)

    def lambda_C12():
        OP_6E(675, 6000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C12)
    StopSound(0x9C40, 0x2A23A, 0x1388)

    def lambda_C2F():
        OP_8F(0xFE, 0xFFFF6A82, 0xC8, 0xDEF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_C2F)

    def lambda_C4A():
        OP_8F(0xFE, 0xFFFF6A82, 0x1450, 0xDEF8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_C4A)

    def lambda_C65():
        OP_8F(0xFE, 0xFFFF8D78, 0x1DB0, 0x10A5E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C65)
    Sleep(1500)

    def lambda_C85():
        OP_8F(0xFE, 0xFFFF6A82, 0x1450, 0xDEF8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_C85)
    PlayEffect(0x0, 0x0, 0xFF, -39070, -150, 58410, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    Sleep(2000)

    def lambda_CDF():
        OP_8F(0xFE, 0xFFFF6A82, 0x1450, 0xDEF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_CDF)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0x25, 0x0)
    OP_82(0x0, 0x2)
    OP_23(0xCC)
    OP_23(0x125)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_48()
    OP_89(0x11, -29320, 7600, 68190, 90)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x40)
    SetChrBattleFlags(0x11, 0x20)
    OP_6D(-29380, 8600, 68010, 0)
    OP_67(0, 6340, -10000, 0)
    OP_6B(1890, 0)
    OP_6C(255000, 0)
    OP_6E(474, 0)
    OP_11(0xA0, 0xB4, 0xFF, 0x9C40, 0x245C1, 0x0)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #0
        0x11,
        (
            "#1125F#5PThis is our proof, men of Erebonia.\x02\x03",

            "#1120FFeel free to feast your eyes upon it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1008FDad!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xE, -17920, -260, 72900, 180)
    SetChrPos(0xD, -17700, -290, 72030, 180)

    ChrTalk(    #2
        0xE,
        "#883F#5PC-CASSIUS BRIGHT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "#1120F#5PIt's been a while, Zechs.\x02\x03",

            "#1124FThey finally gave you a\x01",
            "second star, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xE,
        (
            "#886F#5PThat's beside the point!\x02\x03",

            "#885FWhy are you here?\x01",
            "And what is that ship?!\x02\x03",

            "How is it capable of flying?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x11,
        (
            "#1125F#5PThat, unfortunately, is a national secret.\x02\x03",

            "#1122FRather like those steam tanks\x01",
            "of yours, I would say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xE,
        "#886F#5PGh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xD,
        (
            "#892F#5PHmmm! So this is the Arseille, is it?\x02\x03",

            "And you must be the famed Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#1125F#5PI believe this is the first time we have\x01",
            "had an audience, Your Highness.\x02\x03",

            "#1120FStrange, though...\x01",
            "I feel as if we've met somewhere before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xD,
        (
            "#894F#5PHow curious, General Bright!\x02\x03",

            "#890FI was just thinking the same thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "#1124F#5PHow very curious!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        "#894F#5PIsn't it, though?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #12
        0xD,
        "#891F#5PHahahaha!\x02",
    )


    ChrTalk(    #13
        0x11,
        "#1121F#5PHahahaha!\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #14
        0xE,
        "#885F#5P#4SM-My prince!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-950, 40, 92660, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(147000, 0)
    OP_6E(495, 0)
    SetChrPos(0xE, -3380, -40, 95890, 135)
    SetChrPos(0xD, -1930, 50, 94710, 270)

    def lambda_11FC():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_11FC)

    def lambda_120A():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_120A)

    def lambda_1218():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_1218)
    OP_8C(0xD, 180, 0)

    def lambda_122D():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_122D)
    OP_0D()
    Sleep(500)

    ChrTalk(    #15
        0xD,
        (
            "#890F#5PMiss Bright. Princess Klaudia.\x02\x03",

            "I am a proud member of the Erebonian\x01",
            "Imperial family. I will keep my word.\x02\x03",

            "General, have all our forces withdraw\x01",
            "from this area immediately.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_12FC():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12FC)

    def lambda_130A():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_130A)

    ChrTalk(    #16
        0x101,
        "#1017F#3POlivier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        "#1168F#3PYou have our gratitude...Prince Olivert.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xD,
        (
            "#894F#5PStill, though...\x02\x03",

            "My dear citizens will doubtlessly not\x01",
            "be satisfied with mere possibility\x01",
            "being presented to them.\x02\x03",

            "#892FPerhaps I could board the Arseille\x01",
            "and observe for myself?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #19
        0xE,
        "#883F#5PPrince Olivert?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-940, 0, 52290, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(3410, 0)
    OP_6C(171000, 0)
    OP_6E(304, 0)
    SetChrPos(0x15, 1600, -20, 50600, 0)
    SetChrPos(0x16, -3370, 30, 50630, 0)
    SetChrPos(0xF, -1440, 40, 53120, 0)
    SetChrPos(0x101, -2540, 40, 55190, 0)
    SetChrPos(0x102, -500, 80, 47660, 0)
    SetChrPos(0x8, -1530, 20, 46400, 0)
    SetChrPos(0x9, 1350, 50, 45360, 0)
    SetChrPos(0xB, 0, 80, 44800, 0)
    SetChrPos(0xA, 610, -30, 46380, 0)
    SetChrPos(0xC, -810, 10, 55140, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x11, -12350, -70, 82680, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(    #20
        0x11,
        (
            "#1125F#5PA good idea. I'm sure everyone in\x01",
            "the Imperial government would be\x01",
            "satisfied with the prince as a witness.\x02\x03",

            "#1120FPrincess Klaudia? Shall we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        (
            "#1167F#6POf course.\x01",
            "I see no reason to object.\x02\x03",

            "I am sure this will only further strengthen\x01",
            "the bond of friendship between Erebonia\x01",
            "and Liberl.\x02\x03",

            "#1168FWelcome aboard, Prince Olivert.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-1440, 30, 143110, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(2120, 0)
    OP_6C(45000, 0)
    OP_6E(488, 0)
    SetChrPos(0xE, -2070, 40, 143810, 180)
    SetChrPos(0xD, -2510, 30, 141080, 0)
    SetChrPos(0x10, -1780, 50, 140180, 0)
    SetChrPos(0x27, -7630, 0, 157450, 180)
    SetChrPos(0x28, -5660, -50, 157450, 180)
    SetChrPos(0x11, -29320, 7500, 68190, 90)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0x10, 0)

    def lambda_17A6():
        OP_6B(1700, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17A6)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #22
        0xE,
        (
            "#885F#6PPRINCE OLIVERT!\x01",
            "What have you DONE?!\x02\x03",

            "You finally stride onto the public stage\x01",
            "for the first time in ages, and you\x01",
            "engage in this...this...charade?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xD,
        (
            "#891F#2PHahaha... Ah, I suppose we were\x01",
            "too transparent at the end, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xE,
        (
            "#886F#6PTransparent like AIR!\x02\x03",

            "To think that a prince of the Empire\x01",
            "would plan something like, like THIS,\x01",
            "in Liberl...\x02\x03",

            "#885FMueller! How could you let this happen?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#272F#2PForgive me, Uncle...\x02\x03",

            "...but do you really think this idiot would\x01",
            "listen even if I asked him to stop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xE,
        "#886F#6PErgh. Well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#270F#2PBesides...there are elements of this\x01",
            "which do not sit easily on my conscience.\x02\x03",

            "I learned all about the truth behind\x01",
            "Hamel during this mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xE,
        "#883F#6PGh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#276F#2PSo you did know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xD,
        (
            "#891F#2PHaha! How could he not know?\x02\x03",

            "#890FEven back then, he was a critical part\x01",
            "of the military chain of command.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xE,
        "#884F#6P...My shame is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xD,
        (
            "#891F#2PNo, Zechs. I do not blame you.\x02\x03",

            "It was a subsection of the war hawks.\x01",
            "I know you had nothing to do with it.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 270, 400)
    Sleep(500)

    ChrTalk(    #33
        0xD,
        (
            "#894F#5PA scandal so vile that information about\x01",
            "it had to be tightly controlled...\x02\x03",

            "I do not agree with the logic,\x01",
            "but I understand it.\x02\x03",

            "Seal up that which stinks and bury it forever.\x01",
            "Those who rule remain in power, unblemished.\x02\x03",

            "#897FHowever.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    Sleep(500)

    ChrTalk(    #34
        0xD,
        (
            "#896F#2PI cannot allow the same trick\x01",
            "to be played twice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xE,
        "#883F#6PPrince...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        (
            "#897F#2PZechs, you realized it yourself,\x01",
            "I'm sure.\x02\x03",

            "The incredibly fortuitous addition of\x01",
            "these steam tanks to our arsenal...\x02\x03",

            "The convenient orders to sortie...\x02\x03",

            "#899FEvery bit of it has the fingerprints\x01",
            "of the Blood and Iron Chancellor\x01",
            "himself, Giliath Osborne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        "#882F#6PWhat are--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "#899F#2PHe's in contact with Ouroboros.\x02\x03",

            "I no longer doubt it.\x02\x03",

            "#895FAnd, personally, I find the idea of a\x01",
            "chancellor whose first loyalty is not\x01",
            "to the Empire rather repugnant.\x02\x03",

            "Don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xE,
        (
            "#884F#6P...\x02\x03",

            "#882FMy prince. You can't possibly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xD,
        (
            "#890F#2PHeh, but I do indeed.\x02\x03",

            "#894FThe former military man who has become\x01",
            "the Empire's central politician after rising\x01",
            "to prominence ten years ago...\x02\x03",

            "The cold-blooded yet bold reformer who laid rails\x01",
            "throughout the Empire and has annexed many of our\x01",
            "neighbors through force of arms...\x02\x03",

            "#896FI have decided to slay the beloved monster\x01",
            "which has made its nest in our Empire.\x02\x03",

            "You may call all of this my declaration of war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xE,
        (
            "#884F#6PUnbelievable.\x02\x03",

            "#882FMy prince, do you even realize what\x01",
            "you are attempting to accomplish?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "#895F#2PI like to tell myself I do, at least.\x02\x03",

            "#893FHe is not only politically strong, but he\x01",
            "has de facto control of easily seven-tenths\x01",
            "of the military.\x02\x03",

            "Putting aside neutral people like yourself,\x01",
            "all who stand against him are the nation's feudal\x01",
            "lords, and their influence weakens by the day.\x02\x03",

            "Worse still, my father's trust in\x01",
            "him is nearly absolute.\x02\x03",

            "#892FThe very picture of a monster, I would say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        "#885F#6PThen why even--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "#894F#2PHeh, is it not obvious?\x02\x03",

            "#890FBecause the way he acts is not beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xE,
        "#883F#6P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        (
            "#891F#2PMy eyes were opened as I traveled Liberl.\x02\x03",

            "People and countries are at their greatest\x01",
            "when they are proud...of themselves.\x02\x03",

            "#890FAnd I wish for my people, my fatherland,\x01",
            "to feel the same pride. To be proud of\x01",
            "accomplishments, not conquests.\x02\x03",

            "I hope you can understand, Zechs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xE,
        (
            "#883F#6P...\x02\x03",

            "#884F...My prince.\x01",
            "You've become quite a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        (
            "#891F#2PHeh, as they say!\x01",
            "Only an unwatched pot will boil!\x02\x03",

            "#890FIt's been seven years since you\x01",
            "took me under your wing to teach\x01",
            "me what you knew, Zechs.\x02\x03",

            "I simply learned to apply what you taught\x01",
            "when you weren't looking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xE,
        (
            "#884F#6PHeh... Indeed.\x02\x03",

            "#882FVery well. I will pull my forces back.\x02\x03",

            "I must remind you, however, that the\x01",
            "3rd division was merely the vanguard.\x02\x03",

            "Osborne is mustering another ten\x01",
            "divisions in the capital.\x02\x03",

            "#884FThree days...and then they march.\x01",
            "That's your deadline.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xD,
        (
            "#895F#2PYes...\x01",
            "We'll act with all haste, Zechs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xE,
        (
            "#881F#6PMueller. You're going with Prince Olivert\x01",
            "I take it?\x02\x03",

            "If things go poorly, bring him back,\x01",
            "even if you have to drag him by\x01",
            "his collar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        "#277F#2PI imagine I'll have to do so, either way.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x45, 4000, 0, 157450, 180)
    SetChrPos(0x46, 5930, -50, 157450, 180)
    SetChrPos(0x47, 7900, 0, 157450, 180)
    SetChrPos(0x48, 9800, 90, 157450, 180)
    SetChrPos(0x49, 11700, -30, 157450, 180)
    SetChrPos(0x4A, 13540, -30, 157450, 180)
    SetChrPos(0x4B, 4000, 40, 159600, 180)
    SetChrPos(0x4C, 5930, 20, 159600, 180)
    SetChrPos(0x4D, 7900, -20, 159600, 180)
    SetChrPos(0x4E, 9800, 50, 159600, 180)
    SetChrPos(0x4F, 11700, -20, 159600, 180)
    SetChrPos(0x50, 13540, -50, 159600, 180)
    SetChrPos(0x51, 4000, 30, 161750, 180)
    SetChrPos(0x52, 5930, 10, 161750, 180)
    SetChrPos(0x53, 7900, 20, 161750, 180)
    SetChrPos(0x54, 9800, 70, 161750, 180)
    SetChrPos(0x55, 11700, -10, 161750, 180)
    SetChrPos(0x56, 13540, -30, 161750, 180)
    SetChrPos(0x57, 4000, -20, 163900, 180)
    SetChrPos(0x58, 5930, -40, 163900, 180)
    SetChrPos(0x59, 7900, -40, 163900, 180)
    SetChrPos(0x5A, 9800, 40, 163900, 180)
    SetChrPos(0x5B, 11700, -40, 163900, 180)
    SetChrPos(0x5C, 13540, -20, 163900, 180)
    SetChrPos(0x5D, 4000, -40, 166050, 180)
    SetChrPos(0x5E, 5930, 0, 166050, 180)
    SetChrPos(0x5F, 7900, 30, 166050, 180)
    SetChrPos(0x60, 9800, 60, 166050, 180)
    SetChrPos(0x61, 11700, 10, 166050, 180)
    SetChrPos(0x62, 13540, -20, 166050, 180)
    SetChrPos(0x67, -11510, -30, 157450, 180)
    SetChrPos(0x68, -9600, -30, 157450, 180)
    SetChrPos(0x6D, -11510, -20, 159600, 180)
    SetChrPos(0x6E, -9600, -50, 159600, 180)
    SetChrPos(0x73, -11510, -10, 161750, 180)
    SetChrPos(0x74, -9600, -30, 161750, 180)
    SetChrPos(0x79, -11510, -40, 163900, 180)
    SetChrPos(0x7A, -9600, -20, 163900, 180)
    SetChrPos(0x63, -9600, -30, 168200, 180)
    SetChrPos(0x64, -7630, -40, 168200, 180)
    SetChrPos(0x65, -5660, 0, 168200, 180)
    SetChrPos(0x66, -3630, 30, 168200, 180)
    SetChrPos(0x69, -1730, 60, 168200, 180)
    SetChrPos(0x6A, 230, 10, 168200, 180)
    SetChrPos(0x6B, 2070, -20, 168200, 180)
    SetChrPos(0x6C, 4000, 30, 168200, 180)
    SetChrPos(0x6F, -9600, -30, 170350, 180)
    SetChrPos(0x70, -7630, -40, 170350, 180)
    SetChrPos(0x71, -5660, 0, 170350, 180)
    SetChrPos(0x72, -3630, 30, 170350, 180)
    SetChrPos(0x75, -1730, 60, 170350, 180)
    SetChrPos(0x76, 230, 10, 170350, 180)
    SetChrPos(0x77, 2070, -20, 170350, 180)
    SetChrPos(0x78, 4000, 30, 170350, 180)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    ClearChrFlags(0x4C, 0x80)
    ClearChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    ClearChrFlags(0x4F, 0x80)
    ClearChrFlags(0x50, 0x80)
    ClearChrFlags(0x51, 0x80)
    ClearChrFlags(0x52, 0x80)
    ClearChrFlags(0x53, 0x80)
    ClearChrFlags(0x54, 0x80)
    ClearChrFlags(0x55, 0x80)
    ClearChrFlags(0x56, 0x80)
    ClearChrFlags(0x57, 0x80)
    ClearChrFlags(0x58, 0x80)
    ClearChrFlags(0x59, 0x80)
    ClearChrFlags(0x5A, 0x80)
    ClearChrFlags(0x5B, 0x80)
    ClearChrFlags(0x5C, 0x80)
    ClearChrFlags(0x5D, 0x80)
    ClearChrFlags(0x5E, 0x80)
    ClearChrFlags(0x5F, 0x80)
    ClearChrFlags(0x60, 0x80)
    ClearChrFlags(0x61, 0x80)
    ClearChrFlags(0x62, 0x80)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    ClearChrFlags(0x6D, 0x80)
    ClearChrFlags(0x6E, 0x80)
    ClearChrFlags(0x6F, 0x80)
    ClearChrFlags(0x70, 0x80)
    ClearChrFlags(0x71, 0x80)
    ClearChrFlags(0x72, 0x80)
    ClearChrFlags(0x73, 0x80)
    ClearChrFlags(0x74, 0x80)
    ClearChrFlags(0x75, 0x80)
    ClearChrFlags(0x76, 0x80)
    ClearChrFlags(0x77, 0x80)
    ClearChrFlags(0x78, 0x80)
    ClearChrFlags(0x79, 0x80)
    ClearChrFlags(0x7A, 0x80)
    ClearChrFlags(0x7B, 0x80)
    ClearChrFlags(0x7C, 0x80)
    ClearChrFlags(0x7D, 0x80)
    ClearChrFlags(0x7E, 0x80)

    def lambda_2C94():
        OP_6D(-1410, 70, 152440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C94)

    def lambda_2CAC():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CAC)
    OP_8C(0xE, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #53
        0xE,
        "#885F#2P#3SMen, fall out!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #54
        0xE,
        (
            "#885F#2P#3SWe are withdrawing to Parm!\x01",
            "There, we will await new orders!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(800)
    SetMessageWindowPos(50, 90, -1, -1)
    SetChrName("Imperial Soldiers")

    AnonymousTalk(    #55
        "\x07\x00#5SYES, SIR!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-2140, 50, 142400, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(45000, 0)
    OP_6E(340, 0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x27, -7630, 0, 89450, 0)
    SetChrPos(0x28, -5660, -50, 89450, 0)
    SetChrPos(0x29, -3630, 0, 89450, 0)
    SetChrPos(0x2A, -1730, 90, 89450, 0)
    SetChrPos(0x2B, 230, -30, 89450, 0)
    SetChrPos(0x2C, 2070, -30, 89450, 0)
    SetChrPos(0x2D, -7630, 40, 91600, 0)
    SetChrPos(0x2E, -5660, 20, 91600, 0)
    SetChrPos(0x2F, -3630, -20, 91600, 0)
    SetChrPos(0x30, -1730, 50, 91600, 0)
    SetChrPos(0x31, 230, -20, 91600, 0)
    SetChrPos(0x32, 2070, -50, 91600, 0)
    SetChrPos(0x33, -7630, 30, 93750, 0)
    SetChrPos(0x34, -5660, 10, 93750, 0)
    SetChrPos(0x35, -3630, 20, 93750, 0)
    SetChrPos(0x36, -1730, 70, 93750, 0)
    SetChrPos(0x37, 230, -10, 93750, 0)
    SetChrPos(0x38, 2070, -30, 93750, 0)
    SetChrPos(0x39, -7630, -20, 95900, 0)
    SetChrPos(0x3A, -5660, -40, 95900, 0)
    SetChrPos(0x3B, -3630, -40, 95900, 0)
    SetChrPos(0x3C, -1730, 40, 95900, 0)
    SetChrPos(0x3D, 230, -40, 95900, 0)
    SetChrPos(0x3E, 2070, -20, 95900, 0)
    SetChrPos(0x3F, -7630, -40, 98050, 0)
    SetChrPos(0x40, -5660, 0, 98050, 0)
    SetChrPos(0x41, -3630, 30, 98050, 0)
    SetChrPos(0x42, -1730, 60, 98050, 0)
    SetChrPos(0x43, 230, 10, 98050, 0)
    SetChrPos(0x44, 2070, -20, 98050, 0)
    SetChrPos(0x45, 4000, 0, 89450, 0)
    SetChrPos(0x46, 5930, -50, 89450, 0)
    SetChrPos(0x47, 7900, 0, 89450, 0)
    SetChrPos(0x48, 9800, 90, 89450, 0)
    SetChrPos(0x49, 11700, -30, 89450, 0)
    SetChrPos(0x4A, 13540, -30, 89450, 0)
    SetChrPos(0x4B, 4000, 40, 91600, 0)
    SetChrPos(0x4C, 5930, 20, 91600, 0)
    SetChrPos(0x4D, 7900, -20, 91600, 0)
    SetChrPos(0x4E, 9800, 50, 91600, 0)
    SetChrPos(0x4F, 11700, -20, 91600, 0)
    SetChrPos(0x50, 13540, -50, 91600, 0)
    SetChrPos(0x51, 4000, 30, 93750, 0)
    SetChrPos(0x52, 5930, 10, 93750, 0)
    SetChrPos(0x53, 7900, 20, 93750, 0)
    SetChrPos(0x54, 9800, 70, 93750, 0)
    SetChrPos(0x55, 11700, -10, 93750, 0)
    SetChrPos(0x56, 13540, -30, 93750, 0)
    SetChrPos(0x57, 4000, -20, 95900, 0)
    SetChrPos(0x58, 5930, -40, 95900, 0)
    SetChrPos(0x59, 7900, -40, 95900, 0)
    SetChrPos(0x5A, 9800, 40, 95900, 0)
    SetChrPos(0x5B, 11700, -40, 95900, 0)
    SetChrPos(0x5C, 13540, -20, 95900, 0)
    SetChrPos(0x5D, 4000, -40, 98050, 0)
    SetChrPos(0x5E, 5930, 0, 98050, 0)
    SetChrPos(0x5F, 7900, 30, 98050, 0)
    SetChrPos(0x60, 9800, 60, 98050, 0)
    SetChrPos(0x61, 11700, 10, 98050, 0)
    SetChrPos(0x62, 13540, -20, 98050, 0)
    SetChrPos(0x63, -19030, 0, 89450, 0)
    SetChrPos(0x64, -17150, -50, 89450, 0)
    SetChrPos(0x65, -15270, 0, 89450, 0)
    SetChrPos(0x66, -13390, 90, 89450, 0)
    SetChrPos(0x67, -11510, -30, 89450, 0)
    SetChrPos(0x68, -9600, -30, 89450, 0)
    SetChrPos(0x69, -19030, 40, 91600, 0)
    SetChrPos(0x6A, -17150, 20, 91600, 0)
    SetChrPos(0x6B, -15270, -20, 91600, 0)
    SetChrPos(0x6C, -13390, 50, 91600, 0)
    SetChrPos(0x6D, -11510, -20, 91600, 0)
    SetChrPos(0x6E, -9600, -50, 91600, 0)
    SetChrPos(0x6F, -19030, 30, 93750, 0)
    SetChrPos(0x70, -17150, 10, 93750, 0)
    SetChrPos(0x71, -15270, 20, 93750, 0)
    SetChrPos(0x72, -13390, 70, 93750, 0)
    SetChrPos(0x73, -11510, -10, 93750, 0)
    SetChrPos(0x74, -9600, -30, 93750, 0)
    SetChrPos(0x75, -19030, -20, 95900, 0)
    SetChrPos(0x76, -17150, -40, 95900, 0)
    SetChrPos(0x77, -15270, -40, 95900, 0)
    SetChrPos(0x78, -13390, 40, 95900, 0)
    SetChrPos(0x79, -11510, -40, 95900, 0)
    SetChrPos(0x7A, -9600, -20, 95900, 0)
    SetChrPos(0x7B, -19030, -40, 98050, 0)
    SetChrPos(0x7C, -17150, 0, 98050, 0)
    SetChrPos(0x7D, -15270, 30, 98050, 0)
    SetChrPos(0x7E, -13390, 60, 98050, 0)
    SetChrChipByIndex(0x15, 9)
    SetChrChipByIndex(0x16, 9)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x16, 0)
    SetChrFlags(0x15, 0x200)
    SetChrFlags(0x16, 0x200)
    SetChrPos(0x15, -11510, 10, 98050, 0)
    SetChrPos(0x16, -9600, -20, 98050, 0)
    OP_8C(0x17, 180, 0)
    OP_8C(0x18, 180, 0)
    OP_8C(0x19, 180, 0)
    OP_8C(0x1A, 180, 0)
    OP_8C(0x1B, 180, 0)
    OP_8C(0x1C, 180, 0)
    OP_8C(0x1D, 180, 0)
    OP_8C(0x1E, 180, 0)
    OP_8C(0x1F, 180, 0)
    OP_8C(0x20, 180, 0)
    OP_8C(0x21, 180, 0)
    OP_8C(0x22, 180, 0)
    OP_8C(0x23, 180, 0)
    OP_8C(0x24, 180, 0)
    LoadEffect(0x0, "map\\\\mp109_00.eff")
    LoadEffect(0x1, "map\\\\onsen00.eff")
    PlayEffect(0x0, 0xFF, 0x17, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x17, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x18, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x18, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x19, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x19, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1A, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1A, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1B, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1B, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1C, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1C, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1D, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1D, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1E, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1E, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1F, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1F, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x20, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x20, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x21, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x21, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x22, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x22, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x23, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x23, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x24, 2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x24, -2000, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x19, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x19, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x22, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x22, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x24, 1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x24, -1050, 4000, 1800, 0, 30, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_6D(-2080, 50, 134590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(500, 0)
    SetChrChipByIndex(0x13, 13)
    SetChrChipByIndex(0x12, 14)
    SetChrChipByIndex(0x14, 15)
    OP_22(0x10F, 0x1, 0x64)
    OP_22(0x110, 0x1, 0x5F)
    OP_43(0x17, 0x3, 0x1, 0xE)
    WaitChrThread(0x17, 0x3)
    OP_43(0x27, 0x3, 0x1, 0xF)
    OP_43(0x45, 0x3, 0x1, 0x10)
    OP_43(0x63, 0x3, 0x1, 0x11)
    WaitChrThread(0x27, 0x3)
    WaitChrThread(0x45, 0x3)
    WaitChrThread(0x63, 0x3)
    FadeToBright(1000, 0)
    OP_6D(-1520, 20, 117830, 6000)
    Fade(1000)
    OP_6D(-920, 20, 89290, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(364, 0)
    SetChrPos(0xD, -1950, 40, 88980, 0)
    SetChrPos(0x10, -600, 70, 88900, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x10, 0x80)
    OP_0D()
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)
    SetChrFlags(0x41, 0x80)
    SetChrFlags(0x42, 0x80)
    SetChrFlags(0x43, 0x80)
    SetChrFlags(0x44, 0x80)
    SetChrFlags(0x45, 0x80)
    SetChrFlags(0x46, 0x80)
    SetChrFlags(0x47, 0x80)
    SetChrFlags(0x48, 0x80)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4B, 0x80)
    SetChrFlags(0x4C, 0x80)
    SetChrFlags(0x4D, 0x80)
    SetChrFlags(0x4E, 0x80)
    SetChrFlags(0x4F, 0x80)
    SetChrFlags(0x50, 0x80)
    SetChrFlags(0x51, 0x80)
    SetChrFlags(0x52, 0x80)
    SetChrFlags(0x53, 0x80)
    SetChrFlags(0x54, 0x80)
    SetChrFlags(0x55, 0x80)
    SetChrFlags(0x56, 0x80)
    SetChrFlags(0x57, 0x80)
    SetChrFlags(0x58, 0x80)
    SetChrFlags(0x59, 0x80)
    SetChrFlags(0x5A, 0x80)
    SetChrFlags(0x5B, 0x80)
    SetChrFlags(0x5C, 0x80)
    SetChrFlags(0x5D, 0x80)
    SetChrFlags(0x5E, 0x80)
    SetChrFlags(0x5F, 0x80)
    SetChrFlags(0x60, 0x80)
    SetChrFlags(0x61, 0x80)
    SetChrFlags(0x62, 0x80)
    SetChrFlags(0x63, 0x80)
    SetChrFlags(0x64, 0x80)
    SetChrFlags(0x65, 0x80)
    SetChrFlags(0x66, 0x80)
    SetChrFlags(0x67, 0x80)
    SetChrFlags(0x68, 0x80)
    SetChrFlags(0x69, 0x80)
    SetChrFlags(0x6A, 0x80)
    SetChrFlags(0x6B, 0x80)
    SetChrFlags(0x6C, 0x80)
    SetChrFlags(0x6D, 0x80)
    SetChrFlags(0x6E, 0x80)
    SetChrFlags(0x6F, 0x80)
    SetChrFlags(0x70, 0x80)
    SetChrFlags(0x71, 0x80)
    SetChrFlags(0x72, 0x80)
    SetChrFlags(0x73, 0x80)
    SetChrFlags(0x74, 0x80)
    SetChrFlags(0x75, 0x80)
    SetChrFlags(0x76, 0x80)
    SetChrFlags(0x77, 0x80)
    SetChrFlags(0x78, 0x80)
    SetChrFlags(0x79, 0x80)
    SetChrFlags(0x7A, 0x80)
    SetChrFlags(0x7B, 0x80)
    SetChrFlags(0x7C, 0x80)
    SetChrFlags(0x7D, 0x80)
    SetChrFlags(0x7E, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_71(0x3, 0x0)
    OP_71(0x4, 0x0)
    OP_71(0x5, 0x0)
    OP_71(0x6, 0x0)
    OP_71(0x7, 0x0)
    OP_71(0x8, 0x0)
    OP_71(0x9, 0x0)
    OP_71(0xA, 0x0)
    OP_71(0xB, 0x0)
    OP_71(0xC, 0x0)
    OP_71(0xD, 0x0)
    OP_71(0xE, 0x0)
    OP_71(0xF, 0x0)
    OP_71(0x10, 0x0)
    OP_43(0xD, 0x3, 0x1, 0x12)
    Sleep(500)
    OP_DC()

    ChrTalk(    #56
        0xD,
        (
            "#890F#6PAnd so, we managed to buy ourselves\x01",
            "a little bit of time, at least.\x02\x03",

            "#893FReally, though! No one trusts me, it seems.\x01",
            "My lamentations truly ARE ceaseless!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #57
        0x10,
        (
            "#276F#4POf course they don't, you nitwit.\x02\x03",

            "#272FEven I didn't think you had something\x01",
            "like THIS in you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)
    Sleep(300)

    ChrTalk(    #58
        0xD,
        (
            "#890F#6PAs they say--if you're going to play\x01",
            "your cards, throw in all your chips!\x02\x03",

            "#891FBesides, you certainly did a good\x01",
            "job in arranging all the pieces.\x02\x03",

            "You could say we are partners in crime!\x01",
            "Confederates of love, bees of a flower\x01",
            "who have shared of the sweetest honey!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        "#274F#4PI AM armed, Olivert.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1POlivier!\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x10, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(-2560, 70, 87160, 0)
    OP_67(0, 5080, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(225000, 0)
    OP_6E(364, 0)

    def lambda_464B():
        OP_6D(-3120, -20, 84880, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_464B)

    def lambda_4663():
        OP_6E(381, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4663)
    OP_43(0x101, 0x1, 0x1, 0x6)
    OP_43(0xC, 0x1, 0x1, 0x7)
    OP_43(0x102, 0x1, 0x1, 0x8)
    OP_43(0xA, 0x1, 0x1, 0xB)
    OP_43(0x8, 0x1, 0x1, 0x9)
    OP_43(0x9, 0x1, 0x1, 0xA)
    OP_43(0xB, 0x1, 0x1, 0xC)
    OP_43(0xF, 0x1, 0x1, 0xD)
    OP_8C(0xD, 180, 400)
    OP_8C(0x10, 180, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #61
        0xD,
        "#891F#2PEstelle! Brilliantly done.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1009F#6PBrilliantly done, my ENTIRE butt!\x02\x03",

            "Would you PLEASE explain what\x01",
            "in the hell is going on?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xD,
        (
            "#890F#2PWhy, it's exactly as it looks.\x02\x03",

            "#891FThere was something rotten in the\x01",
            "state of Erebonia.\x02\x03",

            "I simply dragged it up onto the stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1019F#6P'The stage.' And the rest of us couldn't\x01",
            "get a peek at the script?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xD,
        (
            "#894F#2PAs they truly say--if you wish to deceive\x01",
            "your foes, deceive your friends.\x02\x03",

            "#890FHaving the Arseille show up after you\x01",
            "negotiate us into a corner...\x02\x03",

            "That was the plan Cassius Bright\x01",
            "and I came up with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1007F#6PDad and Olivier...\x01",
            "I shoulda known...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#1040F#6POnce Dad showed up, I thought\x01",
            "that might be it.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF, 0x1)
    ClearChrFlags(0x11, 0x20)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, -17000, -130, 84330, 90)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #68
        0x11,
        "Man's Voice",
        "#3PThat was the idea, at least.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4AEA():
        OP_6D(-3420, -30, 84750, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4AEA)

    def lambda_4B02():
        OP_6B(2590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4B02)

    def lambda_4B12():
        OP_6C(224000, 4000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_4B12)

    def lambda_4B22():

        label("loc_4B22")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4B22")

    QueueWorkItem2(0xD, 1, lambda_4B22)

    def lambda_4B33():

        label("loc_4B33")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4B33")

    QueueWorkItem2(0x10, 1, lambda_4B33)
    Sleep(50)

    def lambda_4B49():

        label("loc_4B49")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4B49")

    QueueWorkItem2(0xC, 1, lambda_4B49)

    def lambda_4B5A():

        label("loc_4B5A")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4B5A")

    QueueWorkItem2(0x101, 1, lambda_4B5A)
    Sleep(50)

    def lambda_4B70():

        label("loc_4B70")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4B70")

    QueueWorkItem2(0x102, 1, lambda_4B70)

    def lambda_4B81():

        label("loc_4B81")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4B81")

    QueueWorkItem2(0x9, 1, lambda_4B81)
    Sleep(50)

    def lambda_4B97():

        label("loc_4B97")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4B97")

    QueueWorkItem2(0x8, 1, lambda_4B97)

    def lambda_4BA8():

        label("loc_4BA8")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4BA8")

    QueueWorkItem2(0xA, 1, lambda_4BA8)
    Sleep(50)

    def lambda_4BBE():

        label("loc_4BBE")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4BBE")

    QueueWorkItem2(0xB, 1, lambda_4BBE)

    def lambda_4BCF():

        label("loc_4BCF")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4BCF")

    QueueWorkItem2(0xF, 1, lambda_4BCF)
    OP_8E(0x11, 0xFFFFE9B2, 0xFFFFFFE2, 0x14C4E, 0xBB8, 0x0)
    OP_8C(0x11, 90, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #69
        0x101,
        "#1009F#6PAnd here comes deceitful jerk number two!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "#1123F#4PThat's a little cruel, don't you think?\x02\x03",

            "#1120FI was listening in by phone.\x01",
            "You handled those negotiations expertly.\x02\x03",

            "Thanks to you, the arrival of the Arseille\x01",
            "had all the impact it needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1004F#6PListening in by... What?\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)
    OP_8C(0x8, 0, 400)
    Sleep(300)

    ChrTalk(    #72
        0x8,
        "#023F#6POf course! That artifact of yours!\x02",
    )

    CloseMessageWindow()
    OP_44(0xD, 0x1)
    OP_8C(0xD, 180, 400)
    Sleep(300)

    ChrTalk(    #73
        0xD,
        (
            "#891F#2PEr, ah, my dear Schera!\x01",
            "No more of that, please!\x02\x03",

            "It would be a little problematic\x01",
            "if HE heard about--\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, -22110, -290, 84920, 90)
    SetChrPos(0x12, -21810, -280, 83150, 90)
    SetChrPos(0x13, -23280, -330, 83160, 90)

    NpcTalk(    #74
        0x14,
        "Man's Voice",
        "#3PLittle too late on that score, Prince.\x02",
    )

    CloseMessageWindow()

    def lambda_4E5E():
        OP_6D(-5560, 20, 84410, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4E5E)

    def lambda_4E76():
        OP_67(0, 4530, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E76)

    def lambda_4E8E():
        OP_6E(380, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4E8E)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    def lambda_4EAD():

        label("loc_4EAD")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4EAD")

    QueueWorkItem2(0xC, 1, lambda_4EAD)

    def lambda_4EBE():

        label("loc_4EBE")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4EBE")

    QueueWorkItem2(0x101, 1, lambda_4EBE)

    def lambda_4ECF():

        label("loc_4ECF")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4ECF")

    QueueWorkItem2(0x102, 1, lambda_4ECF)
    Sleep(100)

    def lambda_4EE5():

        label("loc_4EE5")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4EE5")

    QueueWorkItem2(0x9, 1, lambda_4EE5)

    def lambda_4EF6():

        label("loc_4EF6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4EF6")

    QueueWorkItem2(0x8, 1, lambda_4EF6)
    Sleep(100)

    def lambda_4F0C():

        label("loc_4F0C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4F0C")

    QueueWorkItem2(0xA, 1, lambda_4F0C)

    def lambda_4F1D():

        label("loc_4F1D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4F1D")

    QueueWorkItem2(0xB, 1, lambda_4F1D)

    def lambda_4F2E():

        label("loc_4F2E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4F2E")

    QueueWorkItem2(0xF, 1, lambda_4F2E)
    Sleep(100)

    def lambda_4F44():

        label("loc_4F44")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4F44")

    QueueWorkItem2(0xD, 1, lambda_4F44)

    def lambda_4F55():

        label("loc_4F55")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_4F55")

    QueueWorkItem2(0x10, 1, lambda_4F55)

    def lambda_4F66():
        OP_8E(0xFE, 0xFFFFE75A, 0xFFFFFFF6, 0x14FF0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4F66)
    Sleep(400)

    def lambda_4F86():
        OP_8E(0xFE, 0xFFFFE778, 0xFFFFFFF6, 0x146AE, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4F86)
    Sleep(400)

    def lambda_4FA6():
        OP_8E(0xFE, 0xFFFFE188, 0xFFFFFFF6, 0x147EE, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4FA6)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x102, 0x1)

    def lambda_4FD3():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4FD3)
    Sleep(50)

    def lambda_4FE6():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4FE6)

    ChrTalk(    #75
        0x101,
        "#1004F#5PKevin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        "#560F#5PKevin's here too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xC,
        "#1168F#5PAnd Julia, as well...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #78
        0x13,
        (
            "#176FYour Highness... I heard about\x01",
            "the attack on the capital.\x02\x03",

            "#175FI am very glad to see you are safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xC,
        (
            "#1169F#5PI'm sorry, Julia.\x01",
            "I can only imagine how worried\x01",
            "you must have been.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x12,
        (
            "#101F#4PWellll, part of it's my fault. If I'd finished\x01",
            "the Arseille's upgrades we could have\x01",
            "come by to help out ourselves.\x02\x03",

            "Unfortunately, Zero Field reinforcing the\x01",
            "most advanced airship in the world took\x01",
            "a while, if you can believe it.\x02\x03",

            "#100FStill! Glad to see everyone safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "#055F#1PYeah, hang on!\x02\x03",

            "How IS the Arseille flying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "#560F#5PYou made a Zero Field Generator big\x01",
            "enough for the entire ship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x12,
        (
            "#101F#4PYes, indeed!\x02\x03",

            "#100FThe ones I gave you were prototypes I'd\x01",
            "whipped up to help design a large-scale\x01",
            "version.\x02\x03",

            "I've been locked up in the Arseille ever\x01",
            "since you left, and now it's finally ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        "#1040F#6PI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1019F#5PSo, in other words, every last bit\x01",
            "of this was set up by Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x11,
        (
            "#1123F#4PCome now, don't say it like I'm a criminal!\x02\x03",

            "#1120FI simply did what I could to\x01",
            "make it easy for you to act.\x02\x03",

            "You did this because you wanted to, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1015F#5PWell...TECHNICALLY, I guess, but...\x02\x03",

            "#1004FOh, I don't quite get why you're here,\x01",
            "though, Kevin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x14,
        (
            "#1062F#4PAh, right. While I was at the cathedral,\x01",
            "word came in from the Gralsritter higher\x01",
            "ups. They've been hittin' the books.\x02\x03",

            "I think I've got a good picture on what\x01",
            "kinda thing the Aureole is, 'n how to\x01",
            "end this mess.\x02\x03",

            "#1061FAaaand once I told Cassius about this,\x01",
            "I got hog-tied and brought out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1020F#5PWhoa, what?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        "#1042F#6PWhat the Aureole...is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x14,
        (
            "#1065F#4PYeah. So...\x02\x03",

            "#1063FFirst of all, the Aureole isn't that\x01",
            "floating city itself, really.\x02\x03",

            "We think it's an artifact within the city\x01",
            "that provides the whole thing with orbal\x01",
            "power and helps control the flow of it.\x02\x03",

            "The Gospels are basically like\x01",
            "distribution...thingies for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        "#1163F#5PAn ancient power source for a city...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "#065F#5PBut then, why is it causing all\x01",
            "our orbments to shut down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x14,
        (
            "#1067F#4PNow we're gettin' into guesswork, but...\x01",
            "a couple of reeeally old legends talk about the\x01",
            "Aureole 'striking down threats to the chosen.'\x02\x03",

            "#1063FMeaning, all our modern orbments are being\x01",
            "seen by it as 'threats' to the 'chosen.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        (
            "#074F#6PDisabling any possible threat in\x01",
            "its area of influence...\x02\x03",

            "#072FIt's a defense mechanism,\x01",
            "essentially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x12,
        (
            "#104F#4PIt seems extremely likely.\x02\x03",

            "#102FAnd, really, this gives us a ray of hope.\x02\x03",

            "Doing something about the entire city\x01",
            "would be difficult at best due to its\x01",
            "sheer size...\x02\x03",

            "...but if we can find the actual Aureole\x01",
            "somewhere within the city, we may be\x01",
            "able to find a way to deal with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#1040F#6PI see... That is an idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1006F#5PThat does sound like a plan, at least.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xD,
        (
            "#891F#5PYes, it seems as though our\x01",
            "final goal is well set for us.\x02\x03",

            "#890FWe should board the Arseille and make our\x01",
            "way to the flying city with all haste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x11,
        (
            "#1125F#4PThe decision to use the Arseille\x01",
            "must come from the royal family.\x02\x03",

            "#1122FPrincess...shall we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xC,
        (
            "#1167F#5PYou don't need to ask.\x02\x03",

            "#1162FCaptain Schwarz!\x01",
            "Prepare the Arseille for launch.\x02\x03",

            "We are heading for the flying\x01",
            "city above Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x13,
        "#171FAt once, Your Highness!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 270, 400)

    def lambda_5CBD():
        OP_8E(0xFE, 0xFFFFA510, 0xFFFFFEB6, 0x144D8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5CBD)

    def lambda_5CD8():
        OP_6D(-3610, -30, 83240, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5CD8)

    def lambda_5CF0():
        OP_67(0, 4980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CF0)

    def lambda_5D08():
        OP_6B(2450, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D08)

    def lambda_5D18():
        OP_6C(224000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5D18)

    def lambda_5D28():
        OP_6E(354, 2000)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_5D28)
    OP_44(0xC, 0x1)
    OP_8C(0xC, 215, 400)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #103
        0xC,
        "#1167F#5PAnd my bracer friends...\x02",
    )

    CloseMessageWindow()

    def lambda_5D74():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D74)

    def lambda_5D82():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D82)
    Sleep(50)

    def lambda_5D95():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5D95)

    def lambda_5DA3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DA3)
    Sleep(50)

    def lambda_5DB6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5DB6)

    def lambda_5DC4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5DC4)

    def lambda_5DD2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5DD2)
    Sleep(50)

    def lambda_5DE5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5DE5)

    def lambda_5DF3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5DF3)
    Sleep(400)

    ChrTalk(    #104
        0xC,
        (
            "#1162F#5PPlease, everyone, lend your aid\x01",
            "to Liberl in our hour of need.\x02\x03",

            "This mission will likely be\x01",
            "the last one of this crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "#027F#6PWell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "#051F#1PHeh. Sayin' that like it's even\x01",
            "a question if we'll go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xB,
        (
            "#071F#6PThis is something we should\x01",
            "leave up to our leader.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #108
        0x101,
        "#1015F#2PEr, leader?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #109
        0x9,
        (
            "#053F#1PUh, Estelle.\x02\x03",

            "#555FWe mean you of course.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F85():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F85)
    Sleep(50)

    def lambda_5F98():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5F98)
    Sleep(50)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #110
        0x101,
        "#1004F#2PWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#021F#6PWhy so shocked, Estelle?\x02\x03",

            "#524FWe all do have our own stake\x01",
            "in this, yes...\x02\x03",

            "But, one way or another, we've\x01",
            "just been tagging along on this\x01",
            "wild ride of yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xB,
        (
            "#070F#6PSo in that sense, Estelle...\x02\x03",

            "...you're definitely our leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1013F#2PEr, well I, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x11,
        "#1123F#4PHmm... Still not quite ready for it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#1035F#6PNo...she is.\x02\x03",

            "#1040FNo matter how grim it gets,\x01",
            "Estelle never loses hope.\x02\x03",

            "That light is always there to\x01",
            "guide me--to guide us.\x02\x03",

            "#1049FThat's why only Estelle could\x01",
            "ever be our leader.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #116
        0x101,
        "#1013F#2PJOSHUA! NOT HELPING!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        (
            "#061F#5PHeehee... Estelle, your face is\x01",
            "red as a beet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1013F#2PGhhhghghghhcute...\x02\x03",

            "#1022FOKAY, OKAY, I get it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    Sleep(500)

    ChrTalk(    #119
        0x101,
        (
            "#1006F#2PKloe...the guild accepts your mission!\x02\x03",

            "We'll find the Aureole on the\x01",
            "flying city and save Liberl!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #120
        0xC,
        "Kloe",
        "#1168FHaha... Thank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x11,
        (
            "#1120F#4PGood, that's finally settled.\x02\x03",

            "Now I can get back to headquarters.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6381():
        OP_6D(-4960, 10, 83700, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6381)

    def lambda_6399():

        label("loc_6399")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6399")

    QueueWorkItem2(0x101, 1, lambda_6399)

    def lambda_63AA():

        label("loc_63AA")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_63AA")

    QueueWorkItem2(0x102, 1, lambda_63AA)
    Sleep(50)

    def lambda_63C0():

        label("loc_63C0")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_63C0")

    QueueWorkItem2(0xC, 1, lambda_63C0)

    def lambda_63D1():

        label("loc_63D1")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_63D1")

    QueueWorkItem2(0x9, 1, lambda_63D1)

    def lambda_63E2():

        label("loc_63E2")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_63E2")

    QueueWorkItem2(0x8, 1, lambda_63E2)
    Sleep(50)

    def lambda_63F8():

        label("loc_63F8")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_63F8")

    QueueWorkItem2(0xB, 1, lambda_63F8)

    def lambda_6409():

        label("loc_6409")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6409")

    QueueWorkItem2(0xA, 1, lambda_6409)
    Sleep(50)

    def lambda_641F():

        label("loc_641F")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_641F")

    QueueWorkItem2(0xB, 1, lambda_641F)

    def lambda_6430():

        label("loc_6430")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6430")

    QueueWorkItem2(0xF, 1, lambda_6430)
    Sleep(50)

    def lambda_6446():

        label("loc_6446")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6446")

    QueueWorkItem2(0xD, 1, lambda_6446)

    def lambda_6457():

        label("loc_6457")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_6457")

    QueueWorkItem2(0x10, 1, lambda_6457)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #122
        0x101,
        "#1025F#5PDad...you're not coming with us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        (
            "#1125F#4PI'm afraid I can't.\x02\x03",

            "#1122FThey may have retreated for now, and I trust\x01",
            "Zechs to keep his word, but we can't ignore\x01",
            "the larger Erebonian threat.\x02\x03",

            "It's not just Haken Gate. They could use\x01",
            "non-orbal-powered vessels to invade by sea.\x02\x03",

            "I also wouldn't be surprised if the society\x01",
            "attempts another raid on Grancel.\x02\x03",

            "I can't leave the Royal Army\x01",
            "with all of this going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1012F#5PYeah... I get it.\x02\x03",

            "#1017FI'll do my best...\x02\x03",

            "...with Joshua...with everyone!\x02\x03",

            "So, Dad...try not to kill yourself\x01",
            "with work, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x11,
        (
            "#1120F#4PHeh. It will be a struggle!\x01",
            "But don't worry.\x02\x03",

            "#1125FAnd, Joshua...let me give this to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#1044F#6PHm?\x02",
    )

    CloseMessageWindow()

    def lambda_6724():
        OP_8F(0xFE, 0xFFFFED18, 0xFFFFFFF6, 0x14B5E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_6724)
    Sleep(300)
    OP_44(0x102, 0x1)
    OP_8F(0x102, 0xFFFFF038, 0xFFFFFFF6, 0x14A3C, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x2)
    Fade(250)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 16)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x11, 1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #127
        "\x07\x05Cassius handed a letter to Joshua.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(100)
    Fade(250)
    ClearChrFlags(0x11, 0x2)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 11)
    OP_0D()
    Sleep(200)

    ChrTalk(    #128
        0x102,
        "#1044F#6PA letter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x11,
        (
            "#1125F#4PCall it a father's heart.\x02\x03",

            "#1120FIt's between men, so it might\x01",
            "be a little shocking for Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1019F#5PGentle reminder that I'm right\x01",
            "here and still have my staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x102,
        "#1040F#6PI'll read it when I have time, Dad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x11,
        "#1120F#4PPlease do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1007F#5PFor the love of... I seriously do not\x01",
            "get 'guy stuff' like this.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6961():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6961)
    Sleep(500)

    ChrTalk(    #134
        0x11,
        (
            "#1123F#4PDon't be so harsh, Estelle.\x02\x03",

            "#1120FI'm taking some time off\x01",
            "once this is over.\x02\x03",

            "I intend to spend a lot of\x01",
            "time at home once I can.\x02\x03",

            "#1121FEstelle...make sure we can all share\x01",
            "some omelet rice then, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1004F#5PAh...\x02\x03",

            "#1017FYeah, you bet!\x02",
        )
    )

    CloseMessageWindow()
    OP_DB()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0x35, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x3A, 0x80)
    SetChrFlags(0x3B, 0x80)
    SetChrFlags(0x3C, 0x80)
    SetChrFlags(0x3D, 0x80)
    SetChrFlags(0x3E, 0x80)
    SetChrFlags(0x3F, 0x80)
    SetChrFlags(0x40, 0x80)
    SetChrFlags(0x41, 0x80)
    SetChrFlags(0x42, 0x80)
    SetChrFlags(0x43, 0x80)
    SetChrFlags(0x44, 0x80)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_6D(-31630, -180, 59850, 0)
    OP_67(0, 10310, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(156000, 0)
    OP_6E(628, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x125, 0x0, 0x64)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x96)

    def lambda_6C15():
        OP_6D(-26030, 2970, 49440, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6C15)

    def lambda_6C2D():
        OP_67(0, 9640, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C2D)

    def lambda_6C45():
        OP_6E(600, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C45)

    def lambda_6C55():
        OP_6C(138000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6C55)

    def lambda_6C65():
        OP_6B(6000, 10000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6C65)
    OP_43(0x25, 0x0, 0x1, 0x3)
    PlayEffect(0x0, 0x0, 0xFF, -39070, -150, 58410, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_73(0x2)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 150)
    OP_70(0x2, 0x14A)
    Sleep(1500)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x11, 0x0, 0x1)
    Sleep(180)
    OP_74(0x11, 0x0, 0x2)
    Sleep(170)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x11, 0x0, 0x3)
    Sleep(180)
    OP_74(0x11, 0x0, 0x4)
    Sleep(170)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0x11, 0x0, 0x5)
    Sleep(180)
    OP_74(0x11, 0x0, 0x6)
    Sleep(170)
    OP_74(0x11, 0x0, 0x7)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x3C)
    OP_6F(0x2, 330)
    OP_70(0x2, 0x1AE)

    def lambda_6D57():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_6D57)

    def lambda_6D65():
        OP_8C(0xFE, 180, 10)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_6D65)
    Sleep(300)

    def lambda_6D78():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_6D78)

    def lambda_6D86():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_6D86)
    Sleep(200)

    def lambda_6D99():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_6D99)

    def lambda_6DA7():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_6DA7)
    Sleep(100)

    def lambda_6DBA():
        OP_8C(0xFE, 180, 40)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_6DBA)

    def lambda_6DC8():
        OP_8C(0xFE, 180, 40)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_6DC8)
    Sleep(1500)

    def lambda_6DDB():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_6DDB)

    def lambda_6DE9():
        OP_8C(0xFE, 180, 30)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_6DE9)
    Sleep(500)

    def lambda_6DFC():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_6DFC)

    def lambda_6E0A():
        OP_8C(0xFE, 180, 20)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_6E0A)
    WaitChrThread(0x25, 0x0)
    WaitChrThread(0x25, 0x2)
    WaitChrThread(0x26, 0x2)
    OP_82(0x0, 0x2)
    OP_23(0xCC)
    Sleep(1500)

    def lambda_6E32():
        OP_6D(-35800, 0, 22420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E32)

    def lambda_6E4A():
        OP_67(0, 6500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E4A)

    def lambda_6E62():
        OP_6E(469, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E62)

    def lambda_6E72():
        OP_6C(174000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6E72)

    def lambda_6E82():
        OP_6B(8000, 2000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6E82)

    def lambda_6E92():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6E92)

    def lambda_6EAD():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6EAD)
    Sleep(50)

    def lambda_6ECD():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6ECD)

    def lambda_6EE8():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6EE8)
    Sleep(50)

    def lambda_6F08():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6F08)

    def lambda_6F23():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6F23)
    Sleep(50)

    def lambda_6F43():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6F43)

    def lambda_6F5E():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6F5E)
    Sleep(50)

    def lambda_6F7E():
        OP_8F(0xFE, 0xFFFF4A20, 0xC350, 0xFFFA87F6, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6F7E)

    def lambda_6F99():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x38A4, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6F99)
    Sleep(50)

    def lambda_6FB9():
        OP_8F(0xFE, 0xFFFF4A20, 0xEA60, 0xFFFA87F6, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6FB9)

    def lambda_6FD4():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x5014, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_6FD4)
    Sleep(50)
    OP_24(0x125, 0x5A)
    OP_24(0x77, 0x5A)

    def lambda_6FFC():
        OP_8F(0xFE, 0xFFFF4A20, 0x11170, 0xFFFA87F6, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_6FFC)

    def lambda_7017():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x6F54, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_7017)
    Sleep(50)

    def lambda_7037():
        OP_8F(0xFE, 0xFFFF4A20, 0x13880, 0xFFFA87F6, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_7037)

    def lambda_7052():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_7052)
    Sleep(50)

    def lambda_7072():
        OP_8F(0xFE, 0xFFFF4A20, 0x15F90, 0xFFFA87F6, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_7072)

    def lambda_708D():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_708D)
    Sleep(50)

    def lambda_70AD():
        OP_8F(0xFE, 0xFFFF4A20, 0x186A0, 0xFFFA87F6, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_70AD)

    def lambda_70C8():
        OP_8F(0xFE, 0xFFFF4A20, 0x1388, 0xFFFA87F6, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_70C8)
    Sleep(150)
    OP_24(0x125, 0x50)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x125, 0x46)
    OP_24(0x77, 0x46)
    Sleep(300)
    OP_24(0x125, 0x3C)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x125, 0x32)
    OP_24(0x77, 0x32)
    FadeToDark(1000, 0, -1)
    Sleep(300)
    OP_24(0x125, 0x28)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x125, 0x1E)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_24(0x125, 0x14)
    OP_24(0x77, 0x14)
    Sleep(300)
    OP_23(0x125)
    OP_23(0x77)
    OP_0D()
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_AC end

    def Function_3_715C(): pass

    label("Function_3_715C")

    Sleep(1500)

    def lambda_7167():
        OP_8F(0xFE, 0xFFFF63C0, 0x1388, 0xFE38, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_7167)

    def lambda_7182():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_7182)
    Sleep(700)

    def lambda_71A2():
        OP_8F(0xFE, 0xFFFF63C0, 0x1388, 0xFE38, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_71A2)

    def lambda_71BD():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_71BD)
    Sleep(500)

    def lambda_71DD():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_71DD)
    Sleep(300)

    def lambda_71FD():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_71FD)
    Sleep(1000)

    def lambda_721D():
        OP_8F(0xFE, 0xFFFF63C0, 0x4E20, 0xFE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_721D)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0x26, 0x1)
    Return()

    # Function_3_715C end

    def Function_4_723D(): pass

    label("Function_4_723D")

    OP_72(0x2, 0x20)
    OP_73(0x2)
    OP_6F(0x2, 430)
    OP_70(0x2, 0x258)
    Sleep(1000)
    OP_75(0xB, 0x0, 0x2)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(240)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(240)
    OP_22(0xDD, 0x0, 0x64)
    Sleep(240)
    OP_73(0x2)
    OP_6F(0x2, 600)
    OP_70(0x2, 0x320)
    OP_73(0x2)
    Return()

    # Function_4_723D end

    def Function_5_7292(): pass

    label("Function_5_7292")

    Sleep(2600)
    OP_75(0xB, 0x0, 0x2)
    OP_74(0x11, 0x0, 0x6)
    Sleep(150)
    OP_74(0x11, 0x0, 0x5)
    Sleep(150)
    OP_74(0x11, 0x0, 0x4)
    Sleep(150)
    OP_74(0x11, 0x0, 0x3)
    Sleep(150)
    OP_74(0x11, 0x0, 0x2)
    Sleep(150)
    OP_74(0x11, 0x0, 0x1)
    Sleep(150)
    OP_74(0x11, 0x0, 0x0)
    Return()

    # Function_5_7292 end

    def Function_6_72FC(): pass

    label("Function_6_72FC")

    SetChrPos(0xFE, -2790, 20, 65540, 0)
    OP_8E(0xFE, 0xFFFFF51A, 0x14, 0x14E1A, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_72FC end

    def Function_7_7329(): pass

    label("Function_7_7329")

    SetChrChipByIndex(0xFE, 17)
    SetChrPos(0xFE, -1370, 0, 65129, 0)
    OP_8E(0xFE, 0xFFFFFAA6, 0x28, 0x14E6A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_7_7329 end

    def Function_8_7365(): pass

    label("Function_8_7365")

    SetChrPos(0xFE, -2950, 20, 63670, 0)
    OP_8E(0xFE, 0xFFFFF47A, 0xFFFFFFC4, 0x148CA, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_8_7365 end

    def Function_9_7397(): pass

    label("Function_9_7397")

    SetChrChipByIndex(0xFE, 18)
    SetChrPos(0xFE, -1710, 30, 62720, 0)
    OP_8E(0xFE, 0xFFFFF952, 0x1E, 0x14834, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_9_7397 end

    def Function_10_73D3(): pass

    label("Function_10_73D3")

    SetChrChipByIndex(0xFE, 19)
    SetChrPos(0xFE, -520, 30, 61080, 0)
    OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFFF6, 0x1465E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_73D3 end

    def Function_11_740F(): pass

    label("Function_11_740F")

    SetChrChipByIndex(0xFE, 20)
    SetChrPos(0xFE, -860, 10, 62910, 0)
    OP_8E(0xFE, 0xFFFFFCA4, 0x0, 0x14B22, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_740F end

    def Function_12_744B(): pass

    label("Function_12_744B")

    SetChrChipByIndex(0xFE, 21)
    SetChrPos(0xFE, -2670, 30, 60510, 0)
    OP_8E(0xFE, 0xFFFFF592, 0x1E, 0x142E4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_744B end

    def Function_13_7487(): pass

    label("Function_13_7487")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -1890, 40, 61000, 0)
    OP_8E(0xFE, 0xFFFFF89E, 0x28, 0x13D4E, 0xBB8, 0x0)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_7487 end

    def Function_14_74BE(): pass

    label("Function_14_74BE")


    def lambda_74C4():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_74C4)
    Sleep(160)

    def lambda_74E4():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_74E4)

    def lambda_74FF():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_74FF)
    Sleep(200)

    def lambda_751F():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_751F)

    def lambda_753A():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_753A)
    Sleep(180)

    def lambda_755A():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_755A)

    def lambda_7575():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_7575)
    Sleep(230)

    def lambda_7595():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_7595)

    def lambda_75B0():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_75B0)
    Sleep(150)

    def lambda_75D0():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_75D0)

    def lambda_75EB():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_75EB)
    Sleep(190)

    def lambda_760B():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_760B)

    def lambda_7626():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7626)
    Sleep(220)

    def lambda_7646():
        OP_91(0xFE, 0x0, 0x0, 0xABE0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7646)
    Return()

    # Function_14_74BE end

    def Function_15_765C(): pass

    label("Function_15_765C")


    def lambda_7662():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3F, 1, lambda_7662)

    def lambda_767D():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x41, 1, lambda_767D)
    Sleep(100)

    def lambda_769D():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x40, 1, lambda_769D)
    Sleep(80)

    def lambda_76BD():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_76BD)

    def lambda_76D8():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_76D8)
    Sleep(70)

    def lambda_76F8():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_76F8)
    Sleep(30)

    def lambda_7718():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_7718)
    Sleep(90)

    def lambda_7738():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_7738)

    def lambda_7753():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_7753)

    def lambda_776E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_776E)
    Sleep(40)

    def lambda_778E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_778E)

    def lambda_77A9():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_77A9)
    Sleep(30)

    def lambda_77C9():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_77C9)

    def lambda_77E4():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_77E4)
    Sleep(70)

    def lambda_7804():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_7804)

    def lambda_781F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_781F)
    Sleep(40)

    def lambda_783F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_783F)

    def lambda_785A():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_785A)

    def lambda_7875():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_7875)
    Sleep(50)

    def lambda_7895():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_7895)

    def lambda_78B0():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_78B0)
    Sleep(30)

    def lambda_78D0():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_78D0)
    Sleep(100)

    def lambda_78F0():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_78F0)

    def lambda_790B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_790B)
    Sleep(30)

    def lambda_792B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_792B)

    def lambda_7946():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7946)
    Sleep(60)

    def lambda_7966():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_7966)

    def lambda_7981():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7981)
    Sleep(70)

    def lambda_79A1():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_79A1)

    def lambda_79BC():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_79BC)
    Return()

    # Function_15_765C end

    def Function_16_79D2(): pass

    label("Function_16_79D2")


    def lambda_79D8():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5D, 1, lambda_79D8)

    def lambda_79F3():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5F, 1, lambda_79F3)
    Sleep(100)

    def lambda_7A13():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5E, 1, lambda_7A13)
    Sleep(80)

    def lambda_7A33():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x60, 1, lambda_7A33)

    def lambda_7A4E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x62, 1, lambda_7A4E)
    Sleep(70)

    def lambda_7A6E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x61, 1, lambda_7A6E)
    Sleep(30)

    def lambda_7A8E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5B, 1, lambda_7A8E)
    Sleep(90)

    def lambda_7AAE():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x58, 1, lambda_7AAE)

    def lambda_7AC9():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5C, 1, lambda_7AC9)

    def lambda_7AE4():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x59, 1, lambda_7AE4)
    Sleep(40)

    def lambda_7B04():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x57, 1, lambda_7B04)

    def lambda_7B1F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x5A, 1, lambda_7B1F)
    Sleep(30)

    def lambda_7B3F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x51, 1, lambda_7B3F)

    def lambda_7B5A():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x54, 1, lambda_7B5A)
    Sleep(70)

    def lambda_7B7A():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x53, 1, lambda_7B7A)

    def lambda_7B95():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x55, 1, lambda_7B95)
    Sleep(40)

    def lambda_7BB5():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x52, 1, lambda_7BB5)

    def lambda_7BD0():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x56, 1, lambda_7BD0)

    def lambda_7BEB():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4F, 1, lambda_7BEB)
    Sleep(50)

    def lambda_7C0B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4B, 1, lambda_7C0B)

    def lambda_7C26():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4E, 1, lambda_7C26)
    Sleep(30)

    def lambda_7C46():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4D, 1, lambda_7C46)
    Sleep(100)

    def lambda_7C66():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4C, 1, lambda_7C66)

    def lambda_7C81():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x50, 1, lambda_7C81)
    Sleep(30)

    def lambda_7CA1():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x4A, 1, lambda_7CA1)

    def lambda_7CBC():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x47, 1, lambda_7CBC)
    Sleep(60)

    def lambda_7CDC():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_7CDC)

    def lambda_7CF7():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x48, 1, lambda_7CF7)
    Sleep(70)

    def lambda_7D17():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_7D17)

    def lambda_7D32():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_7D32)
    Return()

    # Function_16_79D2 end

    def Function_17_7D48(): pass

    label("Function_17_7D48")


    def lambda_7D4E():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7B, 1, lambda_7D4E)

    def lambda_7D69():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7D, 1, lambda_7D69)
    Sleep(100)

    def lambda_7D89():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7C, 1, lambda_7D89)
    Sleep(80)

    def lambda_7DA9():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7E, 1, lambda_7DA9)

    def lambda_7DC4():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7DC4)
    Sleep(70)

    def lambda_7DE4():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_7DE4)
    Sleep(30)

    def lambda_7E04():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x79, 1, lambda_7E04)
    Sleep(90)

    def lambda_7E24():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x76, 1, lambda_7E24)

    def lambda_7E3F():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x7A, 1, lambda_7E3F)

    def lambda_7E5A():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x77, 1, lambda_7E5A)
    Sleep(40)

    def lambda_7E7A():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x75, 1, lambda_7E7A)

    def lambda_7E95():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x78, 1, lambda_7E95)
    Sleep(30)

    def lambda_7EB5():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6F, 1, lambda_7EB5)

    def lambda_7ED0():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x72, 1, lambda_7ED0)
    Sleep(70)

    def lambda_7EF0():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x71, 1, lambda_7EF0)

    def lambda_7F0B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x73, 1, lambda_7F0B)
    Sleep(40)

    def lambda_7F2B():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x70, 1, lambda_7F2B)

    def lambda_7F46():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x74, 1, lambda_7F46)

    def lambda_7F61():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6D, 1, lambda_7F61)
    Sleep(50)

    def lambda_7F81():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x69, 1, lambda_7F81)

    def lambda_7F9C():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6C, 1, lambda_7F9C)
    Sleep(30)

    def lambda_7FBC():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6B, 1, lambda_7FBC)
    Sleep(100)

    def lambda_7FDC():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6A, 1, lambda_7FDC)

    def lambda_7FF7():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x6E, 1, lambda_7FF7)
    Sleep(30)

    def lambda_8017():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x68, 1, lambda_8017)

    def lambda_8032():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x65, 1, lambda_8032)
    Sleep(60)

    def lambda_8052():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x63, 1, lambda_8052)

    def lambda_806D():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x66, 1, lambda_806D)
    Sleep(70)

    def lambda_808D():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x64, 1, lambda_808D)

    def lambda_80A8():
        OP_91(0xFE, 0x0, 0x0, 0x84D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x67, 1, lambda_80A8)
    Return()

    # Function_17_7D48 end

    def Function_18_80BE(): pass

    label("Function_18_80BE")

    OP_24(0x10F, 0x5F)
    OP_24(0x110, 0x5A)
    Sleep(350)
    OP_24(0x10F, 0x5A)
    OP_24(0x110, 0x55)
    Sleep(350)
    OP_24(0x10F, 0x55)
    OP_24(0x110, 0x50)
    Sleep(350)
    OP_24(0x10F, 0x50)
    OP_24(0x110, 0x4B)
    Sleep(350)
    OP_24(0x10F, 0x4B)
    OP_24(0x110, 0x46)
    Sleep(350)
    OP_24(0x10F, 0x46)
    OP_24(0x110, 0x41)
    Sleep(350)
    OP_24(0x10F, 0x41)
    OP_24(0x110, 0x3C)
    Sleep(350)
    OP_24(0x10F, 0x3C)
    OP_24(0x110, 0x37)
    Sleep(350)
    OP_24(0x10F, 0x37)
    OP_24(0x110, 0x32)
    Sleep(350)
    OP_24(0x10F, 0x32)
    OP_24(0x110, 0x2D)
    Sleep(350)
    OP_24(0x10F, 0x2D)
    OP_24(0x110, 0x28)
    Sleep(350)
    OP_24(0x10F, 0x28)
    OP_24(0x110, 0x23)
    Sleep(350)
    OP_24(0x10F, 0x23)
    OP_24(0x110, 0x1E)
    Sleep(350)
    OP_23(0x10F)
    OP_23(0x110)
    Return()

    # Function_18_80BE end

    SaveToFile()

Try(main)
