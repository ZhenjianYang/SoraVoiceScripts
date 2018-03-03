from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P0800   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P0800.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        'Arseille',                             # 9
        'Gilbert',                              # 10
        'G-Apache',                             # 11
        'Missile Dummy Character',              # 12
        'Missile Dummy Character',              # 13
        'Missile Dummy Character',              # 14
        'Missile Dummy Character',              # 15
        'Dragion 1',                            # 16
        'Dragion 2',                            # 17
        'Dragion 3',                            # 18
        'Dummy Camera',                         # 19
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03750 ._CH',             # 00
        'ED6_DT26/CH20739 ._CH',             # 01
        'ED6_DT29/CH14970 ._CH',             # 02
        'ED6_DT29/CH14800 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03750P._CP',             # 00
        'ED6_DT26/CH20739P._CP',             # 01
        'ED6_DT29/CH14970P._CP',             # 02
        'ED6_DT29/CH14800P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_22A",          # 00, 0
        "Function_1_297",          # 01, 1
        "Function_2_298",          # 02, 2
        "Function_3_874",          # 03, 3
        "Function_4_990",          # 04, 4
        "Function_5_AEC",          # 05, 5
        "Function_6_B4E",          # 06, 6
        "Function_7_B73",          # 07, 7
        "Function_8_13A1",         # 08, 8
        "Function_9_1562",         # 09, 9
        "Function_10_15EB",        # 0A, 10
        "Function_11_1D28",        # 0B, 11
        "Function_12_1D7A",        # 0C, 12
        "Function_13_1DB7",        # 0D, 13
        "Function_14_1E10",        # 0E, 14
        "Function_15_1E46",        # 0F, 15
        "Function_16_1EDD",        # 10, 16
        "Function_17_1F79",        # 11, 17
        "Function_18_2058",        # 12, 18
        "Function_19_2137",        # 13, 19
        "Function_20_226B",        # 14, 20
        "Function_21_239F",        # 15, 21
        "Function_22_2503",        # 16, 22
        "Function_23_2667",        # 17, 23
        "Function_24_386D",        # 18, 24
        "Function_25_390A",        # 19, 25
        "Function_26_395F",        # 1A, 26
        "Function_27_39A2",        # 1B, 27
        "Function_28_3AB8",        # 1C, 28
        "Function_29_3BB4",        # 1D, 29
        "Function_30_3CAB",        # 1E, 30
        "Function_31_3D27",        # 1F, 31
    )


    def Function_0_22A(): pass

    label("Function_0_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24B")
    OP_A3(0x2504)
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 23)
    Jump("loc_296")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 3)), scpexpr(EXPR_END)), "loc_265")
    OP_A3(0x250B)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)
    Jump("loc_296")

    label("loc_265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_27F")
    OP_A3(0x250A)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_296")

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_296")
    OP_A3(0x2509)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_296")

    Return()

    # Function_0_22A end

    def Function_1_297(): pass

    label("Function_1_297")

    Return()

    # Function_1_297 end

    def Function_2_298(): pass

    label("Function_2_298")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_1D(0x9D)
    LoadEffect(0x0, "scraft\\sc000_33.eff")
    LoadEffect(0x5, "map\\mp201_01.eff")
    LoadEffect(0x1, "monster\\ms30803a.eff")
    LoadEffect(0x2, "monster\\ms30803c.eff")
    LoadEffect(0x3, "monster\\ms30803d.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x17, 0x4)
    SetChrPos(0x17, -200000, 22740, -7040, 0)
    OP_72(0x404, 0x0)
    ExitThread()
    ClearChrFlags(0x17, 0x100)
    OP_D1(23, 0, 270000, 0, 0)
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 320)
    OP_70(0x4, 0x140)
    OP_E5(0x0, 0x4, 0x0, 262144)
    OP_E5(0x0, 0x4, 0x1, 262144)
    OP_E5(0x0, 0x4, 0x2, 262144)
    OP_E5(0x0, 0x4, 0x3, 262144)
    OP_E5(0x0, 0x4, 0x4, 262144)
    OP_E5(0x0, 0x4, 0x5, 262144)
    OP_E5(0x0, 0x4, 0x6, 262144)
    OP_E5(0x0, 0x4, 0x7, 262144)
    OP_E5(0x0, 0x4, 0x8, 262144)
    OP_E5(0x0, 0x4, 0x9, 262144)
    OP_E5(0x0, 0x4, 0xA, 262144)
    OP_E5(0x0, 0x4, 0xB, 262144)
    OP_E5(0x0, 0x4, 0xC, 262144)
    OP_E5(0x0, 0x4, 0xD, 262144)
    OP_E5(0x0, 0x4, 0xE, 262144)
    OP_E5(0x2, 0x4, 0x0, 300)
    OP_E5(0x2, 0x4, 0x1, 300)
    OP_E5(0x2, 0x4, 0x2, 300)
    OP_E5(0x2, 0x4, 0x3, 300)
    OP_E5(0x2, 0x4, 0x4, 300)
    OP_E5(0x2, 0x4, 0x5, 300)
    OP_E5(0x2, 0x4, 0x6, 300)
    OP_E5(0x2, 0x4, 0x7, 300)
    OP_E5(0x2, 0x4, 0x8, 300)
    OP_E5(0x2, 0x4, 0x9, 300)
    OP_E5(0x2, 0x4, 0xA, 300)
    OP_E5(0x2, 0x4, 0xB, 300)
    OP_E5(0x2, 0x4, 0xC, 300)
    OP_E5(0x2, 0x4, 0xD, 300)
    OP_E5(0x2, 0x4, 0xE, 300)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, -320000, 22740, -7040, 270)
    OP_72(0x403, 0x0)
    ExitThread()
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 1)
    OP_70(0x3, 0x258)
    PlayEffect(0x5, 0xFF, 0x10, 0, 1500, 16000, 90, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x10, 7300, -1600, 12000, 90, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x10, -7300, -1600, 12000, 90, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_22(0x125, 0x1, 0x64)
    OP_6D(-327270, -2550, 11860, 0)
    OP_67(0, 13480, -10000, 0)
    OP_6B(12970, 0)
    OP_6C(47000, 0)
    OP_6E(582, 0)
    OP_22(0x1C3, 0x0, 0x64)

    def lambda_578():

        label("loc_578")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_578")

    QueueWorkItem2(0x10, 3, lambda_578)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_5A1():
        OP_6D(-320270, -2550, 11860, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_5A1)

    def lambda_5B9():
        OP_67(0, 13780, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5B9)

    def lambda_5D1():
        OP_6B(10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_5D1)

    def lambda_5E1():
        OP_6E(580, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_5E1)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x1A, 0x0)
    OP_43(0x10, 0x0, 0x0, 0x4)
    Sleep(2500)
    OP_43(0x10, 0x2, 0x0, 0x5)
    Sleep(500)
    OP_43(0x17, 0x0, 0x0, 0x3)

    def lambda_61F():
        OP_6B(9670, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_61F)

    def lambda_62F():
        OP_6E(576, 4000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_62F)
    Sleep(2000)
    OP_22(0x158, 0x1, 0x3C)
    Sleep(2000)

    def lambda_64E():

        label("loc_64E")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_64E")

    QueueWorkItem2(0x10, 3, lambda_64E)

    def lambda_669():
        OP_6D(-278000, 1500, 35500, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_669)

    def lambda_681():
        OP_67(0, 4300, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_681)

    def lambda_699():
        OP_6B(8300, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_699)

    def lambda_6A9():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_6A9)

    def lambda_6B9():
        OP_6E(576, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6B9)
    OP_43(0x17, 0x3, 0x0, 0x6)
    WaitChrThread(0x1A, 0x1)
    Sleep(300)
    Fade(500)
    OP_22(0xF3, 0x0, 0x64)
    Play3DEffect(0x1, 0x4, 0x4, "Frame14_Bone__13_", 0x0, 0xF0, 0xFFFFFFBA, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_82(0x4, 0x2)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_44(0x1A, 0x0)
    OP_44(0x1A, 0x1)
    OP_44(0x1A, 0x2)
    OP_44(0x1A, 0x3)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_44(0x17, 0x0)
    OP_44(0x17, 0x1)
    OP_44(0x17, 0x2)
    OP_44(0x17, 0x3)
    OP_6D(-3450, 27700, -6990, 0)
    OP_67(0, -610, -10000, 0)
    OP_6B(1910, 0)
    OP_6C(269000, 0)
    OP_6E(1184, 0)

    def lambda_7A2():
        OP_6D(-4500, 27700, -4540, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_7A2)

    def lambda_7BA():
        OP_67(0, 2080, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_7BA)

    def lambda_7D2():
        OP_6B(1000, 8000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_7D2)

    def lambda_7E2():
        OP_6C(253000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_7E2)

    def lambda_7F2():
        OP_6E(1184, 8000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_7F2)

    def lambda_802():
        OP_D0(-4000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_802)
    SetChrPos(0x10, -350000, 10740, -7040, 270)
    SetChrPos(0x17, 0, 22740, -7040, 0)

    def lambda_834():

        label("loc_834")

        OP_7C(0xB4, 0xB4, 0xBB8, 0x64)
        OP_48()
        Jump("loc_834")

    QueueWorkItem2(0x10, 3, lambda_834)
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    OP_44(0xEE, 0x2)
    SetMapFlags(0x2000000)
    OP_A2(0x250A)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_298 end

    def Function_3_874(): pass

    label("Function_3_874")


    def lambda_87A():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_87A)
    Sleep(1700)

    def lambda_89A():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_89A)
    Sleep(1300)

    def lambda_8BA():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8BA)
    Sleep(1200)

    def lambda_8DA():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DA)
    Sleep(1000)

    def lambda_8FA():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8FA)
    Sleep(800)

    def lambda_91A():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91A)
    Sleep(600)

    def lambda_93A():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93A)
    Sleep(400)

    def lambda_95A():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95A)
    Sleep(200)

    def lambda_97A():
        OP_8F(0xFE, 0xFFFB1E00, 0x58D4, 0xFFFFE480, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97A)
    Return()

    # Function_3_874 end

    def Function_4_990(): pass

    label("Function_4_990")


    def lambda_996():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_996)
    Sleep(300)

    def lambda_9B6():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B6)
    Sleep(200)

    def lambda_9D6():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D6)
    Sleep(100)

    def lambda_9F6():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F6)
    Sleep(100)

    def lambda_A16():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A16)
    Sleep(100)

    def lambda_A36():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A36)
    Sleep(100)

    def lambda_A56():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A56)
    Sleep(100)

    def lambda_A76():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A76)
    Sleep(100)

    def lambda_A96():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A96)
    Sleep(100)

    def lambda_AB6():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AB6)
    Sleep(100)

    def lambda_AD6():
        OP_8F(0xFE, 0xFFF68A20, 0x58D4, 0xFFFFE480, 0xEA60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AD6)
    Return()

    # Function_4_990 end

    def Function_5_AEC(): pass

    label("Function_5_AEC")

    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_24(0x125, 0x14)
    Sleep(100)
    OP_24(0x125, 0x14)
    Sleep(100)
    OP_24(0x125, 0xA)
    Sleep(100)
    OP_24(0x125, 0x0)
    OP_23(0x125)
    Return()

    # Function_5_AEC end

    def Function_6_B4E(): pass

    label("Function_6_B4E")

    Sleep(1000)
    OP_24(0x158, 0x46)
    Sleep(500)
    OP_24(0x158, 0x50)
    Sleep(500)
    OP_24(0x158, 0x5A)
    Sleep(500)
    OP_24(0x158, 0x64)
    Return()

    # Function_6_B4E end

    def Function_7_B73(): pass

    label("Function_7_B73")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, -25640, 20480, 52840, 270)
    OP_72(0x403, 0x0)
    ExitThread()
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 1)
    OP_70(0x3, 0x258)
    OP_22(0x125, 0x1, 0x50)
    ClearChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x20)
    SetChrPos(0x11, -23340, 21840, 52790, 90)
    OP_48()
    LoadEffect(0x0, "monster\\msc1000.eff")
    LoadEffect(0x5, "map\\mp201_01.eff")
    PlayEffect(0x5, 0xFF, 0x10, 0, 1500, 16000, 90, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x10, 7300, -1600, 12000, 90, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x10, -7300, -1600, 12000, 90, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_6D(-18810, 21980, 52530, 0)
    OP_67(0, 6030, -10000, 0)
    OP_6B(1560, 0)
    OP_6C(47000, 0)
    OP_6E(627, 0)
    ClearMapFlags(0x10)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_D06():
        OP_8E(0xFE, 0xFFFFB5A0, 0x5550, 0xCC7E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D06)
    Sleep(500)
    OP_22(0x6D, 0x0, 0x64)
    WaitChrThread(0x11, 0x0)
    Fade(500)
    OP_6D(-19810, 22180, 53230, 0)
    OP_67(0, 4400, -10000, 0)
    OP_6B(1600, 0)
    OP_6C(311000, 0)
    OP_6E(586, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x11,
        (
            "#1226F#5PHeheheh... My moment has finally come.\x02\x03",

            "#1221FFrom now on, I will be the star of this show!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6B(1470, 100)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x11,
        (
            "#1226F#5PIf this world really does respond to people's\x01",
            "thoughts...\x02\x03",

            "#1221F...then come forth, my wings! Cleaver of the \x01",
            "clouds, bluer than the bluest sky...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #2
        0x11,
        "#1225F#5P#4SMy G-Apache!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    PlayEffect(0x0, 0x0, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -19670, 30000, 46300, 0)

    def lambda_F35():

        label("loc_F35")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F35")

    QueueWorkItem2(0x12, 3, lambda_F35)

    def lambda_F48():

        label("loc_F48")

        OP_7C(0x2, 0x2, 0xBB8, 0x64)
        OP_48()
        Jump("loc_F48")

    QueueWorkItem2(0x17, 2, lambda_F48)
    OP_22(0x135, 0x1, 0x0)
    Sleep(200)
    OP_24(0x135, 0xA)
    Sleep(200)
    OP_24(0x135, 0x14)
    Sleep(200)

    def lambda_F7F():

        label("loc_F7F")

        OP_7C(0x4, 0x4, 0xBB8, 0x64)
        OP_48()
        Jump("loc_F7F")

    QueueWorkItem2(0x17, 2, lambda_F7F)
    OP_24(0x135, 0x1E)
    Sleep(200)
    OP_24(0x135, 0x28)
    Sleep(200)
    OP_24(0x135, 0x32)

    def lambda_FB0():

        label("loc_FB0")

        OP_7C(0x6, 0x6, 0xBB8, 0x64)
        OP_48()
        Jump("loc_FB0")

    QueueWorkItem2(0x17, 2, lambda_FB0)
    Sleep(200)
    OP_24(0x135, 0x3C)
    Sleep(200)
    OP_24(0x135, 0x46)

    def lambda_FDD():

        label("loc_FDD")

        OP_7C(0x8, 0x8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_FDD")

    QueueWorkItem2(0x17, 2, lambda_FDD)
    Sleep(200)
    OP_24(0x135, 0x50)
    Sleep(200)
    OP_24(0x135, 0x5A)
    Sleep(200)
    OP_24(0x135, 0x64)

    def lambda_1013():

        label("loc_1013")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1013")

    QueueWorkItem2(0x17, 2, lambda_1013)
    Sleep(1000)
    Fade(500)
    OP_6D(-21500, 21980, 50830, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(1880, 0)
    OP_6C(315000, 0)
    OP_6E(596, 0)

    def lambda_1075():
        OP_8F(0xFE, 0xFFFFB32A, 0x59D8, 0xB4DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1075)
    OP_0D()
    OP_82(0x0, 0x2)
    SetChrChipByIndex(0x11, 0)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 180, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #3
        0x11,
        "#1221F#11PHAHAHA! I knew you would answer to my call!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x0)

    def lambda_10EF():
        OP_6D(-20870, 23040, 47470, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_10EF)

    def lambda_1107():
        OP_67(0, 5200, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1107)

    def lambda_111F():
        OP_6B(1980, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_111F)

    def lambda_112F():
        OP_6E(596, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_112F)

    def lambda_113F():
        OP_8E(0xFE, 0xFFFFB32A, 0x55DC, 0xC3AA, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_113F)
    WaitChrThread(0x11, 0x0)
    ClearChrFlags(0x11, 0x1)
    SetChrFlags(0x11, 0x4)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_116E():
        OP_96(0xFE, 0xFFFFB47E, 0x5DC0, 0xB34C, 0xBB8, 0x1194)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_116E)

    def lambda_118C():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_118C)
    Sleep(350)
    Fade(500)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x3)
    OP_22(0xCB, 0x0, 0x64)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x11, -18800, 23000, 46660, 0)
    SetChrChipByIndex(0x12, 3)
    SetChrSubChip(0x12, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)

    def lambda_11D7():
        OP_6D(-22120, 22040, 48940, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_11D7)

    def lambda_11EF():
        OP_67(0, 5200, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_11EF)

    def lambda_1207():
        OP_6B(1980, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1207)

    def lambda_1217():
        OP_6E(596, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1217)
    OP_8C(0x12, 90, 100)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    NpcTalk(    #4
        0x11,
        "Gilbert",
        (
            "#1226F#5P#100PI, Gilbert Stein, company commander of Ouroboros'\x01",
            "38th Enhanced Jaeger Unit...\x02\x03",

            "#1221F...will hereby commence diverting that Dragion\x01",
            "and taking it out of the sky!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_12FB():

        label("loc_12FB")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_12FB")

    QueueWorkItem2(0x12, 3, lambda_12FB)
    OP_8C(0x12, 90, 100)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_131E():
        OP_6D(-10270, 22040, 48540, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_131E)

    def lambda_1336():
        OP_67(0, 5200, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1336)

    def lambda_134E():
        OP_6B(2370, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_134E)

    def lambda_135E():
        OP_6E(612, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_135E)
    OP_43(0x12, 0x0, 0x0, 0x8)
    OP_43(0x11, 0x0, 0x0, 0x9)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x12, 0x0)
    WaitChrThread(0x11, 0x0)
    SetMapFlags(0x2000000)
    OP_A2(0x250B)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_B73 end

    def Function_8_13A1(): pass

    label("Function_8_13A1")

    OP_22(0x77, 0x0, 0x64)

    def lambda_13AC():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13AC)
    Sleep(100)

    def lambda_13CC():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13CC)
    Sleep(100)

    def lambda_13EC():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_13EC)
    Sleep(100)

    def lambda_140C():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_140C)
    Sleep(100)

    def lambda_142C():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_142C)
    Sleep(100)

    def lambda_144C():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_144C)
    Sleep(100)

    def lambda_146C():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_146C)
    Sleep(100)

    def lambda_148C():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_148C)
    Sleep(100)

    def lambda_14AC():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_14AC)
    Sleep(100)

    def lambda_14CC():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_14CC)
    Sleep(100)

    def lambda_14EC():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_14EC)
    Sleep(100)

    def lambda_150C():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_150C)
    Sleep(100)

    def lambda_152C():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_152C)
    Sleep(100)

    def lambda_154C():
        OP_8F(0xFE, 0x2E9DC, 0xC468, 0xC274, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_154C)
    Return()

    # Function_8_13A1 end

    def Function_9_1562(): pass

    label("Function_9_1562")

    Sleep(2000)
    OP_24(0x77, 0x5A)
    OP_24(0x135, 0x5A)
    Sleep(200)
    OP_24(0x77, 0x50)
    OP_24(0x135, 0x50)
    Sleep(200)
    OP_24(0x77, 0x46)
    OP_24(0x135, 0x46)
    Sleep(200)
    OP_24(0x77, 0x3C)
    OP_24(0x135, 0x3C)
    Sleep(200)
    OP_24(0x77, 0x32)
    OP_24(0x135, 0x32)
    Sleep(200)
    OP_24(0x77, 0x28)
    OP_24(0x135, 0x28)
    Sleep(200)
    OP_24(0x77, 0x1E)
    OP_24(0x135, 0x1E)
    Sleep(200)
    OP_24(0x77, 0x14)
    OP_24(0x135, 0x14)
    Sleep(200)
    OP_24(0x77, 0xA)
    OP_24(0x135, 0xA)
    Sleep(200)
    OP_24(0x77, 0x0)
    OP_24(0x135, 0x0)
    OP_23(0x77)
    OP_23(0x135)
    Return()

    # Function_9_1562 end

    def Function_10_15EB(): pass

    label("Function_10_15EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "monster\\msc0311.eff")
    LoadEffect(0x1, "monster\\ms10997.eff")
    LoadEffect(0x2, "monster\\msc0331.eff")
    LoadEffect(0x3, "map\\mp115_00.eff")
    LoadEffect(0x4, "battle\\btbomb00.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_A1(0x17, 0x4)
    SetChrPos(0x17, 70470, 26380, 52480, 270)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 320)
    OP_70(0x4, 0x140)
    OP_E5(0x0, 0x4, 0x0, 262144)
    OP_E5(0x0, 0x4, 0x1, 262144)
    OP_E5(0x0, 0x4, 0x2, 262144)
    OP_E5(0x0, 0x4, 0x3, 262144)
    OP_E5(0x0, 0x4, 0x4, 262144)
    OP_E5(0x0, 0x4, 0x5, 262144)
    OP_E5(0x0, 0x4, 0x6, 262144)
    OP_E5(0x0, 0x4, 0x7, 262144)
    OP_E5(0x0, 0x4, 0x8, 262144)
    OP_E5(0x0, 0x4, 0x9, 262144)
    OP_E5(0x0, 0x4, 0xA, 262144)
    OP_E5(0x0, 0x4, 0xB, 262144)
    OP_E5(0x0, 0x4, 0xC, 262144)
    OP_E5(0x0, 0x4, 0xD, 262144)
    OP_E5(0x0, 0x4, 0xE, 262144)
    OP_E5(0x2, 0x4, 0x0, 300)
    OP_E5(0x2, 0x4, 0x1, 300)
    OP_E5(0x2, 0x4, 0x2, 300)
    OP_E5(0x2, 0x4, 0x3, 300)
    OP_E5(0x2, 0x4, 0x4, 300)
    OP_E5(0x2, 0x4, 0x5, 300)
    OP_E5(0x2, 0x4, 0x6, 300)
    OP_E5(0x2, 0x4, 0x7, 300)
    OP_E5(0x2, 0x4, 0x8, 300)
    OP_E5(0x2, 0x4, 0x9, 300)
    OP_E5(0x2, 0x4, 0xA, 300)
    OP_E5(0x2, 0x4, 0xB, 300)
    OP_E5(0x2, 0x4, 0xC, 300)
    OP_E5(0x2, 0x4, 0xD, 300)
    OP_E5(0x2, 0x4, 0xE, 300)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -18900, 21940, 52480, 90)
    SetChrChipByIndex(0x12, 3)

    def lambda_17B5():

        label("loc_17B5")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_17B5")

    QueueWorkItem2(0x12, 3, lambda_17B5)
    OP_6D(-15920, 24500, 49750, 0)
    OP_67(0, 4070, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(315000, 0)
    OP_6E(430, 0)
    OP_22(0x135, 0x0, 0x64)

    def lambda_180A():

        label("loc_180A")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_180A")

    QueueWorkItem2(0x19, 3, lambda_180A)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x80, 0x0)
    FadeToBright(1000, 0)
    OP_22(0x35A, 0x0, 0x64)
    Sleep(1500)
    Fade(500)
    OP_6D(-19620, 24500, 50000, 0)
    OP_67(0, 4220, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(45000, 0)
    OP_6E(430, 0)

    def lambda_18B2():

        label("loc_18B2")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_18B2")

    QueueWorkItem2(0x19, 3, lambda_18B2)

    def lambda_18CD():

        label("loc_18CD")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_18CD")

    QueueWorkItem2(0x12, 3, lambda_18CD)
    PlayEffect(0x0, 0x0, 0x12, 1600, 900, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x12, -1600, 900, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    def lambda_194B():
        OP_6B(1840, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_194B)
    Sleep(1500)

    def lambda_1960():
        OP_6C(81000, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1960)
    OP_22(0x115, 0x0, 0x64)
    Sleep(500)
    OP_43(0x14, 0x0, 0x0, 0x14)
    Sleep(300)
    OP_43(0x13, 0x0, 0x0, 0x13)
    Sleep(300)
    OP_43(0x16, 0x0, 0x0, 0x16)
    Sleep(300)
    OP_43(0x15, 0x0, 0x0, 0x15)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_19B3():
        OP_6D(20280, 22500, 53170, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_19B3)

    def lambda_19CB():
        OP_67(0, 4540, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_19CB)

    def lambda_19E3():
        OP_6B(2570, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_19E3)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_23(0x35A)
    OP_22(0x35B, 0x0, 0x64)
    Sleep(2000)
    Fade(500)
    OP_44(0x1A, 0x0)
    OP_44(0x1A, 0x1)
    OP_44(0x1A, 0x2)
    OP_44(0x1A, 0x3)
    OP_44(0x13, 0x0)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x0)
    OP_44(0x14, 0x1)
    OP_44(0x15, 0x0)
    OP_44(0x15, 0x1)
    OP_44(0x16, 0x0)
    OP_44(0x16, 0x1)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_23(0x2D5)

    def lambda_1A4A():

        label("loc_1A4A")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1A4A")

    QueueWorkItem2(0x19, 3, lambda_1A4A)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x81, 0x0)
    OP_24(0x135, 0x0)
    OP_22(0x158, 0x1, 0x64)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    SetChrPos(0x17, 60470, 26380, 52480, 270)
    OP_6D(57620, 24900, 62590, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(5900, 0)
    OP_6C(40000, 0)
    OP_6E(480, 0)

    def lambda_1AFA():
        OP_6D(69520, 24900, 66040, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1AFA)

    def lambda_1B12():
        OP_67(0, 3180, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1B12)

    def lambda_1B2A():
        OP_6B(5900, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1B2A)

    def lambda_1B3A():
        OP_6C(45000, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1B3A)
    PlayEffect(0x1, 0x6, 0x17, 1000, 1500, 1500, 0, 40, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x7, 0x17, 1000, 2500, 1500, 0, 40, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_43(0x13, 0x0, 0x0, 0xF)
    OP_43(0x14, 0x0, 0x0, 0x10)
    OP_43(0x15, 0x0, 0x0, 0x11)
    OP_43(0x16, 0x0, 0x0, 0x12)
    Sleep(300)
    OP_43(0x17, 0x3, 0x0, 0xB)

    def lambda_1BE1():
        OP_6D(69520, 29900, 53040, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1BE1)

    def lambda_1BF9():
        OP_67(0, 1320, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1BF9)

    def lambda_1C11():
        OP_6C(85000, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1C11)

    def lambda_1C21():
        OP_8F(0xFE, 0xEC36, 0x6C20, 0xC530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1C21)
    WaitChrThread(0x17, 0x0)

    def lambda_1C41():
        OP_8F(0xFE, 0xEC36, 0x670C, 0xDCA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1C41)
    WaitChrThread(0x17, 0x0)
    Sleep(500)

    def lambda_1C66():
        OP_8F(0xFE, 0xFFBE, 0x6EDC, 0xC530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1C66)

    def lambda_1C81():
        OP_6D(69520, 28000, 50500, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_1C81)

    def lambda_1C99():
        OP_67(0, 1000, -10000, 2300)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1C99)

    def lambda_1CB1():
        OP_6C(90000, 3500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_1CB1)

    def lambda_1CC1():
        OP_6B(3680, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_1CC1)

    def lambda_1CD1():
        OP_6E(600, 5000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_1CD1)
    WaitChrThread(0x17, 0x0)
    Sleep(1000)

    def lambda_1CEB():
        OP_8F(0xFE, 0xD8AE, 0x6324, 0xC530, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1CEB)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x158)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    OP_A2(0x2505)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_15EB end

    def Function_11_1D28(): pass

    label("Function_11_1D28")

    OP_72(0x2004, 0x0)
    ExitThread()
    OP_D8(0x4, 0x3E8)
    OP_B0(0x4, 0xA)
    OP_22(0x2D3, 0x0, 0x64)
    OP_6F(0x4, 350)
    OP_70(0x4, 0x172)
    OP_73(0x4)
    OP_D8(0x4, 0x3E8)
    OP_6F(0x4, 370)
    OP_70(0x4, 0x177)
    OP_73(0x4)
    OP_71(0x2004, 0x0)
    ExitThread()
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 320)
    OP_70(0x4, 0x140)
    Return()

    # Function_11_1D28 end

    def Function_12_1D7A(): pass

    label("Function_12_1D7A")

    OP_72(0x2004, 0x0)
    ExitThread()
    OP_D8(0x4, 0x3E8)
    OP_B0(0x4, 0xC)
    OP_22(0x2D3, 0x0, 0x64)
    OP_6F(0x4, 350)
    OP_70(0x4, 0x177)
    OP_73(0x4)
    OP_71(0x2004, 0x0)
    ExitThread()
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 320)
    OP_70(0x4, 0x140)
    Return()

    # Function_12_1D7A end

    def Function_13_1DB7(): pass

    label("Function_13_1DB7")

    OP_24(0x2D5, 0x5A)
    Sleep(300)
    OP_24(0x2D5, 0x50)
    Sleep(300)
    OP_24(0x2D5, 0x46)
    Sleep(300)
    OP_24(0x2D5, 0x3C)
    Sleep(300)
    OP_24(0x2D5, 0x32)
    Sleep(300)
    OP_24(0x2D5, 0x28)
    Sleep(300)
    OP_24(0x2D5, 0x1E)
    Sleep(300)
    OP_24(0x2D5, 0x14)
    Sleep(300)
    OP_24(0x2D5, 0xA)
    Sleep(300)
    OP_24(0x2D5, 0x0)
    OP_23(0x2D5)
    Return()

    # Function_13_1DB7 end

    def Function_14_1E10(): pass

    label("Function_14_1E10")

    OP_44(0x19, 0x3)
    OP_7C(0x1F4, 0x1F4, 0xBB8, 0x1F4)
    Sleep(500)

    def lambda_1E30():

        label("loc_1E30")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1E30")

    QueueWorkItem2(0x19, 3, lambda_1E30)
    Return()

    # Function_14_1E10 end

    def Function_15_1E46(): pass

    label("Function_15_1E46")

    OP_22(0x2D5, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 20470, 28380, 54480, 90)
    ClearChrFlags(0xFE, 0x100)
    OP_D1(254, 0, 0, 0, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x3, 0x2, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1EBF():
        OP_8F(0xFE, 0x495B6, 0x6EDC, 0xD4D0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EBF)
    Sleep(2000)
    OP_82(0x2, 0x2)
    Return()

    # Function_15_1E46 end

    def Function_16_1EDD(): pass

    label("Function_16_1EDD")

    Sleep(1000)
    OP_22(0x2D5, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 20470, 28380, 52480, 90)
    ClearChrFlags(0xFE, 0x100)
    OP_D1(254, 0, 0, 0, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x3, 0x3, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1F5B():
        OP_8F(0xFE, 0x495B6, 0x6EDC, 0xC148, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F5B)
    Sleep(2000)
    OP_82(0x3, 0x2)
    Return()

    # Function_16_1EDD end

    def Function_17_1F79(): pass

    label("Function_17_1F79")

    Sleep(1500)
    OP_22(0x2D5, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 20470, 30380, 58480, 90)
    ClearChrFlags(0xFE, 0x100)
    OP_D1(254, 0, 0, 0, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x3, 0x4, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xF618, 0x72C4, 0xDCB4)

    def lambda_2009():
        OP_98(0x2, 0xFE, 0x9C40, 0x6)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2009)
    WaitChrThread(0xFE, 0x1)
    OP_82(0x4, 0x0)
    PlayEffect(0x4, 0x0, 0xFF, 63000, 29380, 56500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_43(0x19, 0x2, 0x0, 0xE)
    Return()

    # Function_17_1F79 end

    def Function_18_2058(): pass

    label("Function_18_2058")

    Sleep(2000)
    OP_22(0x2D5, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 20470, 26380, 30480, 90)
    ClearChrFlags(0xFE, 0x100)
    OP_D1(254, 0, 0, 0, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x3, 0x5, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x103A6, 0x7530, 0xC918)

    def lambda_20E8():
        OP_98(0x2, 0xFE, 0xAFC8, 0x6)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_20E8)
    WaitChrThread(0xFE, 0x1)
    OP_82(0x5, 0x0)
    PlayEffect(0x4, 0x1, 0xFF, 66470, 30000, 51480, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_43(0x19, 0x2, 0x0, 0xE)
    Return()

    # Function_18_2058 end

    def Function_19_2137(): pass

    label("Function_19_2137")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17000, 21000, 52480, 90)
    ClearChrFlags(0xFE, 0x100)
    OP_D1(254, 0, 0, 0, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x3, 0x2, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FA, 0x0, 0x64)
    OP_22(0x2D5, 0x0, 0x64)

    def lambda_21B5():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21B5)
    Sleep(200)

    def lambda_21D5():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21D5)
    Sleep(200)

    def lambda_21F5():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21F5)
    Sleep(200)

    def lambda_2215():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2215)
    Sleep(200)

    def lambda_2235():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2235)
    Sleep(200)

    def lambda_2255():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2255)
    Return()

    # Function_19_2137 end

    def Function_20_226B(): pass

    label("Function_20_226B")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17000, 21000, 54480, 90)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x100)
    OP_D1(254, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FA, 0x0, 0x64)
    OP_22(0x2D5, 0x0, 0x64)

    def lambda_22E9():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xD4D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22E9)
    Sleep(200)

    def lambda_2309():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xD4D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2309)
    Sleep(200)

    def lambda_2329():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xD4D0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2329)
    Sleep(200)

    def lambda_2349():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xD4D0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2349)
    Sleep(200)

    def lambda_2369():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xD4D0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2369)
    Sleep(200)

    def lambda_2389():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xD4D0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2389)
    Return()

    # Function_20_226B end

    def Function_21_239F(): pass

    label("Function_21_239F")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17000, 21000, 52480, 90)
    ClearChrFlags(0xFE, 0x100)
    OP_D1(254, 0, 0, 0, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x3, 0x4, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FA, 0x0, 0x64)
    OP_22(0x2D5, 0x0, 0x64)

    def lambda_241D():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_241D)
    Sleep(200)

    def lambda_243D():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_243D)
    Sleep(200)

    def lambda_245D():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_245D)
    Sleep(200)

    def lambda_247D():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_247D)
    Sleep(200)

    def lambda_249D():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_249D)
    Sleep(200)

    def lambda_24BD():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24BD)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x7530, 0x5DC0, 0xEC40)
    OP_98(0x1, 0x15F90, 0x4A38, 0xE470)

    def lambda_24F8():
        OP_98(0x2, 0xFE, 0x88B8, 0x6)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24F8)
    Return()

    # Function_21_239F end

    def Function_22_2503(): pass

    label("Function_22_2503")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -17000, 21000, 54480, 90)
    ClearChrFlags(0xFE, 0x100)
    OP_D1(254, 0, 0, 0, 0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x3, 0x5, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1FA, 0x0, 0x64)
    OP_22(0x2D5, 0x0, 0x64)

    def lambda_2581():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2581)
    Sleep(200)

    def lambda_25A1():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25A1)
    Sleep(200)

    def lambda_25C1():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25C1)
    Sleep(200)

    def lambda_25E1():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25E1)
    Sleep(200)

    def lambda_2601():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2601)
    Sleep(200)

    def lambda_2621():
        OP_8F(0xFE, 0x11170, 0x4A38, 0xCD00, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2621)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xC350, 0x3E80, 0xB590)
    OP_98(0x1, 0x15F90, 0x4E20, 0xC148)

    def lambda_265C():
        OP_98(0x2, 0xFE, 0x7530, 0x6)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_265C)
    Return()

    # Function_22_2503 end

    def Function_23_2667(): pass

    label("Function_23_2667")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    LoadEffect(0x0, "scraft\\sc000_33.eff")
    LoadEffect(0x1, "map\\mp095_00.eff")
    LoadEffect(0x5, "map\\mp201_01.eff")
    OP_A1(0x17, 0x4)
    SetChrPos(0x17, 44000, 21920, 51200, 270)
    OP_72(0x404, 0x0)
    ExitThread()
    ClearChrFlags(0x17, 0x100)
    OP_D1(23, 0, 270000, 0, 0)
    OP_B0(0x4, 0x1E)
    OP_6F(0x4, 320)
    OP_70(0x4, 0x140)
    OP_E5(0x0, 0x4, 0x0, 262144)
    OP_E5(0x0, 0x4, 0x1, 262144)
    OP_E5(0x0, 0x4, 0x2, 262144)
    OP_E5(0x0, 0x4, 0x3, 262144)
    OP_E5(0x0, 0x4, 0x4, 262144)
    OP_E5(0x0, 0x4, 0x5, 262144)
    OP_E5(0x0, 0x4, 0x6, 262144)
    OP_E5(0x0, 0x4, 0x7, 262144)
    OP_E5(0x0, 0x4, 0x8, 262144)
    OP_E5(0x0, 0x4, 0x9, 262144)
    OP_E5(0x0, 0x4, 0xA, 262144)
    OP_E5(0x0, 0x4, 0xB, 262144)
    OP_E5(0x0, 0x4, 0xC, 262144)
    OP_E5(0x0, 0x4, 0xD, 262144)
    OP_E5(0x0, 0x4, 0xE, 262144)
    OP_E5(0x2, 0x4, 0x0, 300)
    OP_E5(0x2, 0x4, 0x1, 300)
    OP_E5(0x2, 0x4, 0x2, 300)
    OP_E5(0x2, 0x4, 0x3, 300)
    OP_E5(0x2, 0x4, 0x4, 300)
    OP_E5(0x2, 0x4, 0x5, 300)
    OP_E5(0x2, 0x4, 0x6, 300)
    OP_E5(0x2, 0x4, 0x7, 300)
    OP_E5(0x2, 0x4, 0x8, 300)
    OP_E5(0x2, 0x4, 0x9, 300)
    OP_E5(0x2, 0x4, 0xA, 300)
    OP_E5(0x2, 0x4, 0xB, 300)
    OP_E5(0x2, 0x4, 0xC, 300)
    OP_E5(0x2, 0x4, 0xD, 300)
    OP_E5(0x2, 0x4, 0xE, 300)
    OP_A1(0x18, 0x5)
    SetChrPos(0x18, 44000, 21920, 53200, 270)
    OP_72(0x405, 0x0)
    ExitThread()
    ClearChrFlags(0x18, 0x100)
    OP_D1(24, 0, 270000, 0, 0)
    OP_B0(0x5, 0x1E)
    OP_6F(0x5, 320)
    OP_70(0x5, 0x140)
    OP_E5(0x0, 0x5, 0x0, 262144)
    OP_E5(0x0, 0x5, 0x1, 262144)
    OP_E5(0x0, 0x5, 0x2, 262144)
    OP_E5(0x0, 0x5, 0x3, 262144)
    OP_E5(0x0, 0x5, 0x4, 262144)
    OP_E5(0x0, 0x5, 0x5, 262144)
    OP_E5(0x0, 0x5, 0x6, 262144)
    OP_E5(0x0, 0x5, 0x7, 262144)
    OP_E5(0x0, 0x5, 0x8, 262144)
    OP_E5(0x0, 0x5, 0x9, 262144)
    OP_E5(0x0, 0x5, 0xA, 262144)
    OP_E5(0x0, 0x5, 0xB, 262144)
    OP_E5(0x0, 0x5, 0xC, 262144)
    OP_E5(0x0, 0x5, 0xD, 262144)
    OP_E5(0x0, 0x5, 0xE, 262144)
    OP_E5(0x2, 0x5, 0x0, 300)
    OP_E5(0x2, 0x5, 0x1, 300)
    OP_E5(0x2, 0x5, 0x2, 300)
    OP_E5(0x2, 0x5, 0x3, 300)
    OP_E5(0x2, 0x5, 0x4, 300)
    OP_E5(0x2, 0x5, 0x5, 300)
    OP_E5(0x2, 0x5, 0x6, 300)
    OP_E5(0x2, 0x5, 0x7, 300)
    OP_E5(0x2, 0x5, 0x8, 300)
    OP_E5(0x2, 0x5, 0x9, 300)
    OP_E5(0x2, 0x5, 0xA, 300)
    OP_E5(0x2, 0x5, 0xB, 300)
    OP_E5(0x2, 0x5, 0xC, 300)
    OP_E5(0x2, 0x5, 0xD, 300)
    OP_E5(0x2, 0x5, 0xE, 300)
    OP_A1(0x19, 0x6)
    SetChrPos(0x19, 44000, 21920, 56200, 270)
    OP_72(0x406, 0x0)
    ExitThread()
    ClearChrFlags(0x19, 0x100)
    OP_D1(25, 0, 270000, 0, 0)
    OP_B0(0x6, 0x1E)
    OP_6F(0x6, 320)
    OP_70(0x6, 0x140)
    OP_E5(0x0, 0x6, 0x0, 262144)
    OP_E5(0x0, 0x6, 0x1, 262144)
    OP_E5(0x0, 0x6, 0x2, 262144)
    OP_E5(0x0, 0x6, 0x3, 262144)
    OP_E5(0x0, 0x6, 0x4, 262144)
    OP_E5(0x0, 0x6, 0x5, 262144)
    OP_E5(0x0, 0x6, 0x6, 262144)
    OP_E5(0x0, 0x6, 0x7, 262144)
    OP_E5(0x0, 0x6, 0x8, 262144)
    OP_E5(0x0, 0x6, 0x9, 262144)
    OP_E5(0x0, 0x6, 0xA, 262144)
    OP_E5(0x0, 0x6, 0xB, 262144)
    OP_E5(0x0, 0x6, 0xC, 262144)
    OP_E5(0x0, 0x6, 0xD, 262144)
    OP_E5(0x0, 0x6, 0xE, 262144)
    OP_E5(0x2, 0x6, 0x0, 300)
    OP_E5(0x2, 0x6, 0x1, 300)
    OP_E5(0x2, 0x6, 0x2, 300)
    OP_E5(0x2, 0x6, 0x3, 300)
    OP_E5(0x2, 0x6, 0x4, 300)
    OP_E5(0x2, 0x6, 0x5, 300)
    OP_E5(0x2, 0x6, 0x6, 300)
    OP_E5(0x2, 0x6, 0x7, 300)
    OP_E5(0x2, 0x6, 0x8, 300)
    OP_E5(0x2, 0x6, 0x9, 300)
    OP_E5(0x2, 0x6, 0xA, 300)
    OP_E5(0x2, 0x6, 0xB, 300)
    OP_E5(0x2, 0x6, 0xC, 300)
    OP_E5(0x2, 0x6, 0xD, 300)
    OP_E5(0x2, 0x6, 0xE, 300)
    OP_A1(0x10, 0x3)
    SetChrPos(0x10, -21280, 18770, 24900, 270)
    OP_72(0x403, 0x0)
    ExitThread()
    PlayEffect(0x5, 0xFF, 0x10, 0, 1500, 16000, 90, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x10, 7300, -1600, 12000, 90, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0x10, -7300, -1600, 12000, 90, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    OP_22(0x125, 0x1, 0x64)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 2770, 20120, 26840, 90)
    SetChrChipByIndex(0x12, 3)

    def lambda_2B46():

        label("loc_2B46")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2B46")

    QueueWorkItem2(0x12, 3, lambda_2B46)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8)
    SetChrPos(0x11, -18470, 22000, 53060, 0)
    OP_6D(-26650, 20130, 26630, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(6040, 0)
    OP_6C(280000, 0)
    OP_6E(531, 0)

    def lambda_2BB1():
        OP_6D(-32400, 20130, 26630, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2BB1)

    def lambda_2BC9():
        OP_67(0, 1340, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2BC9)

    def lambda_2BE1():
        OP_6B(5960, 8000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2BE1)

    def lambda_2BF1():
        OP_6C(270000, 5000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_2BF1)

    def lambda_2C01():
        OP_6E(906, 8000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C01)
    OP_22(0x159, 0x0, 0x64)
    Sleep(1000)

    def lambda_2C1B():

        label("loc_2C1B")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2C1B")

    QueueWorkItem2(0x11, 3, lambda_2C1B)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x125, 0x1, 0x64)
    OP_22(0x135, 0x1, 0x3C)
    OP_43(0x10, 0x0, 0x0, 0x1F)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    OP_43(0x10, 0x3, 0x0, 0x1E)
    Sleep(2000)
    Fade(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x10, 0x3)
    OP_44(0x1A, 0x0)
    OP_44(0x1A, 0x1)
    OP_44(0x1A, 0x2)
    OP_44(0x1A, 0x3)
    OP_44(0x11, 0x1)
    OP_22(0x135, 0x1, 0x5A)
    SetChrPos(0x12, -18900, 21940, 52480, 90)
    OP_6D(-19700, 21860, 53900, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(323000, 0)
    OP_6E(284, 0)
    OP_44(0x11, 0x3)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x80, 0x0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #5
        0x11,
        "Gilbert",
        (
            "#1226F#5P#100PHeh. Ah, moments like these are the best part\x01",
            "of being a hero.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)

    NpcTalk(    #6
        0x11,
        "Gilbert",
        (
            "#1221F#5P#100P#3SIf only there were more people here to marvel\x01",
            "at just how cool I am this very moment!\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_2E2B():

        label("loc_2E2B")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2E2B")

    QueueWorkItem2(0x10, 3, lambda_2E2B)
    OP_22(0x158, 0x1, 0x50)
    Sleep(1000)

    def lambda_2E50():

        label("loc_2E50")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2E50")

    QueueWorkItem2(0x10, 3, lambda_2E50)
    OP_22(0x158, 0x1, 0x64)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #7
        0x11,
        "Gilbert",
        "#1224F#5P#100P...What?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrPos(0x17, 130000, 21920, 51200, 270)
    SetChrPos(0x18, 250000, 11920, 76200, 270)
    SetChrPos(0x19, 250000, 11920, 26200, 270)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_2EFB():
        OP_6D(87490, 23840, 51200, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2EFB)

    def lambda_2F13():
        OP_6B(4490, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2F13)
    Sleep(1000)

    def lambda_2F28():

        label("loc_2F28")

        OP_7C(0x32, 0x32, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2F28")

    QueueWorkItem2(0x10, 3, lambda_2F28)
    OP_22(0x135, 0x1, 0x46)
    OP_44(0x1A, 0x0)
    OP_44(0x1A, 0x1)
    OP_44(0x1A, 0x2)
    OP_44(0x1A, 0x3)
    OP_44(0x11, 0x1)
    Fade(500)
    OP_22(0x135, 0x1, 0x0)

    def lambda_2F66():

        label("loc_2F66")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2F66")

    QueueWorkItem2(0x10, 3, lambda_2F66)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x81, 0x0)
    OP_44(0x1A, 0x0)
    OP_44(0x1A, 0x1)
    OP_44(0x1A, 0x2)
    OP_44(0x1A, 0x3)
    OP_44(0x11, 0x1)
    OP_6D(130000, 20700, 51260, 0)
    OP_67(0, 5500, -10000, 0)
    OP_6B(3440, 0)
    OP_6C(90000, 0)
    OP_6E(720, 0)

    def lambda_300A():
        OP_6D(130000, 25500, 51060, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_300A)

    def lambda_3022():
        OP_67(0, -570, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3022)

    def lambda_303A():
        OP_6B(3800, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_303A)

    def lambda_304A():
        OP_6E(720, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_304A)

    def lambda_305A():

        label("loc_305A")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_305A")

    QueueWorkItem2(0x10, 3, lambda_305A)

    def lambda_3075():
        OP_8F(0xFE, 0x1D4C0, 0x49E8, 0x10298, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3075)
    Sleep(500)

    def lambda_3095():
        OP_8F(0xFE, 0x1C138, 0x49E8, 0x8D68, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_3095)
    WaitChrThread(0x1A, 0x0)
    Sleep(1000)
    Fade(500)
    OP_44(0x1A, 0x0)
    OP_44(0x1A, 0x1)
    OP_44(0x10, 0x3)
    OP_22(0x135, 0x1, 0x5A)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_6D(-19700, 21860, 53900, 0)
    OP_67(0, 5610, -10000, 0)
    OP_6B(3630, 0)
    OP_6C(323000, 0)
    OP_6E(284, 0)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_44(0x17, 0x0)
    OP_44(0x17, 0x1)
    OP_44(0x17, 0x2)
    OP_44(0x17, 0x3)
    OP_44(0x18, 0x0)
    OP_44(0x18, 0x1)
    OP_44(0x18, 0x2)
    OP_44(0x18, 0x3)
    OP_44(0x19, 0x0)
    OP_44(0x19, 0x1)
    OP_44(0x19, 0x2)
    OP_44(0x19, 0x3)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x80, 0x0)
    OP_0D()
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    NpcTalk(    #8
        0x11,
        "Gilbert",
        (
            "#1224F#5P#100PW-Wait a second! You can't gang up on me like\x01",
            "that! That's messed up!\x02\x03",

            "Arseille, can you hear me?! I take it all back!\x01",
            "I take it all back!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    NpcTalk(    #9
        0x11,
        "Gilbert",
        "#1227F#3S#5P#100PCraaap. They're out of range!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x135, 0x1, 0x0)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x81, 0x0)
    OP_6D(130919, 26260, 48300, 0)
    OP_67(0, -150, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(60000, 0)
    OP_6E(659, 0)
    OP_D0(10000, 0)

    def lambda_3362():
        OP_6B(3150, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3362)
    SetChrPos(0x12, -18900, 21940, 52480, 90)
    SetChrPos(0x17, 130000, 21920, 51200, 270)
    SetChrPos(0x18, 150000, 18000, 45200, 270)
    SetChrPos(0x19, 190000, 26920, 70200, 270)

    def lambda_33B6():

        label("loc_33B6")

        OP_7C(0x96, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_33B6")

    QueueWorkItem2(0x10, 3, lambda_33B6)
    OP_0D()
    Sleep(500)
    OP_22(0x1EC, 0x0, 0x64)
    OP_22(0x143, 0x1, 0x50)
    Play3DEffect(0x1, 0x0, 0x4, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x1, 0x1, 0x4, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    OP_22(0x1EC, 0x0, 0x5A)
    OP_22(0x143, 0x1, 0x5A)
    Play3DEffect(0x1, 0x2, 0x5, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x1, 0x3, 0x5, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    OP_22(0x1EC, 0x0, 0x50)
    OP_22(0x143, 0x1, 0x64)
    Play3DEffect(0x1, 0x4, 0x6, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x1, 0x5, 0x6, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x10E, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(100)
    OP_22(0x2D3, 0x0, 0x64)

    def lambda_3559():
        OP_D1(254, 0, 270000, 60000, 3000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_3559)

    def lambda_3573():
        OP_8F(0xFE, 0xFFFE0430, 0x55A0, 0xC800, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3573)
    Sleep(500)
    OP_22(0x2D3, 0x0, 0x64)

    def lambda_3598():
        OP_D1(254, 30000, 270000, -80000, 3000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_3598)

    def lambda_35B2():
        OP_8F(0xFE, 0xFFFDB610, 0x4650, 0xB090, 0xA7F8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_35B2)
    Sleep(500)
    OP_22(0x2D3, 0x0, 0x64)

    def lambda_35D7():
        OP_D1(254, 0, 270000, 100000, 3000)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_35D7)

    def lambda_35F1():
        OP_8F(0xFE, 0xFFFD19D0, 0x6928, 0x11238, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_35F1)
    Sleep(1500)
    OP_23(0x143)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x17, 0x0)
    OP_44(0x17, 0x3)
    OP_44(0x18, 0x0)
    OP_44(0x18, 0x3)
    OP_44(0x19, 0x0)
    OP_44(0x19, 0x3)
    SetChrPos(0x12, -18900, 21940, 52480, 90)

    def lambda_3650():

        label("loc_3650")

        OP_99(0xFE, 0x0, 0x7, 0x1194)
        OP_48()
        Jump("loc_3650")

    QueueWorkItem2(0x12, 3, lambda_3650)
    OP_22(0x135, 0x1, 0x50)
    SetChrPos(0x17, 30000, 21920, 52200, 270)
    SetChrPos(0x18, 50000, 18000, 52200, 270)
    SetChrPos(0x19, 80000, 26920, 52200, 270)
    OP_72(0x2004, 0x0)
    ExitThread()
    OP_B0(0x4, 0xF)
    OP_6F(0x4, 415)
    OP_70(0x4, 0x19F)
    OP_72(0x2005, 0x0)
    ExitThread()
    OP_B0(0x5, 0xF)
    OP_6F(0x5, 440)
    OP_70(0x5, 0x1B8)
    OP_72(0x2006, 0x0)
    ExitThread()
    OP_B0(0x6, 0xF)
    OP_6F(0x6, 415)
    OP_70(0x6, 0x19F)
    OP_6D(4190, 30000, 38480, 0)
    OP_67(0, 4970, -10000, 0)
    OP_6B(2250, 0)
    OP_6C(323000, 0)
    OP_6E(505, 0)
    OP_D0(0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x80, 0x0)
    OP_43(0x12, 0x0, 0x0, 0x18)
    Sleep(1500)

    def lambda_376D():
        OP_6D(2610, 25000, 41850, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_376D)

    def lambda_3785():
        OP_67(0, 320, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3785)

    def lambda_379D():
        OP_6B(2220, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_379D)

    def lambda_37AD():
        OP_6C(0, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_37AD)

    def lambda_37BD():
        OP_6E(573, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_37BD)
    Sleep(500)
    OP_43(0x17, 0x0, 0x0, 0x1B)
    OP_43(0x18, 0x0, 0x0, 0x1C)
    OP_43(0x19, 0x0, 0x0, 0x1D)
    Sleep(3000)
    Fade(500)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x81, 0x0)
    OP_82(0x80, 0x0)
    WaitChrThread(0x1A, 0x0)
    Sleep(3000)
    OP_43(0x11, 0x0, 0x0, 0x1A)
    OP_20(0x7D0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_43(0x11, 0x1, 0x0, 0x19)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x11, 0x1)
    Sleep(1000)
    OP_A2(0x2504)
    OP_A2(0x2506)
    NewScene("ED6_DT21/P0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_2667 end

    def Function_24_386D(): pass

    label("Function_24_386D")


    def lambda_3873():
        OP_8F(0xFE, 0xFFFFF4AC, 0x51CC, 0xCD00, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3873)
    Sleep(500)
    OP_8C(0x12, 0, 100)
    WaitChrThread(0x12, 0x1)

    def lambda_389F():
        OP_8F(0xFE, 0x8C3C, 0x22EC, 0x100F40, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_389F)
    Sleep(5000)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("Gilbert")

    AnonymousTalk(    #10 op#A
        "\x07\x00#40A#5P#4SAiiieeeeee! Aidios, help meeeeeeeeeeee!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_24_386D end

    def Function_25_390A(): pass

    label("Function_25_390A")

    OP_24(0x158, 0x5A)
    Sleep(200)
    OP_24(0x158, 0x50)
    Sleep(200)
    OP_24(0x158, 0x46)
    Sleep(200)
    OP_24(0x158, 0x3C)
    Sleep(200)
    OP_24(0x158, 0x32)
    Sleep(200)
    OP_24(0x158, 0x28)
    Sleep(200)
    OP_24(0x158, 0x1E)
    Sleep(200)
    OP_24(0x158, 0x14)
    Sleep(200)
    OP_24(0x158, 0xA)
    Sleep(200)
    OP_23(0x158)
    Return()

    # Function_25_390A end

    def Function_26_395F(): pass

    label("Function_26_395F")

    OP_24(0x135, 0x46)
    Sleep(300)
    OP_24(0x135, 0x3C)
    Sleep(300)
    OP_24(0x135, 0x32)
    Sleep(300)
    OP_24(0x135, 0x28)
    Sleep(300)
    OP_24(0x135, 0x1E)
    Sleep(300)
    OP_24(0x135, 0x14)
    Sleep(300)
    OP_24(0x135, 0xA)
    Sleep(300)
    OP_23(0x135)
    Return()

    # Function_26_395F end

    def Function_27_39A2(): pass

    label("Function_27_39A2")


    def lambda_39A8():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_39A8)

    def lambda_39C2():
        OP_8F(0xFE, 0x0, 0x51B8, 0xE358, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_39C2)
    OP_22(0x143, 0x1, 0x50)
    OP_22(0x2D3, 0x0, 0x64)

    def lambda_39E7():
        OP_D1(254, 0, 360000, 0, 2000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_39E7)
    Play3DEffect(0x1, 0x0, 0x4, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x1, 0x1, 0x4, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(2000)
    WaitChrThread(0x17, 0x1)

    def lambda_3A7B():
        OP_8F(0xFE, 0x2710, 0x5D70, 0x102598, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3A7B)
    WaitChrThread(0x17, 0x3)

    def lambda_3A9B():
        OP_D1(254, 0, 360000, 15000, 6000)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_3A9B)
    Sleep(5000)
    OP_23(0x143)
    Return()

    # Function_27_39A2 end

    def Function_28_3AB8(): pass

    label("Function_28_3AB8")

    Sleep(500)

    def lambda_3AC3():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_3AC3)

    def lambda_3ADD():
        OP_8F(0xFE, 0xFFFFEC78, 0x3A98, 0xC418, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3ADD)
    OP_22(0x143, 0x1, 0x50)
    OP_22(0x2D3, 0x0, 0x64)

    def lambda_3B02():
        OP_D1(254, 0, 360000, 0, 2000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_3B02)
    Play3DEffect(0x1, 0x2, 0x5, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x1, 0x3, 0x5, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(2000)
    WaitChrThread(0x18, 0x1)

    def lambda_3B96():
        OP_8F(0xFE, 0xFFFFEC78, 0x2710, 0x100658, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3B96)
    Sleep(5000)
    OP_23(0x143)
    Return()

    # Function_28_3AB8 end

    def Function_29_3BB4(): pass

    label("Function_29_3BB4")


    def lambda_3BBA():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_3BBA)

    def lambda_3BD4():
        OP_8F(0xFE, 0x2710, 0x3278, 0xC418, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3BD4)
    OP_22(0x143, 0x1, 0x64)
    OP_22(0x2D3, 0x0, 0x64)
    Sleep(2000)

    def lambda_3BFE():
        OP_D1(254, 0, 360000, 0, 2000)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_3BFE)
    Play3DEffect(0x1, 0x4, 0x6, "Frame34_Bone__33_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x1, 0x5, 0x6, "Frame26_Bone__25_", 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    WaitChrThread(0x19, 0x1)

    def lambda_3C8D():
        OP_8F(0xFE, 0x2710, 0x22D8, 0x100658, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3C8D)
    Sleep(5000)
    OP_23(0x143)
    Return()

    # Function_29_3BB4 end

    def Function_30_3CAB(): pass

    label("Function_30_3CAB")

    OP_24(0x125, 0x5A)
    OP_24(0x159, 0x5A)
    Sleep(300)
    OP_24(0x125, 0x50)
    OP_24(0x159, 0x50)
    Sleep(300)
    OP_24(0x125, 0x46)
    OP_24(0x159, 0x46)
    Sleep(300)
    OP_24(0x125, 0x3C)
    OP_24(0x159, 0x3C)
    Sleep(300)
    OP_24(0x125, 0x32)
    OP_24(0x159, 0x32)
    Sleep(300)
    OP_24(0x125, 0x28)
    OP_24(0x159, 0x28)
    Sleep(300)
    OP_24(0x125, 0x1E)
    OP_24(0x159, 0x1E)
    Sleep(300)
    OP_24(0x125, 0x14)
    OP_24(0x159, 0x14)
    Sleep(300)
    OP_24(0x125, 0xA)
    OP_24(0x159, 0xA)
    Sleep(300)
    OP_23(0x125)
    OP_23(0x159)
    Return()

    # Function_30_3CAB end

    def Function_31_3D27(): pass

    label("Function_31_3D27")


    def lambda_3D2D():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3D2D)
    Sleep(300)

    def lambda_3D4D():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3D4D)
    Sleep(300)

    def lambda_3D6D():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3D6D)
    Sleep(300)

    def lambda_3D8D():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3D8D)
    Sleep(300)

    def lambda_3DAD():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3DAD)
    Sleep(300)

    def lambda_3DCD():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3DCD)
    Sleep(300)

    def lambda_3DED():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3DED)
    Sleep(300)

    def lambda_3E0D():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E0D)
    Sleep(300)

    def lambda_3E2D():
        OP_8F(0xFE, 0xFFF80BC0, 0xFFFFE976, 0x6144, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E2D)
    Sleep(300)
    Return()

    # Function_31_3D27 end

    SaveToFile()

Try(main)
