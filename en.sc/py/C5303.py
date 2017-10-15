from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5303   ._SN',
        MapName             = 'Other',
        Location            = 'C5303.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        'Elevator',                             # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH12010 ._CH',             # 00
        'ED6_DT29/CH12010 ._CH',             # 01
        'ED6_DT29/CH12080 ._CH',             # 02
        'ED6_DT29/CH12081 ._CH',             # 03
        'ED6_DT29/CH12050 ._CH',             # 04
        'ED6_DT29/CH12051 ._CH',             # 05
        'ED6_DT29/CH12140 ._CH',             # 06
        'ED6_DT29/CH12141 ._CH',             # 07
        'ED6_DT29/CH12420 ._CH',             # 08
        'ED6_DT29/CH12421 ._CH',             # 09
        'ED6_DT29/CH12340 ._CH',             # 0A
        'ED6_DT29/CH12341 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH12010P._CP',             # 00
        'ED6_DT29/CH12010P._CP',             # 01
        'ED6_DT29/CH12080P._CP',             # 02
        'ED6_DT29/CH12081P._CP',             # 03
        'ED6_DT29/CH12050P._CP',             # 04
        'ED6_DT29/CH12051P._CP',             # 05
        'ED6_DT29/CH12140P._CP',             # 06
        'ED6_DT29/CH12141P._CP',             # 07
        'ED6_DT29/CH12420P._CP',             # 08
        'ED6_DT29/CH12421P._CP',             # 09
        'ED6_DT29/CH12340P._CP',             # 0A
        'ED6_DT29/CH12341P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 91440,
        Z                   = 0,
        Y                   = -73190,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 73490,
        Z                   = 0,
        Y                   = -91400,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x528,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -76640,
        Z                   = 0,
        Y                   = -90640,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94840,
        Z                   = 0,
        Y                   = -72560,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x530,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -97730,
        Z                   = 0,
        Y                   = 87090,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x529,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -79380,
        Z                   = 0,
        Y                   = 104930,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 100010,
        Y                   = -2000,
        Z                   = 9030,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = 5130,
        Y                   = -2000,
        Z                   = 110010,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -10540,
        TriggerZ            = 0,
        TriggerY            = -90650,
        TriggerRange        = 1000,
        ActorX              = -10500,
        ActorZ              = 0,
        ActorY              = -90040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9500,
        TriggerZ            = 0,
        TriggerY            = -90660,
        TriggerRange        = 1000,
        ActorX              = 9520,
        ActorZ              = 0,
        ActorY              = -89950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9500,
        TriggerZ            = 0,
        TriggerY            = -95340,
        TriggerRange        = 1000,
        ActorX              = 9520,
        ActorZ              = 0,
        ActorY              = -96050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10460,
        TriggerZ            = 0,
        TriggerY            = -95340,
        TriggerRange        = 1000,
        ActorX              = -10500,
        ActorZ              = 0,
        ActorY              = -96000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A2",          # 00, 0
        "Function_1_324",          # 01, 1
        "Function_2_44D",          # 02, 2
        "Function_3_5A9",          # 03, 3
        "Function_4_736",          # 04, 4
        "Function_5_883",          # 05, 5
        "Function_6_A14",          # 06, 6
        "Function_7_B2B",          # 07, 7
        "Function_8_C58",          # 08, 8
        "Function_9_DF4",          # 09, 9
        "Function_10_FE3",         # 0A, 10
        "Function_11_122F",        # 0B, 11
        "Function_12_132B",        # 0C, 12
    )


    def Function_0_2A2(): pass

    label("Function_0_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2B3")
    OP_A3(0x10F0)
    Event(0, 6)
    Jump("loc_2DC")

    label("loc_2B3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2C7"),
        (114, "loc_2CE"),
        (116, "loc_2D5"),
        (SWITCH_DEFAULT, "loc_2DC"),
    )


    label("loc_2C7")

    Event(0, 8)
    Jump("loc_2DC")

    label("loc_2CE")

    Event(0, 10)
    Jump("loc_2DC")

    label("loc_2D5")

    Event(0, 12)
    Jump("loc_2DC")

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 6)), scpexpr(EXPR_END)), "loc_323")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323")
    OP_A2(0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_323")

    Return()

    # Function_0_2A2 end

    def Function_1_324(): pass

    label("Function_1_324")

    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357")
    OP_6F(0x3, 0)
    Jump("loc_35E")

    label("loc_357")

    OP_6F(0x3, 60)

    label("loc_35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370")
    OP_6F(0x4, 0)
    Jump("loc_377")

    label("loc_370")

    OP_6F(0x4, 60)

    label("loc_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_389")
    OP_6F(0x5, 0)
    Jump("loc_390")

    label("loc_389")

    OP_6F(0x5, 60)

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2")
    OP_6F(0x6, 0)
    Jump("loc_3A9")

    label("loc_3A2")

    OP_6F(0x6, 60)

    label("loc_3A9")

    OP_10(0x0, 0x0)
    OP_10(0xE, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x88, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D4")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_10(0x10, 0x0)
    Jump("loc_425")

    label("loc_3D4")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 600)
    OP_10(0x10, 0x1)
    OP_82(0x83, 0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_1B(0x10, 0x0, 0xB)

    label("loc_425")

    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_324 end

    def Function_2_44D(): pass

    label("Function_2_44D")

    OP_EA(0x2, 0x38, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_525")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_4BE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x06\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2376)
    Jump("loc_522")

    label("loc_4BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x06\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x06\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_522")

    Jump("loc_59B")

    label("loc_525")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You briefly wonder how many jelly beans you\x01",
            "could fit in a treasure chest of this size.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_59B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_44D end

    def Function_3_5A9(): pass

    label("Function_3_5A9")

    OP_EA(0x2, 0x39, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_61A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2378)
    Jump("loc_67E")

    label("loc_61A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_67E")

    Jump("loc_728")

    label("loc_681")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Remember the stuff you took from here last time?\x01",
            "Yeah, the chest was TRYING to afford chest college.\x01",
            "Guess it has to start over again...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_728")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5A9 end

    def Function_4_736(): pass

    label("Function_4_736")

    OP_EA(0x2, 0x3A, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_7A7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xFD\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2379)
    Jump("loc_80B")

    label("loc_7A7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xFD\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFD\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_80B")

    Jump("loc_875")

    label("loc_80E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05You obtain the Sword of the Ancient\x01",
            "God-Kings. Just kidding, it's empty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_875")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_736 end

    def Function_5_883(): pass

    label("Function_5_883")

    OP_EA(0x2, 0x3B, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_8F4")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\xFB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x237A)
    Jump("loc_958")

    label("loc_8F4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\xFB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_958")

    Jump("loc_A06")

    label("loc_95B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05You wonder if you could use arts to turn this\x01",
            "chest into a small, wooden bathtub. Water would\x01",
            "probably be fine. Fire to heat it, likely not.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A06")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_883 end

    def Function_6_A14(): pass

    label("Function_6_A14")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-97890, 0, 32369, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(345000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)
    Sleep(1500)
    OP_22(0xE1, 0x0, 0x64)
    Sleep(3000)
    OP_22(0x70, 0x0, 0x64)
    OP_73(0x0)

    def lambda_A9C():
        OP_6D(-88930, 1090, 4140, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A9C)

    def lambda_AB4():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AB4)
    OP_6C(315000, 5000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5309   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_A14 end

    def Function_7_B2B(): pass

    label("Function_7_B2B")

    EventBegin(0x0)
    OP_A1(0x8, 0x1)
    SetChrPos(0x8, 100010, -1750, 9030, 0)
    OP_48()
    Fade(1000)
    OP_6D(100010, 0, 9030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 0, 10000, 0)
    OP_89(0x1, 101000, 0, 9000, 90)
    OP_89(0x2, 99000, 0, 9000, 270)
    OP_89(0x3, 100000, 0, 8000, 180)
    OP_0D()
    Sleep(300)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_BE0():
        OP_67(0, 6500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE0)

    def lambda_BF8():
        OP_6B(3700, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF8)

    def lambda_C08():
        OP_91(0xFE, 0x0, 0xFFFFD8F0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C08)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A2(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_B2B end

    def Function_8_C58(): pass

    label("Function_8_C58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x1)
    SetChrPos(0x8, 100010, -11750, 9030, 0)
    OP_48()
    OP_6D(100010, 0, 9030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 0, 10000, 0)
    OP_89(0x1, 101000, 0, 9000, 90)
    OP_89(0x2, 99000, 0, 9000, 270)
    OP_89(0x3, 100000, 0, 8000, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_D07():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D07)
    FadeToBright(1000, 0)
    SetPlaceName(0x11E)

    def lambda_D23():
        OP_91(0xFE, 0x0, 0x2710, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D23)
    Sleep(2200)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 100220, 0, 4340, 180)
    SetChrPos(0x1, 100220, 0, 4340, 180)
    SetChrPos(0x2, 100220, 0, 4340, 180)
    SetChrPos(0x3, 100220, 0, 4340, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_8_C58 end

    def Function_9_DF4(): pass

    label("Function_9_DF4")

    EventBegin(0x0)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 5130, -1750, 110010, 90)
    OP_48()
    Fade(1000)
    OP_6D(5130, 0, 110010, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 5000, 0, 111000, 0)
    OP_89(0x1, 6000, 0, 110000, 90)
    OP_89(0x2, 4000, 0, 110000, 270)
    OP_89(0x3, 5000, 0, 109000, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x1, 0x64)

    def lambda_EA4():
        OP_8F(0xFE, 0x140A, 0xFDE8, 0x1ADBA, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EA4)
    Sleep(500)

    def lambda_EC4():
        OP_6D(5130, 35000, 110010, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EC4)

    def lambda_EDC():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EDC)

    def lambda_EF4():
        OP_6C(295000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EF4)
    Sleep(500)

    def lambda_F09():
        OP_8F(0xFE, 0x140A, 0xFDE8, 0x1ADBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F09)
    Sleep(500)

    def lambda_F29():
        OP_8F(0xFE, 0x140A, 0xFDE8, 0x1ADBA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F29)
    Sleep(400)

    def lambda_F49():
        OP_8F(0xFE, 0x140A, 0xFDE8, 0x1ADBA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F49)
    Sleep(200)

    def lambda_F69():
        OP_8F(0xFE, 0x140A, 0xFDE8, 0x1ADBA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F69)
    Sleep(100)

    def lambda_F89():
        OP_8F(0xFE, 0x140A, 0xFDE8, 0x1ADBA, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F89)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A2(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_DF4 end

    def Function_10_FE3(): pass

    label("Function_10_FE3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 5130, 66000, 110010, 90)
    OP_48()
    OP_6D(5130, 48000, 110010, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(295000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 5000, 67000, 111000, 0)
    OP_89(0x1, 6000, 67000, 110000, 90)
    OP_89(0x2, 4000, 67000, 110000, 270)
    OP_89(0x3, 5000, 67000, 109000, 180)
    OP_22(0xEB, 0x1, 0x64)

    def lambda_1092():
        OP_6D(5130, 0, 110010, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1092)

    def lambda_10AA():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10AA)

    def lambda_10C2():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10C2)
    FadeToBright(1000, 0)
    SetPlaceName(0x11E)

    def lambda_10DE():
        OP_8F(0xFE, 0x140A, 0xFFFFF92A, 0x1ADBA, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10DE)
    Sleep(7800)

    def lambda_10FE():
        OP_8F(0xFE, 0x140A, 0xFFFFF92A, 0x1ADBA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10FE)
    Sleep(700)

    def lambda_111E():
        OP_8F(0xFE, 0x140A, 0xFFFFF92A, 0x1ADBA, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_111E)
    Sleep(600)

    def lambda_113E():
        OP_8F(0xFE, 0x140A, 0xFFFFF92A, 0x1ADBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_113E)
    Sleep(100)

    def lambda_115E():
        OP_8F(0xFE, 0x140A, 0xFFFFF92A, 0x1ADBA, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_115E)
    Sleep(500)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 190, 0, 109990, 270)
    SetChrPos(0x1, 190, 0, 109990, 270)
    SetChrPos(0x2, 190, 0, 109990, 270)
    SetChrPos(0x3, 190, 0, 109990, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_10_FE3 end

    def Function_11_122F(): pass

    label("Function_11_122F")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-89000, 1050, 4000, 0)
    SetChrPos(0x101, -88500, 1050, 4500, 90)
    SetChrPos(0x102, -88500, 1050, 3500, 90)
    SetChrPos(0xF8, -89500, 1050, 4500, 90)
    SetChrPos(0xF9, -89500, 1050, 3500, 90)
    OP_0D()
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_12DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_12DA)

    def lambda_12EC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_12EC)

    def lambda_12FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_12FE)

    def lambda_1310():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1310)
    Sleep(2000)
    NewScene("ED6_DT21/C5300   ._SN", 122, 0, 0)
    IdleLoop()
    Return()

    # Function_11_122F end

    def Function_12_132B(): pass

    label("Function_12_132B")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-89000, 1050, 4000, 0)
    SetChrPos(0x101, -89500, 1050, 3500, 270)
    SetChrPos(0x102, -89500, 1050, 4500, 270)
    SetChrPos(0xF8, -88500, 1050, 3500, 270)
    SetChrPos(0xF9, -88500, 1050, 4500, 270)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_1406():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1406)

    def lambda_1418():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1418)

    def lambda_142A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_142A)

    def lambda_143C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_143C)
    Sleep(2500)
    Fade(500)
    OP_6D(-92500, 0, 4000, 0)
    SetChrPos(0x0, -92500, 0, 4000, 270)
    SetChrPos(0x1, -92500, 0, 4000, 270)
    SetChrPos(0x2, -92500, 0, 4000, 270)
    SetChrPos(0x3, -92500, 0, 4000, 270)
    EventEnd(0x0)
    Return()

    # Function_12_132B end

    SaveToFile()

Try(main)
