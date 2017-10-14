from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3401   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3401.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
        'Monster',                              # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Air-Letten - Checkpoint',              # 13
        'Zeiss region',                         # 14
        ' ',                                    # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT09/CH10750 ._CH',             # 00
        'ED6_DT07/CH00160 ._CH',             # 01
        'ED6_DT07/CH00162 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00110 ._CH',             # 05
        'ED6_DT07/CH00111 ._CH',             # 06
        'ED6_DT07/CH00102 ._CH',             # 07
        'ED6_DT07/CH00161 ._CH',             # 08
        'ED6_DT09/CH10130 ._CH',             # 09
        'ED6_DT09/CH10131 ._CH',             # 0A
        'ED6_DT09/CH10750 ._CH',             # 0B
        'ED6_DT09/CH10751 ._CH',             # 0C
        'ED6_DT09/CH10760 ._CH',             # 0D
        'ED6_DT09/CH10761 ._CH',             # 0E
        'ED6_DT09/CH10770 ._CH',             # 0F
        'ED6_DT09/CH10771 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT09/CH10750P._CP',             # 00
        'ED6_DT07/CH00160P._CP',             # 01
        'ED6_DT07/CH00162P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00110P._CP',             # 05
        'ED6_DT07/CH00111P._CP',             # 06
        'ED6_DT07/CH00102P._CP',             # 07
        'ED6_DT07/CH00161P._CP',             # 08
        'ED6_DT09/CH10130P._CP',             # 09
        'ED6_DT09/CH10131P._CP',             # 0A
        'ED6_DT09/CH10750P._CP',             # 0B
        'ED6_DT09/CH10751P._CP',             # 0C
        'ED6_DT09/CH10760P._CP',             # 0D
        'ED6_DT09/CH10761P._CP',             # 0E
        'ED6_DT09/CH10770P._CP',             # 0F
        'ED6_DT09/CH10771P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 169300,
        Z                   = 0,
        Y                   = -27030,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 330710,
        Z                   = 0,
        Y                   = -37560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 257600,
        Z                   = 70,
        Y                   = -24310,
        Unknown_0C          = 180,
        Unknown_0E          = 15,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 286240,
        Z                   = 20,
        Y                   = -35830,
        Unknown_0C          = 180,
        Unknown_0E          = 9,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1D1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 222300,
        Y                   = -1000,
        Z                   = -28000,
        Range               = 217700,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF6CBC,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )


    DeclActor(
        TriggerX            = 199000,
        TriggerZ            = 500,
        TriggerY            = -22200,
        TriggerRange        = 800,
        ActorX              = 199000,
        ActorZ              = 1500,
        ActorY              = -22200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 285640,
        TriggerZ            = 0,
        TriggerY            = -26290,
        TriggerRange        = 1000,
        ActorX              = 285640,
        ActorZ              = 1000,
        ActorY              = -26290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_2B3",          # 01, 1
        "Function_2_324",          # 02, 2
        "Function_3_4AC",          # 03, 3
        "Function_4_637",          # 04, 4
        "Function_5_1E52",         # 05, 5
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Return()

    # Function_0_2B2 end

    def Function_1_2B3(): pass

    label("Function_1_2B3")

    OP_16(0x2, 0xFA0, 0x1F018, 0xFFFD9AB8, 0x30038)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2DA")
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_64(0x0, 0x1)

    label("loc_2DA")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 285640, 1000, -26290, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_2B3 end

    def Function_2_324(): pass

    label("Function_2_324")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_354")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_496")

    label("loc_354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_496")

    label("loc_36D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_496")

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_496")

    label("loc_39F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_496")

    label("loc_3B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_496")

    label("loc_3D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EA")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_496")

    label("loc_3EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_403")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_496")

    label("loc_403")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_496")

    label("loc_41C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_435")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_496")

    label("loc_435")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_496")

    label("loc_44E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_467")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_496")

    label("loc_467")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_480")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_496")

    label("loc_480")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_496")

    label("loc_4AB")

    Return()

    # Function_2_324 end

    def Function_3_4AC(): pass

    label("Function_3_4AC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9")
    OP_A2(0x504)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FE")

    ChrTalk(    #0
        0x101,
        (
            "#004FHey... Does this light\x01",
            "seem strange to you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_534")

    label("loc_4FE")


    ChrTalk(    #1
        0x101,
        (
            "#004FHey... Does that light\x01",
            "seem strange to you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_534")


    ChrTalk(    #2
        0x102,
        (
            "#012FIt does. Something's definitely\x01",
            "not right here.\x02\x03",

            "The power in the orbments is \x01",
            "gradually restored over time,\x01",
            "so that's not a concern...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_634")

    label("loc_5C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_600")

    ChrTalk(    #3
        0x101,
        "#000F...but something seems wrong.\x02",
    )

    CloseMessageWindow()
    Jump("loc_634")

    label("loc_600")


    ChrTalk(    #4
        0x102,
        (
            "#015FIt's flickering...\x01",
            "Something's not right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_634")

    EventEnd(0x1)
    Return()

    # Function_3_4AC end

    def Function_4_637(): pass

    label("Function_4_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E51")
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_A2(0x506)
    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 197700, 0, -23200, 45)
    SetChrPos(0x9, 199000, 0, -24200, 0)
    SetChrPos(0xA, 200900, 0, -24200, 315)
    SetChrPos(0xB, 200600, 0, -23100, 315)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)

    NpcTalk(    #5
        0x8,
        "Girl's Voice",
        "*sigh*...\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(1000)
    OP_6C(45000, 0)
    OP_6D(200700, 2000, -24400, 0)
    OP_31(0x6, 0x0, 0x12)
    OP_B5(0x6, 0x0)
    OP_B5(0x6, 0x1)
    OP_B5(0x6, 0x5)
    OP_B5(0x6, 0x4)
    OP_41(0x6, 0xB5)
    OP_41(0x6, 0xF4)
    OP_41(0x6, 0x112)
    OP_41(0x6, 0x2C9, 0x0)
    OP_41(0x6, 0x271, 0x1)
    OP_41(0x6, 0x262, 0x5)
    OP_41(0x6, 0x26B, 0x4)
    OP_35(0x6, 0xD2)
    OP_36(0x6, 0x104)
    AddParty(0x6, 0xFF)
    SetChrPos(0x107, 204300, 0, -26400, 270)
    OP_0D()
    OP_21()
    OP_1D(0x56)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    Sleep(500)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #6
        0x107,
        "Girl",
        (
            "#065F#2PI can't believe there\x01",
            "are so many of them...\x02\x03",

            "It's going to break, at this rate.\x02\x03",

            "Maybe this...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_81F():
        OP_6B(2600, 2500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_81F)
    Sleep(1000)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 2)
    OP_51(0x107, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Sleep(500)
    TurnDirection(0x107, 0xA, 0)

    NpcTalk(    #7
        0x107,
        "Girl",
        (
            "#062F#2PBearing set... Angle of elevation,\x01",
            "twenty degrees...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #8
        0x107,
        "Girl",
        (
            "#062F#2POrbal compression at thirty percent...\x02\x03",

            "#068F...GO!!\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x2, "map\\\\mp019_00.eff")

    def lambda_901():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_901)
    SetChrChipByIndex(0x107, 2)
    SetChrPos(0xE, 196500, 1500, -22500, 0)
    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0x107, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_99(0x107, 0x0, 0x3, 0x7D0)
    OP_99(0x107, 0x3, 0x7, 0x7D0)

    def lambda_979():
        OP_94(0x1, 0xFE, 0x78, 0x384, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_979)

    def lambda_98F():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_98F)

    def lambda_9A5():
        OP_94(0x1, 0xFE, 0xE6, 0x2BC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_9A5)

    def lambda_9BB():
        OP_94(0x1, 0xFE, 0x5A, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9BB)
    Sleep(1000)
    WaitChrThread(0x8, 0x1)

    def lambda_9DB():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9DB)
    WaitChrThread(0x9, 0x1)

    def lambda_9EE():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9EE)
    WaitChrThread(0xA, 0x1)

    def lambda_A01():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A01)
    WaitChrThread(0xB, 0x1)

    def lambda_A14():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A14)
    OP_8C(0x107, 270, 0)
    Sleep(400)

    NpcTalk(    #9
        0x107,
        "Girl",
        (
            "#062F#2PI-If you come any closer, then I won't miss\x01",
            "next time!\x02\x03",

            "I-I mean it!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(300)
    OP_62(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)
    OP_62(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(100)
    OP_62(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(200)
    Sleep(1000)

    def lambda_AE6():
        OP_6D(201700, 2000, -25100, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AE6)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xB, 0x20)

    def lambda_B12():
        OP_94(0x0, 0xFE, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B12)
    OP_63(0xA)
    Sleep(300)

    def lambda_B30():
        OP_94(0x0, 0xFE, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B30)
    OP_63(0xB)

    def lambda_B49():
        OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B49)
    OP_63(0x9)
    Sleep(600)

    def lambda_B67():
        OP_94(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B67)
    OP_63(0x8)
    SetChrChipByIndex(0x107, 1)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1700)

    NpcTalk(    #10
        0x107,
        "Girl",
        (
            "#065F#2POops... I think that might have made them\x01",
            "angrier...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 210200, 0, -30000, 0)
    SetChrPos(0x102, 209330, 0, -30000, 0)
    SetChrFlags(0x102, 0x4)

    def lambda_C0F():
        OP_94(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C0F)
    Sleep(150)

    def lambda_C2A():
        OP_94(0x0, 0xFE, 0x0, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C2A)

    def lambda_C40():
        OP_94(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C40)
    Sleep(300)

    def lambda_C5B():
        OP_94(0x0, 0xFE, 0x0, 0x258, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C5B)
    Sleep(400)

    NpcTalk(    #11
        0x107,
        "Girl",
        "#069F#2PAaaaah...!\x02",
    )

    OP_9E(0x107, 0x14, 0x0, 0x190, 0xFA0)
    CloseMessageWindow()

    def lambda_CA6():
        OP_94(0x0, 0xA, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_CA6)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)

    def lambda_CD0():
        OP_6B(3160, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CD0)

    def lambda_CE0():
        OP_6D(203200, 0, -24900, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CE0)

    def lambda_CF8():
        OP_6C(78000, 1200)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CF8)

    ChrTalk(    #12 op#A op#5
        0x101,
        "#10A#1PHyaaaahh!\x05\x02",
    )

    OP_8E(0x101, 0x326F4, 0x0, 0xFFFF9886, 0x2710, 0x0)

    def lambda_D32():
        OP_8E(0xFE, 0x317B8, 0x0, 0xFFFF952A, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D32)

    def lambda_D4D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_D4D)
    SetChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x107, 8)

    def lambda_D65():
        OP_8F(0xFE, 0x3214A, 0x0, 0xFFFF9566, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_D65)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 7)

    def lambda_D90():
        OP_99(0xFE, 0x0, 0xC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D90)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0x1F4, 0x0, 0x64)
    OP_96(0x101, 0x31830, 0x0, 0xFFFF9C00, 0x5DC, 0x1770)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    PlayEffect(0x8, 0xFF, 0xFF, 202800, 0, -25600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_E07():
        OP_94(0x1, 0xA, 0xB4, 0x7D0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E07)
    OP_96(0x101, 0x31A92, 0x0, 0xFFFF9A52, 0x1F4, 0x1388)

    def lambda_E34():
        OP_94(0x1, 0xFE, 0xB4, 0x384, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E34)

    def lambda_E4A():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E4A)

    def lambda_E60():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E60)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x102, 5)
    ClearChrFlags(0x102, 0x4)
    Sleep(1000)

    NpcTalk(    #13
        0x107,
        "Girl",
        "#065FHuh...?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x107, 1)
    ClearChrFlags(0x107, 0x1000)
    TurnDirection(0x107, 0x101, 400)

    NpcTalk(    #14
        0x107,
        "Girl",
        "#560FHey, I remember you...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#006FWe can talk later!\x01",
            "Get back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#012FWe've got to get rid of\x01",
            "these things first!\x02",
        )
    )

    CloseMessageWindow()
    Battle(0x3A7, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_F49"),
        (SWITCH_DEFAULT, "loc_F4C"),
    )


    label("loc_F49")

    OP_B4(0x0)
    Return()

    label("loc_F4C")

    EventBegin(0x0)
    OP_4F(0x23, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, 202800, 0, -25600, 315)
    SetChrPos(0x102, 202500, 0, -27300, 315)
    SetChrPos(0x107, 204200, 0, -26900, 315)
    OP_6D(203400, 0, -26050, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #17
        0x107,
        "Girl",
        (
            "#065FTh-That was scary...\x02\x03",

            "#067FUmm...\x01",
            "Thank you very much.\x02\x03",

            "I thought I was a goner,\x01",
            "for sure.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)

    def lambda_1040():
        OP_6B(2790, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1040)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x107, 400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x107, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #18
        0x101,
        (
            "#001FHa ha ha. Well, the important\x01",
            "thing is that you're safe.\x02\x03",

            "#006FBut you really should\x01",
            "be more careful.\x02\x03",

            "Stirring up monsters is a surefire\x01",
            "way to get yourself eaten.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #19
        0x107,
        "Girl",
        (
            "#065FBut...\x02\x03",

            "If I'd left them alone, they probably would've\x01",
            "broken that light...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#505FSpeaking of which...\x02\x03",

            "Why would those things go\x01",
            "after the lights anyway?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_12D6")

    ChrTalk(    #21
        0x102,
        (
            "#010FDon't they do the same\x01",
            "thing when the highway\x01",
            "lights are switched out?\x02\x03",

            "The septium in those circuits\x01",
            "is the monsters' favorite food.\x02\x03",

            "The highway lights work\x01",
            "to keep monsters away...\x02\x03",

            "But when they stop working,\x01",
            "they have the exact opposite\x01",
            "effect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1392")

    label("loc_12D6")


    ChrTalk(    #22
        0x102,
        (
            "#010FThe septium in those circuits\x01",
            "is the monsters' favorite food.\x02\x03",

            "The highway lights work\x01",
            "to keep monsters away...\x02\x03",

            "But when they stop working,\x01",
            "they have the exact opposite\x01",
            "effect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1392")


    ChrTalk(    #23
        0x101,
        (
            "#501FAhh, I get it.\x02\x03",

            "#007FStill, you shouldn't mess\x01",
            "with stuff like that.\x02\x03",

            "Septium might be their favorite\x01",
            "food, but little girls probably\x01",
            "rank a close second.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x107,
        "Girl",
        "#063FOh... S-Sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#019FGo easy, there.\x02\x03",

            "Giving her nightmares and saying,\x01",
            "'Don't do that,' isn't exactly\x01",
            "going to score you any points.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#509FOh, don't be such a wet blanket.\x02\x03",

            "#006FAnyway, my name's Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#010FAnd I'm Joshua.\x02\x03",

            "We're bracers, affiliated with\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x107,
        "Girl",
        (
            "#061FOhhh, so that's why you're\x01",
            "so tough.\x02\x03",

            "#060FI'm Tita.\x02\x03",

            "I work as an apprentice\x01",
            "at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#501FWow, that's pretty impressive.\x02\x03",

            "Well, then, Tita...\x02\x03",

            "We're heading to Zeiss, so do\x01",
            "you want to join us the rest of\x01",
            "the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#010FThat's right. You don't want\x01",
            "to be around here if the\x01",
            "monsters show up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x107,
        (
            "#061FR-Really...? Thank you!\x02\x03",

            "#560FWould you mind waiting\x01",
            "for a little bit?\x02\x03",

            "I've gotta get that light fixed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#004FYeah, it's probably risky\x01",
            "to leave it like that.\x02\x03",

            "How in the world did you\x01",
            "know it had burned out,\x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        (
            "#060FWell, I was lucky enough to notice\x01",
            "the problem when I was looking in\x01",
            "the computer database...\x02\x03",

            "It seems like a defective unit\x01",
            "was installed here by mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#010FAh, all right. It's a good thing\x01",
            "you caught it when you did!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#505F(Computer? Database?)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(198940, 30, -23590, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 199360, 10, -24480, 0)
    SetChrPos(0x102, 198190, 20, -24530, 0)
    SetChrPos(0x107, 199160, 20, -22710, 0)
    SetChrFlags(0x107, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #36
        0x107,
        "#062F#4P...Mmph.\x02",
    )

    CloseMessageWindow()
    OP_72(0x1, 0x4)
    Sleep(100)
    OP_71(0x1, 0x4)
    Sleep(100)
    OP_72(0x1, 0x4)
    Sleep(100)
    OP_71(0x1, 0x4)
    Sleep(90)
    OP_72(0x1, 0x4)
    Sleep(80)
    OP_71(0x1, 0x4)
    Sleep(70)
    OP_72(0x1, 0x4)
    Sleep(60)
    OP_71(0x1, 0x4)
    Sleep(50)
    OP_72(0x1, 0x4)
    Sleep(1000)

    ChrTalk(    #37
        0x107,
        "#560F#4POkay, that should do it.\x02",
    )

    CloseMessageWindow()
    OP_8F(0x107, 0x309BC, 0x1E, 0xFFFFA4DE, 0x7D0, 0x0)
    OP_8C(0x107, 180, 400)
    ClearChrFlags(0x107, 0x4)

    ChrTalk(    #38
        0x107,
        "#061F#3PSorry it took so long.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#501FWooow, color me impressed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#019FWell, if she's an apprentice\x01",
            "at the central factory, she\x01",
            "has to be good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x107,
        (
            "#067F#3PHee hee... Well, I didn't\x01",
            "do anything special.\x02\x03",

            "I just fixed the quartz connection and adjusted\x01",
            "the orbal pressure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#505F???\x02\x03",

            "Well, it sure SOUNDS special...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x107,
        (
            "#560F#3PIt's not that big a deal...\x02\x03",

            "Umm... Okay, how to explain this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x107,
        (
            "#1K#1PEach orbment has a quartz circuit inside,\x01",
            "and if that isn't properly connected, the orbal\x01",
            "energy inside the unit will have nowhere to go.\x01",
            "As a result, the orbment won't be able to\x01",
            "function properly. This happens sometimes with\x01",
            "the highway lights, which means their ability\x01",
            "to give out light and ward off monsters is\x01",
            "compromised, so--\x02",
        )
    )

    Sleep(2000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #45
        0x101,
        "#1K#004FS-Stop!\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #46
        0x101,
        (
            "#506FM-Maybe you should save\x01",
            "the explanation for after\x01",
            "we get on the road...\x02\x03",

            "I mean, if we stand around too\x01",
            "long...the monsters...you know...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x107,
        (
            "#067F#3PYeah, I guess so...\x01",
            "I was just warming up, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#007F(Whew... )\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#019FHa ha. Well, why don't we\x01",
            "set out for Zeiss, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#006FOkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x107,
        "#061F#3PYes, sir!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    OP_64(0x0, 0x1)
    EventEnd(0x0)

    label("loc_1E51")

    Return()

    # Function_4_637 end

    def Function_5_1E52(): pass

    label("Function_5_1E52")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #52
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "[Rest]\x01",       # 0
            "[Leave]\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2071")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 285640, 1000, -26290, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_73(0x11)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 285640, 1000, -26290, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 285600, 30, -28390, 13)
    SetChrPos(0x1, 285600, 30, -28390, 13)
    SetChrPos(0x2, 285600, 30, -28390, 13)
    SetChrPos(0x3, 285600, 30, -28390, 13)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 285640, 1000, -26290, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2071")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_208B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_208B")

    Return()

    # Function_5_1E52 end

    SaveToFile()

Try(main)
