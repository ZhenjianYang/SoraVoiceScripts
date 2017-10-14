from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0810_1 ._SN',
        MapName             = 'Event',
        Location            = 'E0810.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0810   ._SN',
            'ED6_DT21/E0810_1 ._SN',
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
        "Function_1_257",          # 01, 1
        "Function_2_2BC",          # 02, 2
        "Function_3_429",          # 03, 3
        "Function_4_5DE",          # 04, 4
        "Function_5_D2C",          # 05, 5
        "Function_6_D48",          # 06, 6
        "Function_7_DC8",          # 07, 7
        "Function_8_F3E",          # 08, 8
        "Function_9_FED",          # 09, 9
        "Function_10_10A1",        # 0A, 10
        "Function_11_1177",        # 0B, 11
        "Function_12_124D",        # 0C, 12
        "Function_13_127A",        # 0D, 13
        "Function_14_12A7",        # 0E, 14
        "Function_15_12D4",        # 0F, 15
        "Function_16_174C",        # 10, 16
        "Function_17_1831",        # 11, 17
        "Function_18_1916",        # 12, 18
        "Function_19_19FB",        # 13, 19
        "Function_20_1AE0",        # 14, 20
        "Function_21_22B9",        # 15, 21
        "Function_22_238F",        # 16, 22
        "Function_23_29A7",        # 17, 23
        "Function_24_2A27",        # 18, 24
        "Function_25_2AE3",        # 19, 25
        "Function_26_2DD3",        # 1A, 26
        "Function_27_2E33",        # 1B, 27
        "Function_28_2E9B",        # 1C, 28
        "Function_29_2F03",        # 1D, 29
        "Function_30_2F6B",        # 1E, 30
        "Function_31_3DC1",        # 1F, 31
        "Function_32_3E19",        # 20, 32
        "Function_33_3EFA",        # 21, 33
        "Function_34_4036",        # 22, 34
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearMapFlags(0x10)
    OP_6D(-153630, 3450, -35320, 0)
    OP_67(0, -2990, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(0, 0)
    OP_6E(542, 0)
    OP_72(0x0, 0x4)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -158650, -10000, -35510, 0)
    OP_B0(0x0, 0x14)
    SetChrPos(0x8, -158650, -5000, -35510, 90)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 1)
    ClearChrFlags(0x8, 0x80)
    OP_CF(0x8, 0x0, "Frame143_back_Null1")

    def lambda_160():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_160)
    OP_43(0xD, 0x2, 0x1, 0x1)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_18C():
        OP_67(0, -4360, -10000, 13000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_18C)

    def lambda_1A4():
        OP_6B(5920, 13000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1A4)
    Sleep(2000)

    def lambda_1B9():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B9)
    SetMessageWindowPos(250, 240, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #0 op#5
        "\x07\x00#1P#3SDAMMIIIIIIIIIIIT!!!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Sleep(2000)

    def lambda_219():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_219)
    OP_56(0x0)
    SetMapFlags(0x2000000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x10)
    OP_44(0xD, 0x2)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T1103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_0_AA end

    def Function_1_257(): pass

    label("Function_1_257")

    Sleep(1000)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x50)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x46)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x3C)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x32)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x28)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x1E)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x14)
    Sleep(1000)
    OP_22(0x120, 0x0, 0xA)
    Return()

    # Function_1_257 end

    def Function_2_2BC(): pass

    label("Function_2_2BC")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearMapFlags(0x10)
    OP_6D(-153630, 3450, -35320, 0)
    OP_67(0, -2990, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(0, 0)
    OP_6E(542, 0)
    OP_72(0x0, 0x4)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -158650, -10000, -35510, 0)
    OP_B0(0x0, 0x14)
    SetChrPos(0x8, -158650, -5000, -35510, 90)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 1)
    ClearChrFlags(0x8, 0x80)
    OP_CF(0x8, 0x0, "Frame143_back_Null1")
    OP_43(0xD, 0x2, 0x1, 0x1)

    def lambda_379():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_379)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_39E():
        OP_67(0, -4360, -10000, 12000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_39E)

    def lambda_3B6():
        OP_6B(5920, 12000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B6)
    Sleep(2000)

    def lambda_3CB():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3CB)
    Sleep(2000)

    def lambda_3EB():
        OP_90(0xFE, 0x0, 0x9C40, 0x186A0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3EB)
    FadeToDark(3000, 0, -1)
    OP_20(0xBB8)
    OP_0D()
    OP_21()
    OP_DC()
    ClearMapFlags(0x2000000)
    SetMapFlags(0x10)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1103   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2BC end

    def Function_3_429(): pass

    label("Function_3_429")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x101, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_6D(10000, -30000, 10000, 0)
    OP_67(0, -24200, -10000, 0)
    OP_6B(7780, 0)
    OP_6C(135000, 0)
    OP_6E(568, 0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0xAAE60, 0x0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, 10000, 20000, 0, 270)
    OP_22(0x125, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)

    def lambda_4D9():
        OP_6B(3130, 15000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4D9)

    def lambda_4E9():
        OP_6E(282, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E9)
    FadeToBright(2000, 0)

    def lambda_502():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_502)
    Sleep(500)

    def lambda_522():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_522)
    OP_24(0x125, 0x55)
    Sleep(500)

    def lambda_546():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_546)
    OP_24(0x125, 0x5A)
    Sleep(500)

    def lambda_56A():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_56A)
    OP_24(0x125, 0x5F)
    Sleep(500)

    def lambda_58E():
        OP_90(0xFE, 0x0, 0xFFFE0430, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_58E)
    OP_24(0x125, 0x64)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_429 end

    def Function_4_5DE(): pass

    label("Function_4_5DE")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x1, "map\\\\mp078_00.eff")
    LoadEffect(0x2, "monster\\\\ms10997.eff")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-2510, 8550, -1900, 0)
    OP_67(0, 13580, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(57000, 0)
    OP_6E(860, 0)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xD, 0x0)
    ClearChrFlags(0xD, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    SetChrPos(0xD, 0, 0, 0, 270)
    OP_43(0x14, 0x3, 0x1, 0x5)
    OP_A1(0xE, 0x1)
    OP_A1(0xF, 0x2)
    OP_A1(0x10, 0x3)
    ClearChrFlags(0xE, 0x100)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(14, 0, 90000, 0, 0)
    OP_D1(15, 0, 90000, 0, 0)
    OP_D1(16, 0, 90000, 0, 0)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_75C():
        OP_6D(10080, -10000, 12130, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_75C)

    def lambda_774():
        OP_67(0, 6620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_774)

    def lambda_78C():
        OP_6B(5200, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_78C)

    def lambda_79C():
        OP_6C(57000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_79C)

    def lambda_7AC():
        OP_6E(723, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7AC)
    WaitChrThread(0x101, 0x0)
    OP_72(0x1, 0x4)
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0x3C)
    OP_6F(0x1, 701)
    OP_70(0x1, 0x384)
    SetChrPos(0xE, 88460, -4550, 76480, 270)
    OP_D1(14, 0, 90000, 0, 0)
    OP_22(0x79, 0x1, 0x50)

    def lambda_806():
        OP_D1(254, 0, 90000, -20000, 4500)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_806)

    def lambda_820():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_820)
    Sleep(4000)
    OP_24(0x79, 0x55)

    def lambda_844():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_844)
    Sleep(200)
    OP_24(0x79, 0x5A)

    def lambda_868():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_868)
    Sleep(200)
    OP_24(0x79, 0x5F)

    def lambda_88C():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_88C)
    Sleep(100)
    OP_24(0x79, 0x64)

    def lambda_8B0():
        OP_8F(0xFE, 0x210C, 0xFFFFEE3A, 0x8E80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_8B0)
    Sleep(1000)
    OP_72(0x1, 0x20)
    OP_73(0x1)

    def lambda_8D8():
        OP_6D(32950, -10000, 22130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D8)
    OP_B0(0x1, 0x5A)
    OP_6F(0x1, 701)
    OP_70(0x1, 0x3AC)
    OP_43(0xE, 0x1, 0x1, 0x7)
    Sleep(2700)
    Fade(500)
    OP_44(0x101, 0x0)
    SetChrPos(0xE, 54240, -6550, 20200, 270)
    OP_D1(14, 5000, 70000, 20000, 0)
    OP_6D(33690, -3500, 13040, 0)
    OP_67(0, 500, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(225000, 0)
    OP_6E(723, 0)
    OP_0D()
    OP_71(0x1, 0x20)
    OP_B0(0x1, 0x3C)
    OP_6F(0x1, 941)
    OP_70(0x1, 0x3E8)
    OP_43(0x0, 0x0, 0x0, 0x20)
    PlayEffect(0x1, 0x1, 0xE, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_A3(0x1)
    OP_43(0xD, 0x3, 0x1, 0x6)
    Sleep(2000)
    OP_72(0x1, 0x20)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_A2(0x1)
    OP_23(0x235)
    OP_44(0x0, 0x0)
    Sleep(2000)

    def lambda_9FA():
        OP_6D(44940, 0, 13160, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9FA)

    def lambda_A12():
        OP_6C(200000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A12)

    def lambda_A22():
        OP_6E(829, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A22)
    OP_72(0x2, 0x4)
    OP_B0(0x2, 0x3C)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 701)
    OP_70(0x2, 0x384)
    SetChrPos(0xF, 93570, 14000, -1680, 270)
    OP_D1(15, 0, 90000, -20000, 0)
    OP_72(0x3, 0x4)
    OP_B0(0x3, 0x3C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 701)
    OP_70(0x3, 0x384)
    SetChrPos(0x10, 85510, 5000, -36750, 270)
    OP_D1(16, 0, 90000, -40000, 0)
    OP_43(0xF, 0x1, 0x1, 0x8)

    def lambda_AB9():
        OP_D1(254, -5000, 90000, 0, 3000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_AB9)
    Sleep(2500)
    OP_43(0x10, 0x1, 0x1, 0x9)

    def lambda_ADF():
        OP_D1(254, 0, 110000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_ADF)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    Fade(500)
    OP_6D(11050, 4050, -830, 0)
    OP_67(0, 2210, -10000, 0)
    OP_6B(5200, 0)
    OP_6C(91000, 0)
    OP_6E(829, 0)
    OP_0D()
    OP_71(0x1, 0x20)
    OP_71(0x2, 0x20)
    OP_71(0x3, 0x20)
    OP_6F(0x1, 941)
    OP_70(0x1, 0x3E8)
    OP_6F(0x2, 941)
    OP_70(0x2, 0x3E8)
    OP_6F(0x3, 941)
    OP_70(0x3, 0x3E8)
    OP_43(0x0, 0x0, 0x0, 0x20)
    PlayEffect(0x1, 0x1, 0xE, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xF, 0, 1500, -5000, 90, 355, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x10, 0, 1500, -5000, 110, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_A3(0x1)
    OP_43(0xD, 0x3, 0x1, 0x6)
    Sleep(2000)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 125)
    OP_70(0x0, 0x91)
    OP_73(0x0)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 100)
    OP_70(0x0, 0x78)
    Sleep(500)
    OP_22(0x195, 0x0, 0x64)
    OP_A2(0x1)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_43(0xD, 0x3, 0x1, 0xA)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    Sleep(200)
    OP_82(0x5, 0x0)
    OP_82(0x6, 0x0)
    OP_43(0x10, 0x3, 0x1, 0xE)
    Sleep(200)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_43(0xF, 0x3, 0x1, 0xD)
    Sleep(200)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_23(0x235)
    OP_44(0x0, 0x0)
    OP_43(0xE, 0x3, 0x1, 0xC)
    Sleep(400)
    OP_43(0x10, 0x0, 0x1, 0xB)
    Sleep(1000)
    OP_43(0xF, 0x0, 0x1, 0xB)
    Sleep(1000)
    OP_43(0xE, 0x0, 0x1, 0xB)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x3)
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_4_5DE end

    def Function_5_D2C(): pass

    label("Function_5_D2C")

    Sleep(900)

    label("loc_D31")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D47")
    OP_22(0x120, 0x0, 0x50)
    Sleep(1300)
    Jump("loc_D31")

    label("loc_D47")

    Return()

    # Function_5_D2C end

    def Function_6_D48(): pass

    label("Function_6_D48")

    PlayEffect(0x2, 0xFF, 0xD, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC7")
    PlayEffect(0x2, 0xFF, 0xD, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_D82")

    label("loc_DC7")

    Return()

    # Function_6_D48 end

    def Function_7_DC8(): pass

    label("Function_7_DC8")


    def lambda_DCE():
        OP_D1(254, 5000, 70000, 20000, 2600)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_DCE)

    def lambda_DE8():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_DE8)
    Sleep(100)

    def lambda_E08():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_E08)
    Sleep(100)

    def lambda_E28():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_E28)
    Sleep(200)

    def lambda_E48():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_E48)
    Sleep(300)

    def lambda_E68():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_E68)
    Sleep(500)

    def lambda_E88():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_E88)
    Sleep(1800)

    def lambda_EA8():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_EA8)
    Sleep(400)

    def lambda_EC8():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_EC8)
    Sleep(300)

    def lambda_EE8():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_EE8)
    Sleep(200)

    def lambda_F08():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_F08)
    Sleep(100)

    def lambda_F28():
        OP_8F(0xFE, 0xD3E0, 0xFFFFE66A, 0x4EE8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_F28)
    Return()

    # Function_7_DC8 end

    def Function_8_F3E(): pass

    label("Function_8_F3E")


    def lambda_F44():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_F44)
    OP_72(0x2, 0x20)
    Sleep(2100)

    def lambda_F69():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_F69)
    OP_6F(0x2, 901)
    OP_70(0x2, 0x3AC)
    Sleep(400)

    def lambda_F97():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_F97)
    Sleep(300)

    def lambda_FB7():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_FB7)
    Sleep(200)

    def lambda_FD7():
        OP_8F(0xFE, 0xDE62, 0x1B58, 0xFFFFF970, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_FD7)
    Return()

    # Function_8_F3E end

    def Function_9_FED(): pass

    label("Function_9_FED")


    def lambda_FF3():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_FF3)
    OP_72(0x3, 0x20)
    Sleep(900)
    OP_6F(0x3, 901)
    OP_70(0x3, 0x3AC)
    Sleep(900)

    def lambda_102B():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_102B)
    Sleep(400)

    def lambda_104B():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_104B)
    Sleep(300)

    def lambda_106B():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_106B)
    Sleep(200)

    def lambda_108B():
        OP_8F(0xFE, 0xEFF6, 0x3E8, 0xFFFFA25E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_108B)
    Return()

    # Function_9_FED end

    def Function_10_10A1(): pass

    label("Function_10_10A1")


    def lambda_10A7():
        OP_D1(254, 0, 270000, -50000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10A7)

    def lambda_10C1():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C1)
    Sleep(100)

    def lambda_10E1():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10E1)
    Sleep(100)

    def lambda_1101():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1101)
    Sleep(200)

    def lambda_1121():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1121)
    Sleep(200)

    def lambda_1141():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1141)
    Sleep(300)

    def lambda_1161():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1161)
    Return()

    # Function_10_10A1 end

    def Function_11_1177(): pass

    label("Function_11_1177")


    def lambda_117D():
        OP_D1(254, 0, 90000, 30000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_117D)

    def lambda_1197():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1197)
    Sleep(100)

    def lambda_11B7():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11B7)
    Sleep(100)

    def lambda_11D7():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11D7)
    Sleep(200)

    def lambda_11F7():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11F7)
    Sleep(200)

    def lambda_1217():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1217)
    Sleep(300)

    def lambda_1237():
        OP_91(0xFE, 0xFFF3CB00, 0x186A0, 0x493E0, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1237)
    Return()

    # Function_11_1177 end

    def Function_12_124D(): pass

    label("Function_12_124D")

    OP_72(0x1, 0x20)
    OP_73(0x1)
    OP_6F(0x1, 940)
    OP_70(0x1, 0x385)
    OP_73(0x1)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 900)
    OP_70(0x1, 0x2BD)
    Return()

    # Function_12_124D end

    def Function_13_127A(): pass

    label("Function_13_127A")

    OP_72(0x2, 0x20)
    OP_73(0x2)
    OP_6F(0x2, 940)
    OP_70(0x2, 0x385)
    OP_73(0x2)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 900)
    OP_70(0x2, 0x2BD)
    Return()

    # Function_13_127A end

    def Function_14_12A7(): pass

    label("Function_14_12A7")

    OP_72(0x3, 0x20)
    OP_73(0x3)
    OP_6F(0x3, 940)
    OP_70(0x3, 0x385)
    OP_73(0x3)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 900)
    OP_70(0x3, 0x2BD)
    Return()

    # Function_14_12A7 end

    def Function_15_12D4(): pass

    label("Function_15_12D4")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x101, 0x80)
    OP_6D(-98750, -550, -5980, 0)
    OP_67(0, 11650, -10000, 0)
    OP_6B(7460, 0)
    OP_6C(219000, 0)
    OP_6E(905, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x6F158, 0x0)
    OP_71(0x0, 0x4)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -100000, 10250, 0, 90)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 90000, 0, -150000, 315)
    SetChrPos(0x10, 113500, 0, -130000, 315)
    SetChrPos(0x11, 137000, 0, -110000, 315)
    SetChrPos(0x12, 160500, 0, -90000, 315)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(15, 0, 135000, 0, 0)
    OP_D1(16, 0, 135000, 0, 0)
    OP_D1(17, 0, 135000, 0, 0)
    OP_D1(18, 0, 135000, 0, 0)
    OP_22(0x125, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    FadeToBright(2000, 0)

    def lambda_1443():
        OP_67(0, 4930, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1443)
    WaitChrThread(0x101, 0x0)
    OP_B0(0x1, 0x3C)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 701)
    OP_70(0x1, 0x384)
    Sleep(100)
    OP_B0(0x3, 0x3C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 701)
    OP_70(0x3, 0x384)
    Sleep(100)
    OP_B0(0x2, 0x3C)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 701)
    OP_70(0x2, 0x384)
    Sleep(100)
    OP_B0(0x4, 0x3C)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 701)
    OP_70(0x4, 0x384)

    def lambda_14CB():
        OP_6D(-56120, -2750, -26300, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14CB)

    def lambda_14E3():
        OP_67(0, 4930, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14E3)

    def lambda_14FB():
        OP_6B(7460, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14FB)

    def lambda_150B():
        OP_6C(139000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_150B)

    def lambda_151B():
        OP_6E(905, 4000)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_151B)
    Sleep(2000)
    OP_22(0x79, 0x1, 0x50)
    OP_43(0xF, 0x1, 0x1, 0x10)
    OP_43(0x10, 0x1, 0x1, 0x11)
    OP_43(0x11, 0x1, 0x1, 0x12)
    OP_43(0x12, 0x1, 0x1, 0x13)
    WaitChrThread(0x101, 0x0)

    def lambda_1556():
        OP_6D(-25590, -2750, 4840, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1556)

    def lambda_156E():
        OP_6C(107000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_156E)
    Sleep(2000)
    OP_44(0xF, 0x2)

    def lambda_1587():
        OP_D1(254, 0, 250000, 0, 9000)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1587)
    OP_72(0x1, 0x20)
    Sleep(500)
    OP_44(0x10, 0x2)

    def lambda_15AF():
        OP_D1(254, 0, 270000, 0, 9000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_15AF)
    OP_72(0x2, 0x20)
    Sleep(500)
    OP_44(0x11, 0x2)

    def lambda_15D7():
        OP_D1(254, 0, 270000, 0, 9000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_15D7)
    OP_72(0x3, 0x20)
    Sleep(500)
    OP_44(0x12, 0x2)

    def lambda_15FF():
        OP_D1(254, 0, 290000, 0, 9000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_15FF)
    OP_72(0x4, 0x20)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    OP_44(0xF, 0x3)
    SetChrPos(0xF, 10000, 0, -45000, 315)
    OP_44(0x10, 0x3)
    SetChrPos(0x10, 0, 6000, -16000, 315)
    OP_44(0x11, 0x3)
    SetChrPos(0x11, 0, 6000, 16000, 315)
    OP_44(0x12, 0x3)
    SetChrPos(0x12, 10000, 0, 45000, 315)
    Fade(1000)
    OP_6D(-13160, -10000, -660, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(7460, 0)
    OP_6C(282000, 0)
    OP_6E(1343, 0)
    OP_24(0x79, 0x64)
    OP_24(0x125, 0x46)
    WaitChrThread(0x12, 0x2)
    Sleep(400)
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 901)
    OP_70(0x1, 0x3AC)
    Sleep(400)
    OP_B0(0x2, 0x1E)
    OP_6F(0x2, 901)
    OP_70(0x2, 0x3AC)
    Sleep(400)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 901)
    OP_70(0x3, 0x3AC)
    Sleep(400)
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 901)
    OP_70(0x4, 0x3AC)
    OP_73(0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_15_12D4 end

    def Function_16_174C(): pass

    label("Function_16_174C")

    OP_94(0x1, 0xFE, 0x0, 0x13880, 0x7530, 0x0)

    def lambda_1761():
        OP_D1(254, 0, 135000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1761)

    def lambda_177B():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_177B)
    Sleep(1900)

    def lambda_179B():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_179B)
    Sleep(200)

    def lambda_17BB():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_17BB)
    Sleep(200)

    def lambda_17DB():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_17DB)
    Sleep(100)

    def lambda_17FB():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_17FB)
    Sleep(100)

    def lambda_181B():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFF5038, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_181B)
    Return()

    # Function_16_174C end

    def Function_17_1831(): pass

    label("Function_17_1831")

    OP_94(0x1, 0xFE, 0x0, 0x13880, 0x7530, 0x0)

    def lambda_1846():
        OP_D1(254, 0, 135000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1846)

    def lambda_1860():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1860)
    Sleep(2500)

    def lambda_1880():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1880)
    Sleep(200)

    def lambda_18A0():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_18A0)
    Sleep(200)

    def lambda_18C0():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_18C0)
    Sleep(100)

    def lambda_18E0():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_18E0)
    Sleep(100)

    def lambda_1900():
        OP_8F(0xFE, 0x0, 0x0, 0xFFFFC180, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1900)
    Return()

    # Function_17_1831 end

    def Function_18_1916(): pass

    label("Function_18_1916")

    OP_94(0x1, 0xFE, 0x0, 0x13880, 0x7530, 0x0)

    def lambda_192B():
        OP_D1(254, 0, 135000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_192B)

    def lambda_1945():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1945)
    Sleep(3300)

    def lambda_1965():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1965)
    Sleep(200)

    def lambda_1985():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1985)
    Sleep(200)

    def lambda_19A5():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_19A5)
    Sleep(100)

    def lambda_19C5():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_19C5)
    Sleep(100)

    def lambda_19E5():
        OP_8F(0xFE, 0x0, 0x0, 0x3E80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_19E5)
    Return()

    # Function_18_1916 end

    def Function_19_19FB(): pass

    label("Function_19_19FB")

    OP_94(0x1, 0xFE, 0x0, 0x13880, 0x7530, 0x0)

    def lambda_1A10():
        OP_D1(254, 0, 135000, -20000, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1A10)

    def lambda_1A2A():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A2A)
    Sleep(4300)

    def lambda_1A4A():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A4A)
    Sleep(200)

    def lambda_1A6A():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A6A)
    Sleep(200)

    def lambda_1A8A():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A8A)
    Sleep(100)

    def lambda_1AAA():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1AAA)
    Sleep(100)

    def lambda_1ACA():
        OP_8F(0xFE, 0x0, 0x0, 0xAFC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1ACA)
    Return()

    # Function_19_19FB end

    def Function_20_1AE0(): pass

    label("Function_20_1AE0")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x1, "map\\\\mp078_00.eff")
    LoadEffect(0x2, "monster\\\\ms10997.eff")
    SetChrFlags(0x101, 0x80)
    OP_71(0x0, 0x4)
    OP_6D(-95940, 3750, -1830, 0)
    OP_67(0, 1090, -10000, 0)
    OP_6B(7300, 0)
    OP_6C(225000, 0)
    OP_6E(919, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_76(0xFF, 0x0, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -100000, 10250, 0, 90)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 10000, 0, -45000, 315)
    SetChrPos(0x10, 0, 6000, -15000, 315)
    SetChrPos(0x11, 0, 6000, 15000, 315)
    SetChrPos(0x12, 10000, 0, 45000, 315)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(15, 0, 260000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    OP_D1(18, 0, 280000, 0, 0)
    OP_22(0x125, 0x1, 0x50)
    OP_22(0x79, 0x1, 0x64)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_6F(0x1, 940)
    OP_6F(0x2, 940)
    OP_6F(0x3, 940)
    OP_6F(0x4, 940)
    FadeToBright(2000, 0)

    def lambda_1C8B():
        OP_6D(-8020, 3750, 7710, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C8B)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, 150000, 0, 0, 270)
    OP_72(0x0, 0x4)
    OP_D1(15, 5000, 70000, 20000, 0)
    OP_D1(16, -5000, 90000, 0, 0)
    OP_D1(17, 0, 110000, -20000, 0)
    SetChrPos(0xF, 224240, -6550, 20200, 270)
    SetChrPos(0x10, 226930, 7000, -1680, 270)
    SetChrPos(0x11, 231430, 1000, -23970, 270)
    OP_B0(0x1, 0x3C)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 941)
    OP_70(0x1, 0x3E8)
    OP_B0(0x2, 0x3C)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 941)
    OP_70(0x2, 0x3E8)
    OP_B0(0x3, 0x3C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 941)
    OP_70(0x3, 0x3E8)
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFB, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x61A80, 0x0)
    Fade(1000)
    OP_6D(168880, 3750, 210, 0)
    OP_67(0, 1090, -10000, 0)
    OP_6B(6360, 0)
    OP_6C(110000, 0)
    OP_6E(916, 0)
    OP_22(0x79, 0x1, 0x64)
    OP_23(0x125)
    OP_43(0x14, 0x3, 0x1, 0x5)
    OP_0D()
    OP_43(0x0, 0x0, 0x0, 0x20)
    PlayEffect(0x1, 0x1, 0xF, 0, 1500, -5000, 70, 5, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x7, 0xD, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x1, 0x0)
    PlayEffect(0x1, 0x2, 0x10, 0, 1500, -5000, 90, 355, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x2, 0x7, 0xD, 0, 4000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x2, 0x0)
    OP_82(0x7, 0x0)
    OP_44(0x0, 0x0)
    OP_23(0x235)

    def lambda_1F1F():
        OP_6D(169150, 3750, 0, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F1F)

    def lambda_1F37():
        OP_67(0, 1740, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F37)

    def lambda_1F4F():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1F4F)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 100)
    OP_70(0x0, 0x78)
    Sleep(500)
    OP_22(0x195, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 10)
    OP_70(0x0, 0x1E)
    OP_B0(0x0, 0x14)

    def lambda_1F99():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1F99)
    Sleep(100)

    def lambda_1FB9():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1FB9)
    Sleep(100)

    def lambda_1FD9():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1FD9)
    Sleep(200)

    def lambda_1FF9():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1FF9)
    Sleep(200)

    def lambda_2019():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2019)
    Sleep(300)

    def lambda_2039():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2039)
    Sleep(1000)
    OP_44(0x14, 0x3)
    OP_72(0x1, 0x20)
    OP_43(0xF, 0x0, 0x1, 0x15)
    Sleep(200)
    OP_72(0x2, 0x20)
    OP_43(0x10, 0x0, 0x1, 0x15)
    Sleep(200)
    OP_72(0x3, 0x20)
    OP_43(0x11, 0x0, 0x1, 0x15)
    Sleep(3000)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x877F8, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_76(0xFF, 0x0, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFF, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_44(0xD, 0x1)
    SetChrPos(0xD, 250000, 0, 0, 270)

    def lambda_2112():
        OP_91(0xFE, 0xFFFE7960, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2112)
    OP_B0(0x0, 0xF)
    SetChrPos(0xF, 10000, 0, -45000, 315)
    SetChrPos(0x10, 0, 6000, -15000, 315)
    SetChrPos(0x11, 0, 6000, 15000, 315)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_72(0x4, 0x20)
    OP_6F(0x1, 940)
    OP_6F(0x2, 940)
    OP_6F(0x3, 940)
    OP_6F(0x4, 940)
    OP_D1(15, 0, 260000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_D1(17, 0, 270000, 0, 0)
    Fade(1000)
    OP_6D(38580, 3750, 0, 0)
    OP_67(0, 1090, -10000, 0)
    OP_6B(7300, 0)
    OP_6C(90000, 0)
    OP_6E(919, 0)
    OP_22(0x79, 0x1, 0x64)
    OP_22(0x125, 0x1, 0x46)
    OP_0D()

    def lambda_222E():
        OP_6D(38580, 3750, 0, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_222E)

    def lambda_2246():
        OP_67(0, 1200, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2246)

    def lambda_225E():
        OP_6B(12530, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_225E)

    def lambda_226E():
        OP_6E(970, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_226E)
    OP_22(0x120, 0x0, 0x3C)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x41)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x46)
    Sleep(1300)
    FadeToDark(1000, 0, -1)
    OP_22(0x120, 0x0, 0x4B)
    Sleep(1300)
    OP_0D()
    OP_DC()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_20_1AE0 end

    def Function_21_22B9(): pass

    label("Function_21_22B9")


    def lambda_22BF():
        OP_D1(254, 20000, 90000, 30000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22BF)

    def lambda_22D9():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22D9)
    Sleep(100)

    def lambda_22F9():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22F9)
    Sleep(100)

    def lambda_2319():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2319)
    Sleep(200)

    def lambda_2339():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2339)
    Sleep(300)

    def lambda_2359():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2359)
    Sleep(500)

    def lambda_2379():
        OP_91(0xFE, 0x0, 0xFFFF8AD0, 0x61A80, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2379)
    Return()

    # Function_21_22B9 end

    def Function_22_238F(): pass

    label("Function_22_238F")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    LoadEffect(0x1, "map\\\\mp078_00.eff")
    LoadEffect(0x2, "monster\\\\ms10997.eff")
    SetChrFlags(0x101, 0x80)
    OP_6D(17660, 13750, -20070, 0)
    OP_67(0, 2990, -10000, 0)
    OP_6B(3670, 0)
    OP_6C(60000, 0)
    OP_6E(1289, 0)
    OP_76(0xFF, 0x0, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -100000, 10250, 0, 90)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 10000, 0, -45000, 90)
    SetChrPos(0x10, 0, 6000, -15000, 90)
    SetChrPos(0x11, 0, 6000, 15000, 90)
    SetChrPos(0x12, 10000, 0, 45000, 90)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(15, 0, 260000, 0, 0)
    OP_D1(16, 0, 268000, 0, 0)
    OP_D1(17, 0, 272000, 0, 0)
    OP_D1(18, 0, 280000, 0, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)
    OP_B0(0x1, 0x3C)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 941)
    OP_70(0x1, 0x3E8)
    OP_B0(0x2, 0x3C)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 941)
    OP_70(0x2, 0x3E8)
    OP_B0(0x3, 0x3C)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 941)
    OP_70(0x3, 0x3E8)
    OP_B0(0x4, 0x3C)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 941)
    OP_70(0x4, 0x3E8)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, 150000, 4000, 0, 270)
    ClearChrFlags(0xD, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    FadeToBright(2000, 0)
    Sleep(600)
    OP_43(0x0, 0x3, 0x0, 0x20)
    PlayEffect(0x1, 0x1, 0xF, 0, 1500, -5000, 250, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0x10, 0, 1500, -5000, 268, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0x3, 0x11, 0, 1500, -5000, 272, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0x12, 0, 1500, -5000, 290, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0xD, 0x0, 0x1, 0x18)
    OP_A3(0x1)
    OP_43(0xD, 0x3, 0x1, 0x17)

    def lambda_26AB():
        OP_6D(17020, 13750, 23220, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_26AB)

    def lambda_26C3():
        OP_6C(120000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26C3)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 170)
    OP_70(0x0, 0xBE)
    OP_73(0x0)
    OP_6F(0x0, 195)
    OP_70(0x0, 0xD7)
    OP_73(0x0)
    OP_6F(0x0, 220)
    OP_70(0x0, 0xE6)
    OP_22(0x195, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    SetChrPos(0xD, 60000, 4000, 0, 270)
    OP_44(0xD, 0x0)
    OP_44(0xD, 0x1)
    OP_6D(63240, 6750, -2890, 0)
    OP_67(0, 2630, -10000, 0)
    OP_6B(5120, 0)
    OP_6C(120000, 0)
    OP_6E(934, 0)
    OP_0D()

    def lambda_2787():
        OP_6D(62720, 6750, 2750, 11000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2787)

    def lambda_279F():
        OP_6B(3990, 11000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_279F)

    def lambda_27AF():
        OP_6C(57000, 11000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27AF)
    Sleep(1000)
    OP_72(0x0, 0x20)
    OP_73(0x0)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    OP_22(0x195, 0x0, 0x64)
    OP_73(0x0)
    OP_B0(0x0, 0xD)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    OP_73(0x0)
    OP_B0(0x0, 0xB)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    OP_22(0x195, 0x0, 0x64)
    OP_73(0x0)
    OP_B0(0x0, 0x9)
    OP_6F(0x0, 235)
    OP_70(0x0, 0x109)
    OP_73(0x0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_82(0x4, 0x2)
    OP_A2(0x1)
    OP_23(0x235)
    OP_44(0x0, 0x3)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 270)
    OP_70(0x0, 0x122)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    Fade(1000)
    OP_6D(60540, 6750, 220, 0)
    OP_67(0, -129430, -10000, 0)
    OP_6B(660, 0)
    OP_6C(90000, 0)
    OP_6E(934, 0)

    def lambda_289C():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_289C)
    OP_73(0x0)
    OP_B0(0x0, 0x2)
    OP_6F(0x0, 290)
    OP_70(0x0, 0x12C)
    Sleep(100)

    def lambda_28D1():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_28D1)
    Sleep(100)

    def lambda_28F1():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_28F1)
    Sleep(200)

    def lambda_2911():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2911)
    Sleep(200)

    def lambda_2931():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2931)
    Sleep(300)

    def lambda_2951():
        OP_91(0xFE, 0x0, 0xFFFE7960, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2951)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0xDC, 0x0, 0x64)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    Sleep(1500)
    OP_DC()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_22_238F end

    def Function_23_29A7(): pass

    label("Function_23_29A7")

    PlayEffect(0x2, 0x7, 0xD, -5000, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    label("loc_29E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A26")
    PlayEffect(0x2, 0x7, 0xD, -5000, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_29E1")

    label("loc_2A26")

    Return()

    # Function_23_29A7 end

    def Function_24_2A27(): pass

    label("Function_24_2A27")


    def lambda_2A2D():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A2D)
    Sleep(2500)

    def lambda_2A4D():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A4D)
    Sleep(400)

    def lambda_2A6D():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A6D)
    Sleep(300)

    def lambda_2A8D():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A8D)
    Sleep(200)

    def lambda_2AAD():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2AAD)
    Sleep(100)

    def lambda_2ACD():
        OP_8F(0xFE, 0xEA60, 0xFA0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2ACD)
    Return()

    # Function_24_2A27 end

    def Function_25_2AE3(): pass

    label("Function_25_2AE3")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x4, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_11(0xB8, 0xD8, 0xFF, 0x4E20, 0x3E418, 0x0)
    OP_6D(-30090, -10000, -9900, 0)
    OP_67(0, -12470, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(57000, 0)
    OP_6E(923, 0)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    SetChrPos(0xF, -30000, 0, 0, 90)
    SetChrPos(0x10, -15000, 0, 25000, 90)
    SetChrPos(0x11, -15000, 0, -25000, 90)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    OP_D1(15, 0, 90000, 0, 0)
    OP_D1(16, 0, 90000, 0, 0)
    OP_D1(17, 0, 90000, 0, 0)
    OP_22(0x79, 0x0, 0x64)
    OP_B0(0x1, 0x1E)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 500)
    OP_70(0x1, 0x208)
    OP_B0(0x3, 0x1E)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 500)
    OP_70(0x3, 0x208)
    OP_B0(0x2, 0x1E)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x208)
    OP_0D()
    LoadEffect(0x0, "map\\\\mp079_00.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_2C67():
        OP_6E(1100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C67)
    PlayEffect(0x0, 0xFF, 0xFF, -35000, -35000, 0, 90, -90, 0, 10000, 10000, 10000, 0xFF, 0, 0, 0, 0)
    OP_22(0x121, 0x0, 0x64)
    Sleep(600)
    OP_43(0xF, 0x2, 0x1, 0x1B)
    OP_43(0x10, 0x2, 0x1, 0x1C)
    OP_43(0x11, 0x2, 0x1, 0x1D)
    Sleep(3000)

    def lambda_2CD0():
        OP_6D(-13570, 30000, -19950, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2CD0)

    def lambda_2CE8():
        OP_67(0, -10590, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CE8)

    def lambda_2D00():
        OP_6B(2480, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D00)
    StopSound(0x4E20, 0x6F158, 0x1388)
    OP_72(0x0, 0x20)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 55)
    OP_70(0x0, 0x4B)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -25000, -55000, 0, 90)
    OP_72(0x0, 0x4)
    OP_43(0xD, 0x2, 0x1, 0x1A)

    def lambda_2D57():
        OP_91(0xD, 0x1D4C0, 0x30D40, 0x0, 0x8CA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2D57)
    Sleep(1000)

    def lambda_2D77():
        OP_91(0xD, 0x1D4C0, 0x30D40, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2D77)
    Sleep(1000)

    def lambda_2D97():
        OP_91(0xD, 0x1D4C0, 0x30D40, 0x0, 0xB3B0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2D97)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x2)
    SetMapFlags(0x2000000)
    OP_DC()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_2AE3 end

    def Function_26_2DD3(): pass

    label("Function_26_2DD3")

    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x5A)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x50)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x46)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x3C)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x32)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x28)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x1E)
    Sleep(1300)
    OP_22(0x120, 0x0, 0x14)
    Sleep(1300)
    OP_22(0x120, 0x0, 0xA)
    Return()

    # Function_26_2DD3 end

    def Function_27_2E33(): pass

    label("Function_27_2E33")


    def lambda_2E39():
        OP_91(0xFE, 0xFFFFE890, 0x0, 0xFFFFF830, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2E39)
    OP_D1(15, -10000, 80000, -10000, 700)
    OP_D1(15, 10000, 95000, 5000, 700)
    OP_D1(15, -5000, 85000, -5000, 800)
    OP_D1(15, 0, 90000, 0, 800)
    Return()

    # Function_27_2E33 end

    def Function_28_2E9B(): pass

    label("Function_28_2E9B")


    def lambda_2EA1():
        OP_91(0xFE, 0xFFFFEC78, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2EA1)
    OP_D1(16, -10000, 95000, 10000, 600)
    OP_D1(16, 5000, 80000, -10000, 600)
    OP_D1(16, -5000, 95000, 5000, 700)
    OP_D1(16, 0, 90000, 0, 700)
    Return()

    # Function_28_2E9B end

    def Function_29_2F03(): pass

    label("Function_29_2F03")


    def lambda_2F09():
        OP_91(0xFE, 0xBB8, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F09)
    OP_D1(17, 15000, 80000, -10000, 700)
    OP_D1(17, -5000, 90000, 10000, 700)
    OP_D1(17, 5000, 85000, -8000, 800)
    OP_D1(17, 0, 90000, 0, 800)
    Return()

    # Function_29_2F03 end

    def Function_30_2F6B(): pass

    label("Function_30_2F6B")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x1, "map\\\\mp077_00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-20560, 20530, -22790, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(8670, 0)
    OP_6C(54000, 0)
    OP_6E(523, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_71(0x0, 0x4)
    OP_A1(0xF, 0x1)
    OP_A1(0x10, 0x2)
    OP_A1(0x11, 0x3)
    OP_A1(0x12, 0x4)
    SetChrPos(0xF, 20000, 0, 20000, 90)
    SetChrPos(0x10, 20000, 0, -20000, 90)
    SetChrPos(0x11, 60000, 0, 30000, 90)
    SetChrPos(0x12, 60000, 0, -30000, 90)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    ClearChrFlags(0x11, 0x100)
    ClearChrFlags(0x12, 0x100)
    OP_D1(15, 0, 90000, 0, 0)
    OP_D1(16, 0, 90000, 0, 0)
    OP_D1(17, 0, 90000, 0, 0)
    OP_D1(18, 0, 90000, 0, 0)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -10000, 0, 0, 270)
    OP_48()
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    OP_89(0xA, -28840, 3200, 90, 270)
    OP_89(0x9, -28240, 3200, 820, 270)
    OP_89(0xB, -27820, 3200, -1500, 270)
    OP_89(0xC, -28450, 3200, -850, 270)
    OP_E5(0xA, 0x0, 0x0)
    OP_E5(0x9, 0x0, 0x0)
    OP_E5(0xC, 0x0, 0x0)
    OP_E5(0xB, 0x0, 0x0)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_22(0x125, 0x1, 0x50)
    OP_22(0x79, 0x1, 0x50)
    OP_B0(0x5, 0x1E)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0xA)
    OP_6F(0x5, 330)
    OP_70(0x5, 0x1AE)

    def lambda_317F():
        OP_6B(7490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_317F)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6D(-27780, 3000, -200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(54000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #1
        0xC,
        (
            "#156F#6PIt's getting pretty late...\x02\x03",

            "Ooooh, I hope everyone's okay!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xB,
        (
            "#142F#4PYou don't suppose the tables got\x01",
            "turned on 'em?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#176F#6PIf that were to happen, Sieg would have\x01",
            "returned to tell us that they're in danger.\x02\x03",

            "#178FFor now, all we can do is trust in them\x01",
            "and wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        "#145F#4PI hope so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "#160F#6P...\x02\x03",

            "#163FOne hour until nightfall...\x01",
            "Once that passes, we begin our assault.\x02\x03",

            "Captain. Ready the men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        "#175F#6PSir.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #7
        "\x07\x05#3SThat shall not be necessary.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0xB,
        "#143F#4PWh-Wh-What the hell was THAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "#178F#6PThat wasn't just me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        "#161F#6PWhere did that sound come from?!\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0xC,
        (
            "#153F#6PHuh?\x02\x03",

            "It looks like something reeeeal big's\x01",
            "coming up from below!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        "#173F#6PWHAT?!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(-73960, 11720, -1060, 0)
    OP_67(0, 7820, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(311000, 0)
    OP_6E(901, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_72(0x0, 0x4)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -130000, -30000, 0, 90)
    OP_6F(0x0, 55)
    OP_70(0x0, 0x4B)
    Sleep(400)
    PlayEffect(0x1, 0xFF, 0xFF, -104000, 0, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -104000, 0, 15000, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -104000, 0, -15000, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0xD, 0x3, 0x1, 0x1F)
    Sleep(200)
    OP_43(0xD, 0x0, 0x1, 0x20)
    OP_75(0x0, 0xD, 0x7)
    Sleep(3000)
    Fade(500)
    OP_6D(-6420, 12220, -23160, 0)
    OP_67(0, 1380, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(290000, 0)
    OP_6E(528, 0)
    WaitChrThread(0xD, 0x0)
    OP_72(0x0, 0x20)
    OP_73(0x0)

    def lambda_36E2():
        OP_6B(10, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_36E2)

    def lambda_36F2():
        OP_67(0, 500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36F2)

    def lambda_370A():
        OP_6E(360, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_370A)
    OP_6F(0x0, 76)
    OP_70(0x0, 0x5F)
    OP_73(0x0)
    OP_6F(0x0, 170)
    OP_70(0x0, 0xC3)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 195)
    OP_70(0x0, 0xD7)
    Sleep(1500)
    SetMessageWindowPos(230, 280, -1, -1)
    SetChrName("Ancient Dragon Ragnard")

    AnonymousTalk(    #13
        (
            "\x07\x05Brave bannermen of Auslese. Hearken to my\x01",
            "words.\x02\x03",

            "I am Ragnard, the dragon who has slumbered\x01",
            "in these lands since time immemorial.\x02\x03",

            "My will was wrested from me, turned toward the\x01",
            "machinations of the vile ones, but as surely as\x01",
            "I speak to thee now, thy bracers have freed me.\x02\x03",

            "The full tale is theirs to tell...\x01",
            "Till next we meet, I bid you fair skies.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    WaitChrThread(0x101, 0x0)
    OP_72(0x0, 0x20)
    OP_73(0x0)

    def lambda_38F3():
        OP_67(0, -1000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38F3)

    def lambda_390B():
        OP_91(0xFE, 0x186A0, 0x186A0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_390B)
    OP_6F(0x0, 575)
    OP_70(0x0, 0x258)

    def lambda_3934():
        OP_8C(0xD, 315, 100)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3934)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 600)
    OP_70(0x0, 0x26C)
    OP_43(0xD, 0x0, 0x1, 0x21)
    WaitChrThread(0x101, 0x1)
    Fade(500)
    OP_6D(-120890, 30000, 45390, 0)
    OP_67(0, 34330, -10000, 0)
    OP_6B(2280, 0)
    OP_6C(125000, 0)
    OP_6E(1200, 0)
    OP_0D()

    def lambda_39A7():
        OP_6B(2500, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39A7)
    Sleep(6000)
    Fade(500)
    OP_44(0xD, 0x3)
    OP_6D(-27780, 3000, -200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(54000, 0)
    OP_6E(262, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    Sleep(1000)
    OP_63(0xA)
    OP_63(0xB)
    OP_63(0xC)
    OP_63(0x9)
    OP_E5(0xA, 0x0, 0x1)
    OP_E5(0x9, 0x0, 0x1)
    OP_E5(0xC, 0x0, 0x1)
    OP_E5(0xB, 0x0, 0x1)
    Sleep(500)
    OP_DC()

    ChrTalk(    #14
        0xA,
        "#161F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        "#153F#6PWhoa! It's already out of sight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xB,
        "#143F#4PEr... We gonna, uh, give chase?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "#176F#6PWe can't possibly chase him at\x01",
            "that altitude.\x02\x03",

            "Even if the Arseille survived,\x01",
            "we would suffocate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "#163F#6POh, Aidios...\x02\x03",

            "#165FThose bracers are going to\x01",
            "have some explaining to do.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_24(0x79, 0x50)
    OP_24(0x125, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    OP_24(0x125, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    OP_24(0x125, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    OP_24(0x125, 0x32)
    Sleep(200)
    OP_24(0x79, 0x28)
    OP_24(0x125, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(200)
    OP_23(0x79)
    OP_23(0x125)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05And thus, the incident of the dragon that had shaken the\x01",
            "Bose region came to a close.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05Estelle and her group spent a long (long) time explaining\x01",
            "everything that had happened to General Morgan.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05When they were finally let go, they delivered the goldia crystals\x01",
            "entrusted to them by Ragnard to Mayor Maybelle and Elder Reisen.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05And so, one week later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1202   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_2F6B end

    def Function_31_3DC1(): pass

    label("Function_31_3DC1")

    Sleep(200)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1600)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x120, 0x0, 0x64)
    Sleep(1800)

    label("loc_3E02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E18")
    OP_22(0x120, 0x0, 0x64)
    Sleep(1300)
    Jump("loc_3E02")

    label("loc_3E18")

    Return()

    # Function_31_3DC1 end

    def Function_32_3E19(): pass

    label("Function_32_3E19")


    def lambda_3E1F():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E1F)
    Sleep(900)

    def lambda_3E3F():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E3F)
    Sleep(800)

    def lambda_3E5F():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E5F)
    Sleep(700)

    def lambda_3E7F():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E7F)
    Sleep(500)

    def lambda_3E9F():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3E9F)
    Sleep(400)

    def lambda_3EBF():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3EBF)
    Sleep(300)

    def lambda_3EDF():
        OP_8F(0xFE, 0xFFFEC780, 0xBB8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3EDF)
    WaitChrThread(0xD, 0x1)
    Return()

    # Function_32_3E19 end

    def Function_33_3EFA(): pass

    label("Function_33_3EFA")


    def lambda_3F00():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F00)
    Sleep(200)

    def lambda_3F20():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F20)
    Sleep(200)

    def lambda_3F40():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F40)
    Sleep(200)

    def lambda_3F60():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F60)
    Sleep(200)

    def lambda_3F80():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F80)
    Sleep(200)

    def lambda_3FA0():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3FA0)
    Sleep(200)

    def lambda_3FC0():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3FC0)
    Sleep(200)

    def lambda_3FE0():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x6590, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3FE0)
    Sleep(200)

    def lambda_4000():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4000)
    Sleep(200)

    def lambda_4020():
        OP_8F(0xFE, 0xFFFC0860, 0x3D090, 0x27100, 0x8CA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4020)
    Return()

    # Function_33_3EFA end

    def Function_34_4036(): pass

    label("Function_34_4036")


    def lambda_403C():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x61A8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_403C)
    Sleep(200)

    def lambda_405C():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0xFFFF9E58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_405C)
    Sleep(500)

    def lambda_407C():
        OP_8F(0xFE, 0xFFFF2928, 0x0, 0x61A8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_407C)
    Sleep(200)

    def lambda_409C():
        OP_8F(0xFE, 0xFFFF2928, 0x0, 0xFFFF9E58, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_409C)
    WaitChrThread(0xF, 0x1)

    def lambda_40BC():
        OP_D1(254, 0, 45000, 0, 1000)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_40BC)
    WaitChrThread(0x10, 0x1)

    def lambda_40DB():
        OP_D1(254, 0, 135000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_40DB)
    WaitChrThread(0x11, 0x1)

    def lambda_40FA():
        OP_D1(254, 0, 135000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_40FA)
    WaitChrThread(0x12, 0x1)

    def lambda_4119():
        OP_D1(254, 0, 45000, 0, 1000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4119)
    Return()

    # Function_34_4036 end

    SaveToFile()

Try(main)
