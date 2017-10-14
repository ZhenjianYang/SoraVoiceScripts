from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3603   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3603.x',
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
        'ED6_DT29/CH12660 ._CH',             # 00
        'ED6_DT29/CH12661 ._CH',             # 01
        'ED6_DT29/CH12670 ._CH',             # 02
        'ED6_DT29/CH12671 ._CH',             # 03
        'ED6_DT29/CH12680 ._CH',             # 04
        'ED6_DT29/CH12681 ._CH',             # 05
        'ED6_DT29/CH12690 ._CH',             # 06
        'ED6_DT29/CH12691 ._CH',             # 07
        'ED6_DT29/CH12700 ._CH',             # 08
        'ED6_DT29/CH12701 ._CH',             # 09
        'ED6_DT29/CH12710 ._CH',             # 0A
        'ED6_DT29/CH12711 ._CH',             # 0B
        'ED6_DT29/CH12720 ._CH',             # 0C
        'ED6_DT29/CH12721 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12660P._CP',             # 00
        'ED6_DT29/CH12661P._CP',             # 01
        'ED6_DT29/CH12670P._CP',             # 02
        'ED6_DT29/CH12671P._CP',             # 03
        'ED6_DT29/CH12680P._CP',             # 04
        'ED6_DT29/CH12681P._CP',             # 05
        'ED6_DT29/CH12690P._CP',             # 06
        'ED6_DT29/CH12691P._CP',             # 07
        'ED6_DT29/CH12700P._CP',             # 08
        'ED6_DT29/CH12701P._CP',             # 09
        'ED6_DT29/CH12710P._CP',             # 0A
        'ED6_DT29/CH12711P._CP',             # 0B
        'ED6_DT29/CH12720P._CP',             # 0C
        'ED6_DT29/CH12721P._CP',             # 0D
    )

    DeclMonster(
        X                   = 4780,
        Z                   = -3800,
        Y                   = -34920,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x411,
        Unknown_18          = 7874,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -6020,
        Z                   = -3600,
        Y                   = -34270,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x411,
        Unknown_18          = 7875,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28010,
        Z                   = 200,
        Y                   = -13660,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x414,
        Unknown_18          = 7876,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 33740,
        Z                   = -50,
        Y                   = -20750,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x410,
        Unknown_18          = 7877,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_18A",          # 00, 0
        "Function_1_1BF",          # 01, 1
        "Function_2_22C",          # 02, 2
        "Function_3_33E",          # 03, 3
        "Function_4_3BF",          # 04, 4
        "Function_5_4BF",          # 05, 5
        "Function_6_537",          # 06, 6
        "Function_7_637",          # 07, 7
        "Function_8_6AF",          # 08, 8
        "Function_9_7AF",          # 09, 9
        "Function_10_827",         # 0A, 10
        "Function_11_906",         # 0B, 11
        "Function_12_9E5",         # 0C, 12
        "Function_13_A33",         # 0D, 13
    )


    def Function_0_18A(): pass

    label("Function_0_18A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1A2"),
        (101, "loc_1A9"),
        (102, "loc_1B0"),
        (103, "loc_1B7"),
        (SWITCH_DEFAULT, "loc_1BE"),
    )


    label("loc_1A2")

    Event(0, 2)
    Jump("loc_1BE")

    label("loc_1A9")

    Event(0, 4)
    Jump("loc_1BE")

    label("loc_1B0")

    Event(0, 6)
    Jump("loc_1BE")

    label("loc_1B7")

    Event(0, 8)
    Jump("loc_1BE")

    label("loc_1BE")

    Return()

    # Function_0_18A end

    def Function_1_1BF(): pass

    label("Function_1_1BF")

    LoadEffect(0x0, "map\\\\mp049_21.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 2)), scpexpr(EXPR_END)), "loc_1F3")
    SetChrFlags(0x8, 0x80)

    label("loc_1F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 3)), scpexpr(EXPR_END)), "loc_1FF")
    SetChrFlags(0x9, 0x80)

    label("loc_1FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 4)), scpexpr(EXPR_END)), "loc_20B")
    SetChrFlags(0xA, 0x80)

    label("loc_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D8, 5)), scpexpr(EXPR_END)), "loc_217")
    SetChrFlags(0xB, 0x80)

    label("loc_217")

    OP_1B(0x0, 0x0, 0x3)
    OP_1B(0x1, 0x0, 0x5)
    OP_1B(0x2, 0x0, 0x7)
    OP_1B(0x3, 0x0, 0x9)
    Return()

    # Function_1_1BF end

    def Function_2_22C(): pass

    label("Function_2_22C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, -3810, -71500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, -500, -3810, -71000, 0)
    SetChrPos(0x102, 500, -3810, -71000, 0)
    SetChrPos(0xF8, -500, -3810, -72000, 0)
    SetChrPos(0xF9, 500, -3810, -72000, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 10)
    Call(0, 12)
    Fade(500)
    OP_6D(-100, -3810, -69250, 0)
    OP_6C(45000, 0)
    SetChrPos(0x0, -100, -3810, -69250, 0)
    SetChrPos(0x1, -100, -3810, -69250, 0)
    SetChrPos(0x2, -100, -3810, -69250, 0)
    SetChrPos(0x3, -100, -3810, -69250, 0)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_2_22C end

    def Function_3_33E(): pass

    label("Function_3_33E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, -3810, -71500, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 500, -3810, -72000, 180)
    SetChrPos(0x102, -500, -3810, -72000, 180)
    SetChrPos(0xF8, 500, -3810, -71000, 180)
    SetChrPos(0xF9, -500, -3810, -71000, 180)
    OP_0D()
    Call(0, 10)
    Call(0, 13)
    NewScene("ED6_DT21/C3602   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_3_33E end

    def Function_4_3BF(): pass

    label("Function_4_3BF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(30800, 4240, 18500, 0)
    SetChrPos(0x101, 31300, 4240, 18000, 180)
    SetChrPos(0x102, 30300, 4240, 18000, 180)
    SetChrPos(0xF8, 31300, 4240, 19000, 180)
    SetChrPos(0xF9, 30300, 4240, 19000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 11)
    Call(0, 12)
    Fade(500)
    OP_6D(30720, 4240, 16250, 0)
    SetChrPos(0x0, 30720, 4240, 16250, 180)
    SetChrPos(0x1, 30720, 4240, 16250, 180)
    SetChrPos(0x2, 30720, 4240, 16250, 180)
    SetChrPos(0x3, 30720, 4240, 16250, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_4_3BF end

    def Function_5_4BF(): pass

    label("Function_5_4BF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(30800, 4240, 18500, 0)
    SetChrPos(0x101, 30300, 4240, 19000, 0)
    SetChrPos(0x102, 31300, 4240, 19000, 0)
    SetChrPos(0xF8, 30300, 4240, 18000, 0)
    SetChrPos(0xF9, 31300, 4240, 18000, 0)
    OP_0D()
    Call(0, 11)
    Call(0, 13)
    NewScene("ED6_DT21/C3604   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_5_4BF end

    def Function_6_537(): pass

    label("Function_6_537")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-30500, 190, -17000, 0)
    SetChrPos(0x101, -30000, 190, -17500, 180)
    SetChrPos(0x102, -31000, 190, -17500, 180)
    SetChrPos(0xF8, -30000, 190, -16500, 180)
    SetChrPos(0xF9, -31000, 190, -16500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 11)
    Call(0, 12)
    Fade(500)
    OP_6D(-30690, 190, -19100, 0)
    SetChrPos(0x0, -30690, 190, -19100, 180)
    SetChrPos(0x1, -30690, 190, -19100, 180)
    SetChrPos(0x2, -30690, 190, -19100, 180)
    SetChrPos(0x3, -30690, 190, -19100, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_6_537 end

    def Function_7_637(): pass

    label("Function_7_637")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-30500, 190, -17000, 0)
    SetChrPos(0x101, -31000, 190, -16500, 0)
    SetChrPos(0x102, -30000, 190, -16500, 0)
    SetChrPos(0xF8, -31000, 190, -17500, 0)
    SetChrPos(0xF9, -30000, 190, -17500, 0)
    OP_0D()
    Call(0, 11)
    Call(0, 13)
    NewScene("ED6_DT21/C3604   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_7_637 end

    def Function_8_6AF(): pass

    label("Function_8_6AF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 190, 36000, 0)
    SetChrPos(0x101, 500, 190, 35500, 180)
    SetChrPos(0x102, -500, 190, 35500, 180)
    SetChrPos(0xF8, 500, 190, 36500, 180)
    SetChrPos(0xF9, -500, 190, 36500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    Call(0, 11)
    Call(0, 12)
    Fade(500)
    OP_6D(100, 190, 34170, 0)
    SetChrPos(0x0, 100, 190, 34170, 180)
    SetChrPos(0x1, 100, 190, 34170, 180)
    SetChrPos(0x2, 100, 190, 34170, 180)
    SetChrPos(0x3, 100, 190, 34170, 180)
    SetMapFlags(0x1)
    EventEnd(0x2)
    Return()

    # Function_8_6AF end

    def Function_9_7AF(): pass

    label("Function_9_7AF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(0, 190, 36000, 0)
    SetChrPos(0x101, -500, 190, 36500, 0)
    SetChrPos(0x102, 500, 190, 36500, 0)
    SetChrPos(0xF8, -500, 190, 35500, 0)
    SetChrPos(0xF9, 500, 190, 35500, 0)
    OP_0D()
    Call(0, 11)
    Call(0, 13)
    NewScene("ED6_DT21/C3604   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_7AF end

    def Function_10_827(): pass

    label("Function_10_827")

    PlayEffect(0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_10_827 end

    def Function_11_906(): pass

    label("Function_11_906")

    PlayEffect(0x1, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_11_906 end

    def Function_12_9E5(): pass

    label("Function_12_9E5")


    def lambda_9EB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9EB)

    def lambda_9FD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9FD)

    def lambda_A0F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A0F)

    def lambda_A21():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A21)
    Sleep(2500)
    Return()

    # Function_12_9E5 end

    def Function_13_A33(): pass

    label("Function_13_A33")


    def lambda_A39():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A39)

    def lambda_A4B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A4B)

    def lambda_A5D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_A5D)

    def lambda_A6F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_A6F)
    Sleep(2000)
    Return()

    # Function_13_A33 end

    SaveToFile()

Try(main)
