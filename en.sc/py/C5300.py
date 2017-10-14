from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5300   ._SN',
        MapName             = 'Other',
        Location            = 'C5300.x',
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
        'Weissmann',                            # 9
        'Campanella',                           # 10
        'Father Kevin',                         # 11
        'エレベータ',                           # 12
        'ワイスマンの杖',                       # 13
        '地震制御用ダミーキャラ',               # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
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
        'ED6_DT29/CH12280 ._CH',             # 0A
        'ED6_DT29/CH12281 ._CH',             # 0B
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
        'ED6_DT29/CH12280P._CP',             # 0A
        'ED6_DT29/CH12281P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x1C5,
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


    DeclMonster(
        X                   = -76830,
        Z                   = 0,
        Y                   = -90660,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -94910,
        Z                   = 0,
        Y                   = -72500,
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
        X                   = -100110,
        Z                   = 0,
        Y                   = 15090,
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
        X                   = -87500,
        Z                   = 0,
        Y                   = 96820,
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
        X                   = 81290,
        Z                   = 0,
        Y                   = 102460,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 99160,
        Z                   = 0,
        Y                   = 84400,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x52A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 102030,
        Y                   = -2000,
        Z                   = 1000,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 13,
    )


    DeclActor(
        TriggerX            = 20,
        TriggerZ            = 0,
        TriggerY            = -83640,
        TriggerRange        = 1000,
        ActorX              = 50,
        ActorZ              = 0,
        ActorY              = -82980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2550,
        TriggerZ            = 0,
        TriggerY            = -83650,
        TriggerRange        = 1000,
        ActorX              = -2520,
        ActorZ              = 0,
        ActorY              = -83030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2450,
        TriggerZ            = 0,
        TriggerY            = -83650,
        TriggerRange        = 1000,
        ActorX              = 2480,
        ActorZ              = 0,
        ActorY              = -82990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10350,
        TriggerZ            = 0,
        TriggerY            = -94070,
        TriggerRange        = 1000,
        ActorX              = 11050,
        ActorZ              = 0,
        ActorY              = -94030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10350,
        TriggerZ            = 0,
        TriggerY            = -96660,
        TriggerRange        = 1000,
        ActorX              = 10970,
        ActorZ              = 0,
        ActorY              = -96630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 10350,
        TriggerZ            = 0,
        TriggerY            = -91550,
        TriggerRange        = 1000,
        ActorX              = 11060,
        ActorZ              = 0,
        ActorY              = -91560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_36A",          # 00, 0
        "Function_1_3C8",          # 01, 1
        "Function_2_511",          # 02, 2
        "Function_3_64C",          # 03, 3
        "Function_4_794",          # 04, 4
        "Function_5_902",          # 05, 5
        "Function_6_A36",          # 06, 6
        "Function_7_B7F",          # 07, 7
        "Function_8_CC0",          # 08, 8
        "Function_9_146A",         # 09, 9
        "Function_10_2BE9",        # 0A, 10
        "Function_11_2C22",        # 0B, 11
        "Function_12_2C6A",        # 0C, 12
        "Function_13_2CB9",        # 0D, 13
        "Function_14_2EA8",        # 0E, 14
        "Function_15_30F9",        # 0F, 15
        "Function_16_3278",        # 10, 16
        "Function_17_357B",        # 11, 17
        "Function_18_3601",        # 12, 18
    )


    def Function_0_36A(): pass

    label("Function_0_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_384")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 9)
    Jump("loc_3C7")

    label("loc_384")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397")
    Event(0, 14)
    Jump("loc_3C7")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B4")
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_3C7")

    label("loc_3B4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (122, "loc_3C0"),
        (SWITCH_DEFAULT, "loc_3C7"),
    )


    label("loc_3C0")

    Event(0, 15)
    Jump("loc_3C7")

    label("loc_3C7")

    Return()

    # Function_0_36A end

    def Function_1_3C8(): pass

    label("Function_1_3C8")

    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406")
    OP_6F(0x1, 0)
    Jump("loc_40D")

    label("loc_406")

    OP_6F(0x1, 60)

    label("loc_40D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41F")
    OP_6F(0x2, 0)
    Jump("loc_426")

    label("loc_41F")

    OP_6F(0x2, 60)

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_438")
    OP_6F(0x3, 0)
    Jump("loc_43F")

    label("loc_438")

    OP_6F(0x3, 60)

    label("loc_43F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_451")
    OP_6F(0x4, 0)
    Jump("loc_458")

    label("loc_451")

    OP_6F(0x4, 60)

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46A")
    OP_6F(0x5, 0)
    Jump("loc_471")

    label("loc_46A")

    OP_6F(0x5, 60)

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483")
    OP_6F(0x6, 0)
    Jump("loc_48A")

    label("loc_483")

    OP_6F(0x6, 60)

    label("loc_48A")

    OP_E0(0x1, 0x14, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C, 0xB8, 0xFE, 0xFF)
    OP_E0(0x2, 0xA, 0xF6, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0, 0x1C, 0xB8, 0xFE, 0xFF)
    OP_E0(0x3, 0x92, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x12, 0xB8, 0xFE, 0xFF)
    OP_E0(0x4, 0x4, 0x29, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x8A, 0x90, 0xFE, 0xFF)
    OP_E0(0x5, 0x4, 0x29, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x6C, 0x86, 0xFE, 0xFF)
    OP_E0(0x6, 0x4, 0x29, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x62, 0x9A, 0xFE, 0xFF)
    OP_10(0x13, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_505")
    OP_10(0x16, 0x1)
    OP_1B(0x16, 0x0, 0x10)
    Jump("loc_50B")

    label("loc_505")

    OP_10(0x16, 0x0)
    OP_82(0x83, 0x0)

    label("loc_50B")

    OP_22(0x140, 0x0, 0x64)
    Return()

    # Function_1_3C8 end

    def Function_2_511(): pass

    label("Function_2_511")

    OP_EA(0x2, 0x2A, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x154, 1)"), scpexpr(EXPR_END)), "loc_582")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x54\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2364)
    Jump("loc_5E6")

    label("loc_582")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x54\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x54\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_5E6")

    Jump("loc_63E")

    label("loc_5E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Nothing. Well, life is full of little disappointments.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_63E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_511 end

    def Function_3_64C(): pass

    label("Function_3_64C")

    OP_EA(0x2, 0x2B, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_724")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_6BD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xF7\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2366)
    Jump("loc_721")

    label("loc_6BD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xF7\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF7\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_721")

    Jump("loc_786")

    label("loc_724")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Oh, no, it's a Mimic! Prepare for battle!\x01",
            "...Wait. No? False alarm.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_786")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_64C end

    def Function_4_794(): pass

    label("Function_4_794")

    OP_EA(0x2, 0x2C, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_805")
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
    OP_A2(0x2367)
    Jump("loc_869")

    label("loc_805")

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
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_869")

    Jump("loc_8F4")

    label("loc_86C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05I'll have you know that if you could take\x01",
            "multiple items from the same chest, the\x01",
            "economy would collapse.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_8F4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_794 end

    def Function_5_902(): pass

    label("Function_5_902")

    OP_EA(0x2, 0x2D, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_973")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "Found \x1F\x04\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2368)
    Jump("loc_9D7")

    label("loc_973")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "Found \x1F\x04\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x04\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_9D7")

    Jump("loc_A28")

    label("loc_9DA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Nothing in here but a couple of hairs. Gross...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A28")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_902 end

    def Function_6_A36(): pass

    label("Function_6_A36")

    OP_EA(0x2, 0x2E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_AA7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2369)
    Jump("loc_B0B")

    label("loc_AA7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_B0B")

    Jump("loc_B71")

    label("loc_B0E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05I had saved some coffee for you, but then it was\x01",
            "taken in a mugging.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B71")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_A36 end

    def Function_7_B7F(): pass

    label("Function_7_B7F")

    OP_EA(0x2, 0x2F, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x140, 1)"), scpexpr(EXPR_END)), "loc_BF0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\x40\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x236A)
    Jump("loc_C54")

    label("loc_BF0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\x40\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x40\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_C54")

    Jump("loc_CB2")

    label("loc_C57")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "\x07\x05How would you like it if some random chest\x01",
            "kept opening you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CB2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B7F end

    def Function_8_CC0(): pass

    label("Function_8_CC0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD7")
    Call(0, 17)
    Call(0, 18)

    label("loc_CD7")

    OP_6D(-1440, 0, -89110, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(171000, 0)
    OP_6E(500, 0)
    SetChrPos(0x101, 450, 0, -129370, 0)
    SetChrPos(0x102, -740, 0, -129490, 0)
    SetChrPos(0xF8, 450, 0, -130590, 0)
    SetChrPos(0xF9, -760, 0, -130850, 0)
    FadeToBright(1000, 0)

    def lambda_D67():
        OP_6D(80, 0, -129160, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D67)

    def lambda_D7F():
        OP_67(0, 6290, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D7F)

    def lambda_D97():
        OP_6C(159000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D97)

    def lambda_DA7():
        OP_6B(1980, 7000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA7)
    OP_C8(0x80, 0x46, "C_PLAC27._CH", 0x1, 0x3E8)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E17")

    ChrTalk(    #18
        0x10B,
        (
            "#212FSo this is the inside of\x01",
            "the Axis Pillar...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_E17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5E")

    ChrTalk(    #19
        0x108,
        (
            "#072FSo this is the inside of\x01",
            "the Axis Pillar...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_E5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA3")

    ChrTalk(    #20
        0x106,
        (
            "#057FSo this what the thing looks\x01",
            "like inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_EA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EFB")

    ChrTalk(    #21
        0x104,
        (
            "#032FHm. So this is what the heart\x01",
            "of the city looks like inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_EFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3F")

    ChrTalk(    #22
        0x110,
        "#270FSo this is the Axis Pillar's interior...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_F3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F90")

    ChrTalk(    #23
        0x109,
        (
            "#1063FWhoaaa. So this is the guts\x01",
            "of the Axis Pillar, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_F90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD9")

    ChrTalk(    #24
        0x103,
        (
            "#022FSo this is the interior of\x01",
            "the Axis Pillar...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_FD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1023")

    ChrTalk(    #25
        0x105,
        (
            "#1163FSo this is the interior of\x01",
            "the Axis Pillar...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1069")

    label("loc_1023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1069")

    ChrTalk(    #26
        0x10F,
        (
            "#172FSo this is the interior of\x01",
            "the Axis Pillar...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1069")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B2")

    ChrTalk(    #27
        0x107,
        (
            "#065FIt's almost like being inside\x01",
            "a huge orbment!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_10B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F6")

    ChrTalk(    #28
        0x10F,
        (
            "#178FIt reminds me of an orbment,\x01",
            "a little...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_10F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113F")

    ChrTalk(    #29
        0x105,
        (
            "#1163FIt reminds me of an orbment,\x01",
            "in some ways...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_113F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1187")

    ChrTalk(    #30
        0x103,
        (
            "#022FAlmost feels like being\x01",
            "inside an orbment...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_1187")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D0")

    ChrTalk(    #31
        0x109,
        (
            "#1063FKinda feels like the inside\x01",
            "of an orbment...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_11D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1210")

    ChrTalk(    #32
        0x110,
        "#270FRather like being inside an orbment.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_1210")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1265")

    ChrTalk(    #33
        0x104,
        (
            "#034FThis is not wholly unlike being\x01",
            "inside an orbment. Eerie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_1265")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(    #34
        0x106,
        "#555FLike bein' an ant inside an orbment...\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F1")

    label("loc_12A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12F1")

    ChrTalk(    #35
        0x108,
        (
            "#072FIt feels a little like being\x01",
            "inside an orbment...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12F1")


    ChrTalk(    #36
        0x101,
        (
            "#1002F#6PAnd what the heck is that glowing liquid?\x02\x03",

            "I've never seen anything like THAT before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#1035F#6PI think it may be a liquid medium for\x01",
            "concentrated orbal power...\x02\x03",

            "#1042FI definitely wouldn't touch it barehanded.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(10, 0, -131270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 10, 0, -131270, 0)
    SetChrPos(0x1, 10, 0, -131270, 0)
    SetChrPos(0x2, 10, 0, -131270, 0)
    SetChrPos(0x3, 10, 0, -131270, 0)
    OP_A2(0x223C)
    EventEnd(0x0)
    Return()

    # Function_8_CC0 end

    def Function_9_146A(): pass

    label("Function_9_146A")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_D2(0x2601EF, 0x2601F4, 0xC)
    OP_D2(0x27028E, 0x270298, 0xD)
    OP_D2(0x270296, 0x2702A0, 0xE)
    OP_D2(0x2601F0, 0x2601F5, 0xF)
    OP_D2(0x2601F6, 0x2601FB, 0x10)
    OP_D2(0x270080, 0x270084, 0x11)
    OP_D2(0x270176, 0x270183, 0x12)
    OP_D2(0x270178, 0x270185, 0x13)
    OP_D2(0x2701DA, 0x2701DF, 0x14)
    OP_D2(0x2600C1, 0x2600C6, 0x15)
    OP_D2(0x260157, 0x26015C, 0x16)
    OP_D2(0x2701D0, 0x2701D5, 0x17)
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    LoadEffect(0x1, "monster\\\\msc0647a.eff")
    LoadEffect(0x2, "monster\\\\msc0647b.eff")
    LoadEffect(0x3, "scraft\\\\sc008_02.eff")
    LoadEffect(0x3, "scraft\\\\sc008_02.eff")
    LoadEffect(0x4, "monster\\\\ms31004a.eff")
    OP_6D(-101510, 30, -14160, 0)
    OP_67(0, 9190, -10000, 0)
    OP_6B(2190, 0)
    OP_6C(315000, 0)
    OP_6E(336, 0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 12)
    SetChrChipByIndex(0xA, 17)
    SetChrChipByIndex(0x9, 20)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -99780, 110, -11120, 0)
    OP_43(0xD, 0x3, 0x0, 0xC)
    OP_22(0x85, 0x1, 0x46)
    FadeToBright(1500, 0)

    def lambda_1606():
        OP_6D(-100630, 0, -4610, 6800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1606)

    def lambda_161E():
        OP_6B(2080, 6800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_161E)

    def lambda_162E():

        label("loc_162E")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x1F4)
        OP_48()
        Jump("loc_162E")

    QueueWorkItem2(0x8, 3, lambda_162E)
    OP_8E(0x8, 0xFFFE799C, 0x0, 0xFFFFEBD8, 0x3E8, 0x0)
    OP_44(0x8, 0x3)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #38
        0x8,
        (
            "#1157F#6P...Absurd... This is a farce...\x02\x03",

            "This wasn't in the Grandmaster's\x01",
            "prophecy at all!\x02\x03",

            "#1156FUn... Unless...\x02\x03",

            "Does this mean...I, too, was being\x01",
            "tested?\x02\x03",

            "#1157FRrrgh. I shall have to have words\x01",
            "with my 'master' once I return.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, -99790, 0, 7790, 180)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #39
        0xA,
        "Man's Voice",
        (
            "#3PSorry, but I think your question's\x01",
            "gonna be deferred. Indefinitely.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_17DF():
        OP_6D(-100880, 0, -790, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17DF)

    def lambda_17F7():
        OP_67(0, 5400, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17F7)

    def lambda_180F():
        OP_6B(1660, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_180F)

    def lambda_181F():
        OP_6E(534, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_181F)
    OP_8E(0xA, 0xFFFE79EC, 0x0, 0x96A, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #40
        0x8,
        (
            "#1157F#5PKevin Graham?\x01",
            "What are YOU doing here?\x02\x03",

            "Out of my way, insect. I've no time\x01",
            "to deal with gnats like you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 14)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x8, 14)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    OP_22(0xD8, 0x0, 0x64)
    OP_99(0x8, 0x4, 0x9, 0x5DC)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0xA, 22)
    SetChrSubChip(0xA, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0xA, 1)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0xA, 0, 2800, 3000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_82(0x0, 0x2)
    PlayEffect(0x3, 0x2, 0xA, 300, 1000, 550, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    PlayEffect(0x2, 0x3, 0xA, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x390, 0x0, 0x64)
    PlayEffect(0x4, 0x4, 0xA, 0, 0, 0, 0, 0, 0, 2000, 4000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_82(0x3, 0x2)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    ClearChrFlags(0x8, 0x800)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 13)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0x8,
        (
            "#1156FWhat...?\x01",
            "The Evil Eye didn't work?!\x02\x03",

            "Even with Gralsritter training, a fledgling\x01",
            "like you can't possibly--\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x4, 0x2)
    Sleep(1000)
    Sleep(100)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xA, 17)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #42
        0xA,
        (
            "#1066F#4PYeah, sorry, I've been puttin' on\x01",
            "a bit of a show.\x02\x03",

            "#1060FI'm actually their number five.\x01",
            "I've seen my fair share of fights.\x02\x03",

            "#1075FGranted...when you were at your best\x01",
            "and power-tripping on the Aureole\x01",
            "I would've struggled...\x02\x03",

            "#1073FBut now? You don't have a prayer.\x01",
            "Not that you do that anymore...\x01",
            "you filthy heathen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        "#1153FWhat...?\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x3, "map\\\\mp104_00.eff")
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 18)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0xA, 19)
    OP_99(0xA, 0x0, 0x7, 0xBB8)

    def lambda_1CD2():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CD2)
    Sleep(300)
    PlayEffect(0x3, 0x3, 0xA, 0, 1050, 1550, 0, 0, 0, 500, 500, 500, 0x8, 0, 500, 0, 0)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(200)
    OP_22(0x151, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 15)
    OP_99(0x8, 0x0, 0x4, 0x5DC)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)
    OP_83(0x3, 0x2)
    OP_82(0x3, 0x0)
    Sleep(500)

    ChrTalk(    #44
        0x8,
        "#1157FGh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#1075F#4PLocating the Aureole's been kind of\x01",
            "a sideshow. As you mighta figured out.\x02\x03",

            "#1072FSo. Georg Weissmann, apostate and\x01",
            "heretic, damned in the sight of Aidios.\x02\x03",

            "I'm here to send you to your final judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#1151FHeh...heh heh... I see...\x02\x03",

            "However, Gralsritter, I think you will\x01",
            "find it a little hard to fight the Faceless\x01",
            "on your own with onl--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_9E(0x8, 0x28, 0x0, 0x12C, 0x1388)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 15)
    Sleep(500)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_1F2E():
        OP_99(0xFE, 0x5, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1F2E)
    Sleep(150)
    OP_43(0xC, 0x0, 0x0, 0xA)
    WaitChrThread(0x8, 0x0)
    Sleep(1000)
    OP_99(0x8, 0x8, 0xA, 0x320)
    Sleep(500)

    ChrTalk(    #47
        0x8,
        "#1153F#5PWh...at? A stake?\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x152, 0x1, 0x5A)
    OP_99(0x8, 0xB, 0xF, 0x1F4)
    OP_62(0x8, 0xC8, 1800, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #48
        0x8,
        (
            "#1156F#5PIt's...the Pillar of Salt?\x02\x03",

            "The calamity which turned half of\x01",
            "North Ambria into a sea of salt...?\x02\x03",

            "#1157FThey would let you use that just to\x01",
            "kill ME?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #49
        0xA,
        (
            "#1072FIt's what you've earned, you faithless\x01",
            "pile of filth.\x02\x03",

            "The church does try to stay neutral in\x01",
            "all things, but we can't overlook what\x01",
            "you've done.\x02\x03",

            "Now kindly stand still and die quietly.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_213B():
        OP_99(0xFE, 0x10, 0x18, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_213B)
    Sleep(1000)

    ChrTalk(    #50 op#A op#5
        0x8,
        "#1158F#5P#3S#60AYou... YOU DAMNED DOG!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    WaitChrThread(0x8, 0x2)
    OP_23(0x152)
    Sleep(1500)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xA)
    Sleep(500)

    ChrTalk(    #51
        0xA,
        (
            "#1072F#4PDog...?\x01",
            "You aren't wrong, I guess.\x02\x03",

            "#1076F...\x02\x03",

            "#1065FYou know, Joshua, you're lucky.\x02\x03",

            "You, at least, can get out of this\x01",
            "sort of life.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    LoadEffect(0x1, "map\\\\mp055_00.eff")
    LoadEffect(0x2, "map\\\\mp105_00.eff")
    SetChrPos(0x9, -102410, 0, -5240, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetMessageWindowPos(70, 100, -1, -1)
    SetChrName("Boy's Voice")

    AnonymousTalk(    #52
        "\x07\x05#5PHeheheh... Is that jealously I hear?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_22FD():
        OP_6D(-102500, 0, -550, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_22FD)

    def lambda_2315():
        OP_67(0, 5200, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2315)

    def lambda_232D():
        OP_6B(1740, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_232D)

    def lambda_233D():
        OP_6E(542, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_233D)
    PlayEffect(0x1, 0x0, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(500)

    def lambda_238C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_238C)
    WaitChrThread(0x9, 0x1)
    OP_82(0x0, 0x2)
    OP_43(0x9, 0x3, 0x0, 0xB)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #53
        0x9,
        (
            "#853F#5PKevin Graham, the Heretic Hunter\x01",
            "and Gralsritter's Fifth Dominion.\x02\x03",

            "#854FI must say, you're just as cold\x01",
            "as the rumors said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "#1074F#4PAh... You're the 'Fool,' right?\x02\x03",

            "#1072FSorry, but it's a bit late for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#854F#5PHeheh. You may have heard, but I am\x01",
            "here purely as an observer. Purely.\x02\x03",

            "To observe and oversee every single facet\x01",
            "of the Gospel Plan and report the results, \x01",
            "without exception to the Grandmaster.\x02\x03",

            "#853FWeissmann's...self-destruction is simply\x01",
            "another result to report, and wasn't anything\x01",
            "I needed to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "#1075F#4PI see.\x02\x03",

            "#1073FYou Ouroboros types sure do love\x01",
            "being mysterious, don't you? Heh,\x01",
            "and you accuse ME of being cold...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "#854F#5PHaha! Are the Gralsritter REALLY\x01",
            "so different? I wonder.\x02\x03",

            "#853FNow, then...I'd say I've observed\x01",
            "everything, hmm?\x02\x03",

            "I've found what I was looking for,\x01",
            "so it's time I went on home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        "#1074F#4PWhat...?\x02",
    )

    CloseMessageWindow()

    def lambda_2734():
        OP_6D(-101170, 0, -3010, 1200)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2734)

    def lambda_274C():
        OP_67(0, 4800, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_274C)
    OP_8C(0x9, 90, 400)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 21)
    SetChrSubChip(0x9, 0)
    OP_0D()
    WaitChrThread(0x9, 0x1)
    Sleep(500)
    Fade(500)

    def lambda_278A():
        OP_6B(1540, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_278A)
    OP_99(0x9, 0x1, 0x2, 0x3E8)
    OP_22(0xBC, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    OP_22(0x153, 0x0, 0x64)
    SetChrSubChip(0x8, 25)
    Sleep(500)
    PlayEffect(0x2, 0x2, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)

    def lambda_27FD():

        label("loc_27FD")

        OP_99(0xFE, 0x8, 0xF, 0x5DC)
        OP_48()
        Jump("loc_27FD")

    QueueWorkItem2(0xC, 1, lambda_27FD)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2831():
        OP_6B(1640, 5000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2831)
    PlayEffect(0x1, 0x0, 0x9, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(200)
    PlayEffect(0x1, 0x1, 0xC, 0, 0, 0, 0, 0, 0, 1300, 1000, 1300, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 20)
    SetChrSubChip(0x9, 0)
    Sleep(500)
    OP_8C(0x9, 0, 300)
    Sleep(500)

    ChrTalk(    #59
        0x9,
        (
            "#851FHahaha! Well, good day,\x01",
            "Mr. Graham!\x02\x03",

            "I hope we meet again someday!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2922():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2922)
    Sleep(200)

    def lambda_2939():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2939)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0xC, 0x1)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_43(0x9, 0x3, 0x0, 0xB)
    SetChrFlags(0x9, 0x80)
    Sleep(1500)

    def lambda_296C():
        OP_67(0, 5300, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_296C)
    OP_8E(0xA, 0xFFFE79F6, 0x0, 0xFFFFF22C, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #60
        0xA,
        (
            "#1074F#4PFound what he was looking for?\x01",
            "Could he mean...?\x02\x03",

            "#1072F...\x02\x03",

            "#1065FWell, whatever...\x01",
            "That's outside my jurisdiction.\x02\x03",

            "#1067FI should hurry back and rejoin the others.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    FadeToDark(1500, 0, -1)
    OP_24(0x85, 0x3C)
    Sleep(200)
    OP_24(0x85, 0x32)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    OP_0D()
    OP_21()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #61
        (
            "\x07\x05And so Estelle's group escaped from the Axis Pillar while\x01",
            "Liber Ark began shaking itself apart.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #62
        (
            "\x07\x05With the sudden, immense reduction in orbal energy making\x01",
            "the Halo Rail unusable...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "\x07\x05Estelle's group began heading to the Arseille via the city's\x01",
            "underground passageways.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5208   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_9_146A end

    def Function_10_2BE9(): pass

    label("Function_10_2BE9")

    SetChrPos(0xFE, -99300, 0, -4800, 0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x800)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xC, 16)
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x5, 0x3E8)
    Return()

    # Function_10_2BE9 end

    def Function_11_2C22(): pass

    label("Function_11_2C22")

    Sleep(250)
    OP_24(0x10A, 0x5A)
    Sleep(250)
    OP_24(0x10A, 0x50)
    Sleep(250)
    OP_24(0x10A, 0x46)
    Sleep(250)
    OP_24(0x10A, 0x3C)
    Sleep(250)
    OP_24(0x10A, 0x32)
    Sleep(250)
    OP_24(0x10A, 0x28)
    Sleep(250)
    OP_24(0x10A, 0x1E)
    Sleep(250)
    OP_23(0x10A)
    Return()

    # Function_11_2C22 end

    def Function_12_2C6A(): pass

    label("Function_12_2C6A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CB8")
    OP_7C(0x28, 0x28, 0x3E8, 0x320)
    Sleep(1800)
    OP_7C(0x14, 0x14, 0x3E8, 0x514)
    Sleep(1600)
    OP_7C(0x1E, 0x1E, 0x3E8, 0x5DC)
    Sleep(2000)
    Jump("Function_12_2C6A")

    label("loc_2CB8")

    Return()

    # Function_12_2C6A end

    def Function_13_2CB9(): pass

    label("Function_13_2CB9")

    EventBegin(0x0)
    OP_A1(0xB, 0x0)
    SetChrPos(0xB, 101980, -1750, 850, 0)
    OP_48()
    Fade(1000)
    OP_6D(101980, 0, 850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 102000, 0, 2000, 0)
    OP_89(0x1, 103000, 0, 1000, 90)
    OP_89(0x2, 101000, 0, 1000, 270)
    OP_89(0x3, 102000, 0, 0, 180)
    OP_0D()
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_2D69():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2D69)
    Sleep(500)

    def lambda_2D89():
        OP_6D(101980, 35000, 850, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D89)

    def lambda_2DA1():
        OP_67(0, 14000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2DA1)

    def lambda_2DB9():
        OP_6C(335000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2DB9)
    Sleep(500)

    def lambda_2DCE():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2DCE)
    Sleep(500)

    def lambda_2DEE():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2DEE)
    Sleep(400)

    def lambda_2E0E():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2E0E)
    Sleep(200)

    def lambda_2E2E():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2E2E)
    Sleep(100)

    def lambda_2E4E():
        OP_8F(0xFE, 0x18E5C, 0xFDE8, 0x352, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2E4E)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x228C)
    OP_A3(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
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

    # Function_13_2CB9 end

    def Function_14_2EA8(): pass

    label("Function_14_2EA8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A1(0xB, 0x0)
    SetChrPos(0xB, 101980, 66000, 850, 0)
    OP_48()
    OP_6D(101980, 48000, 850, 0)
    OP_67(0, 16000, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(335000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 102000, 67000, 2000, 0)
    OP_89(0x1, 103000, 67000, 1000, 90)
    OP_89(0x2, 101000, 67000, 1000, 270)
    OP_89(0x3, 102000, 67000, 0, 180)
    OP_22(0xEB, 0x0, 0x64)

    def lambda_2F57():
        OP_6D(101980, 0, 850, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F57)

    def lambda_2F6F():
        OP_67(0, 9500, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F6F)

    def lambda_2F87():
        OP_6C(315000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F87)
    FadeToBright(1000, 0)
    SetPlaceName(0x11C)

    def lambda_2FA3():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2FA3)
    Sleep(3800)
    Sleep(4000)

    def lambda_2FC8():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2FC8)
    Sleep(700)

    def lambda_2FE8():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2FE8)
    Sleep(600)

    def lambda_3008():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3008)
    Sleep(100)

    def lambda_3028():
        OP_8F(0xFE, 0x18E5C, 0xFFFFF92A, 0x352, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3028)
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
    WaitChrThread(0xB, 0x1)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 102080, 0, 5330, 0)
    SetChrPos(0x1, 102080, 0, 5330, 0)
    SetChrPos(0x2, 102080, 0, 5330, 0)
    SetChrPos(0x3, 102080, 0, 5330, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_14_2EA8 end

    def Function_15_30F9(): pass

    label("Function_15_30F9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 1100, -94000, 0)
    SetChrPos(0x101, 500, 1100, -94500, 180)
    SetChrPos(0x102, -500, 1100, -94500, 180)
    SetChrPos(0xF8, 500, 1100, -93500, 180)
    SetChrPos(0xF9, -500, 1100, -93500, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_31D4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_31D4)

    def lambda_31E6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_31E6)

    def lambda_31F8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_31F8)

    def lambda_320A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_320A)
    Sleep(2500)
    Fade(500)
    OP_6D(0, 0, -97620, 0)
    SetChrPos(0x0, 0, 0, -97620, 180)
    SetChrPos(0x1, 0, 0, -97620, 180)
    SetChrPos(0x2, 0, 0, -97620, 180)
    SetChrPos(0x3, 0, 0, -97620, 180)
    EventEnd(0x0)
    Return()

    # Function_15_30F9 end

    def Function_16_3278(): pass

    label("Function_16_3278")

    EventBegin(0x1)
    Fade(500)
    OP_6D(0, 1100, -94000, 0)
    SetChrPos(0x101, -500, 1100, -93500, 0)
    SetChrPos(0x102, 500, 1100, -93500, 0)
    SetChrPos(0xF8, -500, 1100, -94500, 0)
    SetChrPos(0xF9, 500, 1100, -94500, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 3)), scpexpr(EXPR_END)), "loc_3316")
    OP_CC(0x1, 0x0, "[ 5F ]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_3316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 1)), scpexpr(EXPR_END)), "loc_3331")
    OP_CC(0x1, 0x0, "[ 4F ]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_3331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 6)), scpexpr(EXPR_END)), "loc_334C")
    OP_CC(0x1, 0x0, "[ 3F ]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_334C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 3)), scpexpr(EXPR_END)), "loc_3367")
    OP_CC(0x1, 0x0, "[ 2F ]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_3367")

    OP_CC(0x1, 0x0, "[Stop]")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33B0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3432")

    label("loc_33B0")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3432")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33D4")
    Jump("loc_3432")

    label("loc_33D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3425")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_340E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_340B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_340B")

    Jump("loc_3425")

    label("loc_340E")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33D4")

    label("loc_3425")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_33BA")

    label("loc_3432")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34D5")
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_348E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_348E)

    def lambda_34A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_34A0)

    def lambda_34B2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_34B2)

    def lambda_34C4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_34C4)
    Sleep(2000)

    label("loc_34D5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_34EE"),
        (1, "loc_34FA"),
        (2, "loc_3506"),
        (3, "loc_3512"),
        (SWITCH_DEFAULT, "loc_351E"),
    )


    label("loc_34EE")

    NewScene("ED6_DT21/C5306   ._SN", 111, 0, 0)
    IdleLoop()
    Jump("loc_351E")

    label("loc_34FA")

    NewScene("ED6_DT21/C5305   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_351E")

    label("loc_3506")

    NewScene("ED6_DT21/C5303   ._SN", 116, 0, 0)
    IdleLoop()
    Jump("loc_351E")

    label("loc_3512")

    NewScene("ED6_DT21/C5301   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_351E")

    label("loc_351E")

    Fade(500)
    OP_6D(0, 0, -97620, 0)
    SetChrPos(0x0, 0, 0, -97620, 180)
    SetChrPos(0x1, 0, 0, -97620, 180)
    SetChrPos(0x2, 0, 0, -97620, 180)
    SetChrPos(0x3, 0, 0, -97620, 180)
    EventEnd(0x0)
    Return()

    # Function_16_3278 end

    def Function_17_357B(): pass

    label("Function_17_357B")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_35F4"),
        (1, "loc_35FA"),
        (SWITCH_DEFAULT, "loc_3600"),
    )


    label("loc_35F4")

    OP_A2(0x1200)
    Jump("loc_3600")

    label("loc_35FA")

    OP_A2(0x1201)
    Jump("loc_3600")

    label("loc_3600")

    Return()

    # Function_17_357B end

    def Function_18_3601(): pass

    label("Function_18_3601")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_18_3601 end

    SaveToFile()

Try(main)
