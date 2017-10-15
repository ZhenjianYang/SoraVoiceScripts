from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5306   ._SN',
        MapName             = 'Other',
        Location            = 'C5306.x',
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
        'エレベータ',                           # 9
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
        'ED6_DT29/CH12300 ._CH',             # 0A
        'ED6_DT29/CH12301 ._CH',             # 0B
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
        'ED6_DT29/CH12300P._CP',             # 0A
        'ED6_DT29/CH12301P._CP',             # 0B
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
        X                   = 91640,
        Z                   = 0,
        Y                   = -72910,
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
        X                   = -76800,
        Z                   = 0,
        Y                   = -90840,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94600,
        Z                   = 0,
        Y                   = -73000,
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
        X                   = -87930,
        Z                   = 0,
        Y                   = 96320,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 100070,
        Y                   = -2000,
        Z                   = 9020,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = 5140,
        Y                   = -2000,
        Z                   = 110030,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = -10520,
        TriggerZ            = 0,
        TriggerY            = -90700,
        TriggerRange        = 1000,
        ActorX              = -10490,
        ActorZ              = 0,
        ActorY              = -90090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9460,
        TriggerZ            = 0,
        TriggerY            = -90710,
        TriggerRange        = 1000,
        ActorX              = 9490,
        ActorZ              = 0,
        ActorY              = -90050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9550,
        TriggerZ            = 0,
        TriggerY            = -95300,
        TriggerRange        = 1000,
        ActorX              = 9520,
        ActorZ              = 0,
        ActorY              = -95870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10520,
        TriggerZ            = 0,
        TriggerY            = -95300,
        TriggerRange        = 1000,
        ActorX              = -10470,
        ActorZ              = 0,
        ActorY              = -96000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_2EC",          # 01, 1
        "Function_2_42B",          # 02, 2
        "Function_3_567",          # 03, 3
        "Function_4_6D5",          # 04, 4
        "Function_5_810",          # 05, 5
        "Function_6_971",          # 06, 6
        "Function_7_A88",          # 07, 7
        "Function_8_BB5",          # 08, 8
        "Function_9_D51",          # 09, 9
        "Function_10_F40",         # 0A, 10
        "Function_11_118C",        # 0B, 11
        "Function_12_1288",        # 0C, 12
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_27B")
    OP_A3(0x10F0)
    Event(0, 6)
    Jump("loc_2A4")

    label("loc_27B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_28F"),
        (122, "loc_296"),
        (111, "loc_29D"),
        (SWITCH_DEFAULT, "loc_2A4"),
    )


    label("loc_28F")

    Event(0, 8)
    Jump("loc_2A4")

    label("loc_296")

    Event(0, 10)
    Jump("loc_2A4")

    label("loc_29D")

    Event(0, 12)
    Jump("loc_2A4")

    label("loc_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_END)), "loc_2EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB")
    OP_A2(0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_2EB")

    Return()

    # Function_0_26A end

    def Function_1_2EC(): pass

    label("Function_1_2EC")

    OP_51(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F")
    OP_6F(0x3, 0)
    Jump("loc_326")

    label("loc_31F")

    OP_6F(0x3, 60)

    label("loc_326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338")
    OP_6F(0x4, 0)
    Jump("loc_33F")

    label("loc_338")

    OP_6F(0x4, 60)

    label("loc_33F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_351")
    OP_6F(0x5, 0)
    Jump("loc_358")

    label("loc_351")

    OP_6F(0x5, 60)

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A")
    OP_6F(0x6, 0)
    Jump("loc_371")

    label("loc_36A")

    OP_6F(0x6, 60)

    label("loc_371")

    OP_10(0x0, 0x0)
    OP_10(0x16, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x88, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 0)
    OP_10(0xB, 0x0)
    Jump("loc_3ED")

    label("loc_39C")

    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 600)
    OP_10(0xB, 0x1)
    OP_82(0x83, 0x0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_1B(0xB, 0x0, 0xB)

    label("loc_3ED")

    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_6F(0x2, 0)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 5140, -1750, 110030, 90)
    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_2EC end

    def Function_2_42B(): pass

    label("Function_2_42B")

    OP_EA(0x2, 0x48, 0x1, 0x0)
    OP_EA(0x2, 0xF, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_508")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x167, 1)"), scpexpr(EXPR_END)), "loc_4A1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x67\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x238B)
    Jump("loc_505")

    label("loc_4A1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x67\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x67\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_505")

    Jump("loc_559")

    label("loc_508")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Mind doing me a favor and not opening me up\x01",
            "again?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_559")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_42B end

    def Function_3_567(): pass

    label("Function_3_567")

    OP_EA(0x2, 0x49, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_5D8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x06\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x238D)
    Jump("loc_63C")

    label("loc_5D8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x06\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x06\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_63C")

    Jump("loc_6C7")

    label("loc_63F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Inside the empty chest is carved:\x01",
            "'Olivier is handsome.'\x01",
            "You briefly wonder if he put that there himself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6C7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_567 end

    def Function_4_6D5(): pass

    label("Function_4_6D5")

    OP_EA(0x2, 0x4A, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_746")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x238E)
    Jump("loc_7AA")

    label("loc_746")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_7AA")

    Jump("loc_802")

    label("loc_7AD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Nothing. Well, life is full of little disappointments.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_802")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6D5 end

    def Function_5_810(): pass

    label("Function_5_810")

    OP_EA(0x2, 0x4B, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x471, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_881")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x238F)
    Jump("loc_8E5")

    label("loc_881")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_8E5")

    Jump("loc_963")

    label("loc_8E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05Hey, you. Yeah, you. Stop reading all these chest\x01",
            "messages and get on with playing the game!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_963")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_810 end

    def Function_6_971(): pass

    label("Function_6_971")

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
    OP_6F(0x1, 0)
    OP_70(0x1, 0x258)
    Sleep(1500)
    OP_22(0xE1, 0x0, 0x64)
    Sleep(3000)
    OP_22(0x70, 0x0, 0x64)
    OP_73(0x1)

    def lambda_9F9():
        OP_6D(-88930, 1090, 4140, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F9)

    def lambda_A11():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A11)
    OP_6C(315000, 5000)
    Fade(1000)
    OP_22(0xD7, 0x0, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_971 end

    def Function_7_A88(): pass

    label("Function_7_A88")

    EventBegin(0x0)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100070, -1750, 9020, 0)
    OP_48()
    Fade(1000)
    OP_6D(100070, 0, 9020, 0)
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

    def lambda_B3D():
        OP_67(0, 6500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B3D)

    def lambda_B55():
        OP_6B(3700, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B55)

    def lambda_B65():
        OP_91(0xFE, 0x0, 0xFFFFD8F0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B65)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A2(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_A88 end

    def Function_8_BB5(): pass

    label("Function_8_BB5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, 100070, -11750, 9020, 0)
    OP_48()
    OP_6D(100070, 0, 9020, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 100000, 0, 10000, 0)
    OP_89(0x1, 101000, 0, 9000, 90)
    OP_89(0x2, 99000, 0, 9000, 270)
    OP_89(0x3, 100000, 0, 8000, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_C64():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C64)
    FadeToBright(1000, 0)
    SetPlaceName(0x120)

    def lambda_C80():
        OP_91(0xFE, 0x0, 0x2710, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C80)
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
    SetChrPos(0x0, 100080, 0, 4460, 180)
    SetChrPos(0x1, 100080, 0, 4460, 180)
    SetChrPos(0x2, 100080, 0, 4460, 180)
    SetChrPos(0x3, 100080, 0, 4460, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_8_BB5 end

    def Function_9_D51(): pass

    label("Function_9_D51")

    EventBegin(0x0)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 5140, -1750, 110030, 90)
    OP_48()
    Fade(1000)
    OP_6D(5140, 0, 110030, 0)
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

    def lambda_E01():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E01)
    Sleep(500)

    def lambda_E21():
        OP_6D(5140, 35000, 110030, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E21)

    def lambda_E39():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E39)

    def lambda_E51():
        OP_6C(295000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E51)
    Sleep(500)

    def lambda_E66():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E66)
    Sleep(500)

    def lambda_E86():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E86)
    Sleep(400)

    def lambda_EA6():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EA6)
    Sleep(200)

    def lambda_EC6():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EC6)
    Sleep(100)

    def lambda_EE6():
        OP_8F(0xFE, 0x1414, 0xFDE8, 0x1ADCE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EE6)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A2(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5316   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_D51 end

    def Function_10_F40(): pass

    label("Function_10_F40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0x8, 0x2)
    SetChrPos(0x8, 5140, 66000, 110030, 90)
    OP_48()
    OP_6D(5140, 48000, 110030, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(295000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 5000, 67000, 111000, 0)
    OP_89(0x1, 6000, 67000, 110000, 90)
    OP_89(0x2, 4000, 67000, 110000, 270)
    OP_89(0x3, 5000, 67000, 109000, 180)
    OP_22(0xEB, 0x1, 0x64)

    def lambda_FEF():
        OP_6D(5140, 0, 110030, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FEF)

    def lambda_1007():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1007)

    def lambda_101F():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_101F)
    FadeToBright(1000, 0)
    SetPlaceName(0x120)

    def lambda_103B():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_103B)
    Sleep(7800)

    def lambda_105B():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_105B)
    Sleep(700)

    def lambda_107B():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_107B)
    Sleep(600)

    def lambda_109B():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_109B)
    Sleep(100)

    def lambda_10BB():
        OP_8F(0xFE, 0x1414, 0xFFFFF92A, 0x1ADCE, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10BB)
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
    SetChrPos(0x0, 160, 0, 109620, 270)
    SetChrPos(0x1, 160, 0, 109620, 270)
    SetChrPos(0x2, 160, 0, 109620, 270)
    SetChrPos(0x3, 160, 0, 109620, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_10_F40 end

    def Function_11_118C(): pass

    label("Function_11_118C")

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

    def lambda_1237():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1237)

    def lambda_1249():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1249)

    def lambda_125B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_125B)

    def lambda_126D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_126D)
    Sleep(2000)
    NewScene("ED6_DT21/C5300   ._SN", 122, 0, 0)
    IdleLoop()
    Return()

    # Function_11_118C end

    def Function_12_1288(): pass

    label("Function_12_1288")

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

    def lambda_1363():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1363)

    def lambda_1375():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1375)

    def lambda_1387():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1387)

    def lambda_1399():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1399)
    Sleep(2500)
    Fade(500)
    OP_6D(-92500, 0, 4000, 0)
    SetChrPos(0x0, -92500, 0, 4000, 270)
    SetChrPos(0x1, -92500, 0, 4000, 270)
    SetChrPos(0x2, -92500, 0, 4000, 270)
    SetChrPos(0x3, -92500, 0, 4000, 270)
    EventEnd(0x0)
    Return()

    # Function_12_1288 end

    SaveToFile()

Try(main)
