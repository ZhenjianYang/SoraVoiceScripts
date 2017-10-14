from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5410   ._SN',
        MapName             = 'Other',
        Location            = 'C5410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60028",
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
        'ヴォーグル570（青）',                  # 9
        'ポートシーカー',                       # 10
        'ポートシーカー',                       # 11
        'ヴォーグル235（赤）',                  # 12
        'ヴォーグル570（青）',                  # 13
        'ポートシーカー',                       # 14
        'ポートシーカー',                       # 15
        'ヴォーグル235（赤）',                  # 16
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12350 ._CH',             # 02
        'ED6_DT29/CH12351 ._CH',             # 03
        'ED6_DT29/CH12580 ._CH',             # 04
        'ED6_DT29/CH12581 ._CH',             # 05
        'ED6_DT29/CH12320 ._CH',             # 06
        'ED6_DT29/CH12321 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12350P._CP',             # 02
        'ED6_DT29/CH12351P._CP',             # 03
        'ED6_DT29/CH12580P._CP',             # 04
        'ED6_DT29/CH12581P._CP',             # 05
        'ED6_DT29/CH12320P._CP',             # 06
        'ED6_DT29/CH12321P._CP',             # 07
    )

    DeclMonster(
        X                   = -64330,
        Z                   = 1000,
        Y                   = 62450,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x424,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -45060,
        Z                   = 0,
        Y                   = 5510,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -125030,
        Z                   = 0,
        Y                   = -45280,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x428,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -113980,
        Z                   = 1000,
        Y                   = -111570,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x427,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -64330,
        Z                   = 1000,
        Y                   = 62450,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x42D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -45060,
        Z                   = 0,
        Y                   = 5510,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -125030,
        Z                   = 0,
        Y                   = -45280,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x431,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -113980,
        Z                   = 1000,
        Y                   = -111570,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x430,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -127440,
        Y                   = 0,
        Z                   = -25200,
        Range               = -122190,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF8F80,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -127660,
        Y                   = 0,
        Z                   = -57300,
        Range               = -122030,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF13AC,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -92800,
        Y                   = 0,
        Z                   = -166990,
        Range               = -89100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFD919E,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -81710,
        TriggerZ            = 0,
        TriggerY            = -17950,
        TriggerRange        = 1000,
        ActorX              = -81000,
        ActorZ              = 0,
        ActorY              = -18020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_24F",          # 01, 1
        "Function_2_2C2",          # 02, 2
        "Function_3_445",          # 03, 3
        "Function_4_4F2",          # 04, 4
        "Function_5_533",          # 05, 5
        "Function_6_574",          # 06, 6
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Return()

    # Function_0_24E end

    def Function_1_24F(): pass

    label("Function_1_24F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F")
    OP_6F(0x13, 0)
    Jump("loc_286")

    label("loc_27F")

    OP_6F(0x13, 60)

    label("loc_286")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_2BD")

    label("loc_2A9")

    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_2BD")

    Call(0, 3)
    Return()

    # Function_1_24F end

    def Function_2_2C2(): pass

    label("Function_2_2C2")

    OP_EA(0x2, 0x7F, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x145, 1)"), scpexpr(EXPR_END)), "loc_333")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x45\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D3A)
    Jump("loc_397")

    label("loc_333")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x45\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x45\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_397")

    Jump("loc_437")

    label("loc_39A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You don't understand how hard it is to come up\x01",
            "with five hundred unique treasure chest phrases\x01",
            "that are brimming with sarcasm.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_437")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2C2 end

    def Function_3_445(): pass

    label("Function_3_445")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_452")
    Return()

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 6)), scpexpr(EXPR_END)), "loc_487")
    OP_6F(0x0, 100)
    OP_72(0x0, 0x2)
    OP_BE(0x0, 0x1, 0x2, 0x64, 0x0, 0x2, -127510, -1000, -25720, -122680, 2000, -28500)

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 7)), scpexpr(EXPR_END)), "loc_4BC")
    OP_6F(0x1, 100)
    OP_72(0x1, 0x2)
    OP_BE(0x1, 0x1, 0x2, 0x64, 0x0, 0x2, -127750, -1000, -57600, -122480, 2000, -60300)

    label("loc_4BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x395, 0)), scpexpr(EXPR_END)), "loc_4F1")
    OP_6F(0x2, 100)
    OP_72(0x2, 0x2)
    OP_BE(0x2, 0x1, 0x2, 0x64, 0x0, 0x2, -92500, -1000, -167010, -89100, 2000, -159530)

    label("loc_4F1")

    Return()

    # Function_3_445 end

    def Function_4_4F2(): pass

    label("Function_4_4F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4FF")
    Return()

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 6)), scpexpr(EXPR_END)), "loc_507")
    Return()

    label("loc_507")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x64)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x0)
    OP_A2(0x1CA6)
    Call(0, 3)
    EventEnd(0x3)
    Return()

    # Function_4_4F2 end

    def Function_5_533(): pass

    label("Function_5_533")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_540")
    Return()

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x394, 7)), scpexpr(EXPR_END)), "loc_548")
    Return()

    label("loc_548")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x1CA7)
    Call(0, 3)
    EventEnd(0x3)
    Return()

    # Function_5_533 end

    def Function_6_574(): pass

    label("Function_6_574")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_581")
    Return()

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x395, 0)), scpexpr(EXPR_END)), "loc_589")
    Return()

    label("loc_589")

    EventBegin(0x2)
    OP_22(0x6B, 0x0, 0x64)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x64)
    Sleep(900)
    OP_22(0x9D, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x1CA8)
    Call(0, 3)
    EventEnd(0x3)
    Return()

    # Function_6_574 end

    SaveToFile()

Try(main)
