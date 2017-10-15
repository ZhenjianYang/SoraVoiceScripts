from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2300   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60060",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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


    AddCharChip(
        'ED6_DT29/CH12730 ._CH',             # 00
        'ED6_DT29/CH12731 ._CH',             # 01
        'ED6_DT29/CH12740 ._CH',             # 02
        'ED6_DT29/CH12741 ._CH',             # 03
        'ED6_DT29/CH12750 ._CH',             # 04
        'ED6_DT29/CH12751 ._CH',             # 05
        'ED6_DT29/CH12760 ._CH',             # 06
        'ED6_DT29/CH12761 ._CH',             # 07
        'ED6_DT29/CH12770 ._CH',             # 08
        'ED6_DT29/CH12771 ._CH',             # 09
        'ED6_DT29/CH12780 ._CH',             # 0A
        'ED6_DT29/CH12781 ._CH',             # 0B
        'ED6_DT29/CH12790 ._CH',             # 0C
        'ED6_DT29/CH12791 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12730P._CP',             # 00
        'ED6_DT29/CH12731P._CP',             # 01
        'ED6_DT29/CH12740P._CP',             # 02
        'ED6_DT29/CH12741P._CP',             # 03
        'ED6_DT29/CH12750P._CP',             # 04
        'ED6_DT29/CH12751P._CP',             # 05
        'ED6_DT29/CH12760P._CP',             # 06
        'ED6_DT29/CH12761P._CP',             # 07
        'ED6_DT29/CH12770P._CP',             # 08
        'ED6_DT29/CH12771P._CP',             # 09
        'ED6_DT29/CH12780P._CP',             # 0A
        'ED6_DT29/CH12781P._CP',             # 0B
        'ED6_DT29/CH12790P._CP',             # 0C
        'ED6_DT29/CH12791P._CP',             # 0D
    )

    DeclMonster(
        X                   = 120,
        Z                   = -3600,
        Y                   = -26100,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7833,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -8600,
        Z                   = -7200,
        Y                   = -1440,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x401,
        Unknown_18          = 7834,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 270,
        Z                   = -7650,
        Y                   = -200,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7835,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 9000,
        Z                   = -7200,
        Y                   = 980,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x400,
        Unknown_18          = 7836,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 380,
        Z                   = 400,
        Y                   = 50610,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x404,
        Unknown_18          = 7837,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_1C5",          # 01, 1
        "Function_2_234",          # 02, 2
        "Function_3_41A",          # 03, 3
        "Function_4_485",          # 04, 4
        "Function_5_4F0",          # 05, 5
        "Function_6_55B",          # 06, 6
        "Function_7_5C6",          # 07, 7
        "Function_8_6AC",          # 08, 8
        "Function_9_7A7",          # 09, 9
        "Function_10_81F",         # 0A, 10
        "Function_11_8A4",         # 0B, 11
        "Function_12_929",         # 0C, 12
        "Function_13_9AE",         # 0D, 13
        "Function_14_A33",         # 0E, 14
        "Function_15_B12",         # 0F, 15
        "Function_16_BF1",         # 10, 16
        "Function_17_C3F",         # 11, 17
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1B6"),
        (101, "loc_1BD"),
        (SWITCH_DEFAULT, "loc_1C4"),
    )


    label("loc_1B6")

    Event(0, 2)
    Jump("loc_1C4")

    label("loc_1BD")

    Event(0, 8)
    Jump("loc_1C4")

    label("loc_1C4")

    Return()

    # Function_0_1A6 end

    def Function_1_1C5(): pass

    label("Function_1_1C5")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 1)), scpexpr(EXPR_END)), "loc_1F9")
    SetChrFlags(0x8, 0x80)

    label("loc_1F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 2)), scpexpr(EXPR_END)), "loc_205")
    SetChrFlags(0x9, 0x80)

    label("loc_205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 3)), scpexpr(EXPR_END)), "loc_211")
    SetChrFlags(0xA, 0x80)

    label("loc_211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 4)), scpexpr(EXPR_END)), "loc_21D")
    SetChrFlags(0xB, 0x80)

    label("loc_21D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D3, 5)), scpexpr(EXPR_END)), "loc_229")
    SetChrFlags(0xC, 0x80)

    label("loc_229")

    OP_1B(0x0, 0x0, 0x7)
    OP_1B(0x1, 0x0, 0x9)
    Return()

    # Function_1_1C5 end

    def Function_2_234(): pass

    label("Function_2_234")

    EventBegin(0x0)
    OP_6D(110, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(158000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 0, 1050, -83970, 0)
    SetChrPos(0x102, 0, 1050, -83970, 0)
    SetChrPos(0xF8, 0, 1050, -83970, 0)
    SetChrPos(0xF9, 0, 1050, -83970, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    OP_C8(0x200, 0x46, "C_PLAC22._CH", 0x1, 0x1F4)
    OP_DE("Sapphirl Tower")
    FadeToBright(1000, 0)
    OP_43(0x101, 0x0, 0x0, 0x3)
    Sleep(800)

    def lambda_34B():
        OP_6D(140, 600, -78810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_34B)
    OP_43(0x102, 0x0, 0x0, 0x4)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x5)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x6)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(610, 600, -77870, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 610, 600, -77870, 0)
    SetChrPos(0x1, 610, 600, -77870, 0)
    SetChrPos(0x2, 610, 600, -77870, 0)
    SetChrPos(0x3, 610, 600, -77870, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_2_234 end

    def Function_3_41A(): pass

    label("Function_3_41A")


    def lambda_420():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_420)

    def lambda_43A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_43A)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_465():
        OP_8F(0xFE, 0x262, 0x258, 0xFFFECFD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_465)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_3_41A end

    def Function_4_485(): pass

    label("Function_4_485")


    def lambda_48B():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48B)

    def lambda_4A5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4A5)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_4D0():
        OP_8F(0xFE, 0xFFFFFE2A, 0x258, 0xFFFECEF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D0)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_485 end

    def Function_5_4F0(): pass

    label("Function_5_4F0")


    def lambda_4F6():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F6)

    def lambda_510():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_510)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_53B():
        OP_8F(0xFE, 0x276, 0x2EE, 0xFFFECA32, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_53B)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_4F0 end

    def Function_6_55B(): pass

    label("Function_6_55B")


    def lambda_561():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_561)

    def lambda_57B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57B)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_5A6():
        OP_8F(0xFE, 0xFFFFFDE4, 0x2EE, 0xFFFECA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A6)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_55B end

    def Function_7_5C6(): pass

    label("Function_7_5C6")

    EventBegin(0x0)
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(-600, 700, -83690, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(219000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 680, 700, -81310, 180)
    SetChrPos(0x102, -330, 700, -81100, 180)
    SetChrPos(0xF8, 910, 750, -79600, 180)
    SetChrPos(0xF9, -270, 750, -79450, 180)
    OP_43(0x101, 0x0, 0x0, 0xA)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0xB)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0xD)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/R2401   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_7_5C6 end

    def Function_8_6AC(): pass

    label("Function_8_6AC")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 250, 84500, 0)
    SetChrPos(0x101, 500, 250, 84000, 180)
    SetChrPos(0x102, -500, 250, 84000, 180)
    SetChrPos(0xF8, 500, 250, 85000, 180)
    SetChrPos(0xF9, -500, 250, 85000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 15)
    Call(0, 16)
    Fade(500)
    OP_6D(70, 250, 82530, 0)
    SetChrPos(0x0, 70, 250, 82530, 180)
    SetChrPos(0x1, 70, 250, 82530, 180)
    SetChrPos(0x2, 70, 250, 82530, 180)
    SetChrPos(0x3, 70, 250, 82530, 180)
    EventEnd(0x0)
    Return()

    # Function_8_6AC end

    def Function_9_7A7(): pass

    label("Function_9_7A7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 250, 84500, 0)
    SetChrPos(0x101, -500, 250, 85000, 0)
    SetChrPos(0x102, 500, 250, 85000, 0)
    SetChrPos(0xF8, -500, 250, 84000, 0)
    SetChrPos(0xF9, 500, 250, 84000, 0)
    OP_0D()
    Call(0, 15)
    Call(0, 17)
    NewScene("ED6_DT21/C2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_7A7 end

    def Function_10_81F(): pass

    label("Function_10_81F")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_864():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_864)

    def lambda_87E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_87E)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_10_81F end

    def Function_11_8A4(): pass

    label("Function_11_8A4")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_8E9():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8E9)

    def lambda_903():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_903)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_11_8A4 end

    def Function_12_929(): pass

    label("Function_12_929")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_96E():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96E)

    def lambda_988():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_988)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_12_929 end

    def Function_13_9AE(): pass

    label("Function_13_9AE")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_9F3():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F3)

    def lambda_A0D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A0D)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_13_9AE end

    def Function_14_A33(): pass

    label("Function_14_A33")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_14_A33 end

    def Function_15_B12(): pass

    label("Function_15_B12")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_15_B12 end

    def Function_16_BF1(): pass

    label("Function_16_BF1")


    def lambda_BF7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BF7)

    def lambda_C09():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C09)

    def lambda_C1B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C1B)

    def lambda_C2D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C2D)
    Sleep(2500)
    Return()

    # Function_16_BF1 end

    def Function_17_C3F(): pass

    label("Function_17_C3F")


    def lambda_C45():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C45)

    def lambda_C57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C57)

    def lambda_C69():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C69)

    def lambda_C7B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_C7B)
    Sleep(2000)
    Return()

    # Function_17_C3F end

    SaveToFile()

Try(main)
