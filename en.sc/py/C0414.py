from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0414   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0414.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        '',                                     # 14
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
        'ED6_DT09/CH10040 ._CH',             # 00
        'ED6_DT09/CH10041 ._CH',             # 01
        'ED6_DT09/CH10070 ._CH',             # 02
        'ED6_DT09/CH10071 ._CH',             # 03
        'ED6_DT09/CH10150 ._CH',             # 04
        'ED6_DT09/CH10151 ._CH',             # 05
        'ED6_DT09/CH10190 ._CH',             # 06
        'ED6_DT09/CH10191 ._CH',             # 07
        'ED6_DT29/CH12140 ._CH',             # 08
        'ED6_DT29/CH12141 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10040P._CP',             # 00
        'ED6_DT09/CH10041P._CP',             # 01
        'ED6_DT09/CH10070P._CP',             # 02
        'ED6_DT09/CH10071P._CP',             # 03
        'ED6_DT09/CH10150P._CP',             # 04
        'ED6_DT09/CH10151P._CP',             # 05
        'ED6_DT09/CH10190P._CP',             # 06
        'ED6_DT09/CH10191P._CP',             # 07
        'ED6_DT29/CH12140P._CP',             # 08
        'ED6_DT29/CH12141P._CP',             # 09
    )

    DeclNpc(
        X                   = 4420,
        Z                   = 1000,
        Y                   = -23090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -14210,
        Z                   = 0,
        Y                   = 14100,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x33,
        Unknown_18          = 6518,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -40,
        Z                   = 0,
        Y                   = 4100,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 6519,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 4019,
        Z                   = 0,
        Y                   = -4000,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x32,
        Unknown_18          = 6520,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3950,
        Z                   = 0,
        Y                   = -4080,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x33,
        Unknown_18          = 6521,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -2610,
        Z                   = 0,
        Y                   = -20030,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x34,
        Unknown_18          = 6522,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 4370,
        TriggerZ            = 0,
        TriggerY            = -22480,
        TriggerRange        = 1000,
        ActorX              = 4420,
        ActorZ              = 0,
        ActorY              = -23090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1CA",          # 00, 0
        "Function_1_1CB",          # 01, 1
        "Function_2_221",          # 02, 2
        "Function_3_237",          # 03, 3
    )


    def Function_0_1CA(): pass

    label("Function_0_1CA")

    Return()

    # Function_0_1CA end

    def Function_1_1CB(): pass

    label("Function_1_1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD")
    OP_6F(0x0, 0)
    Jump("loc_1E4")

    label("loc_1DD")

    OP_6F(0x0, 60)

    label("loc_1E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32E, 6)), scpexpr(EXPR_END)), "loc_1F0")
    SetChrFlags(0x9, 0x80)

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32E, 7)), scpexpr(EXPR_END)), "loc_1FC")
    SetChrFlags(0xA, 0x80)

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32F, 0)), scpexpr(EXPR_END)), "loc_208")
    SetChrFlags(0xB, 0x80)

    label("loc_208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32F, 1)), scpexpr(EXPR_END)), "loc_214")
    SetChrFlags(0xC, 0x80)

    label("loc_214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32F, 2)), scpexpr(EXPR_END)), "loc_220")
    SetChrFlags(0xD, 0x80)

    label("loc_220")

    Return()

    # Function_1_1CB end

    def Function_2_221(): pass

    label("Function_2_221")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_236")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_221")

    label("loc_236")

    Return()

    # Function_2_221 end

    def Function_3_237(): pass

    label("Function_3_237")

    OP_EA(0x2, 0xFF, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x32A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_28E():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28E)

    def lambda_2A9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2A9)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x35, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2FC"),
        (2, "loc_30E"),
        (1, "loc_31E"),
        (SWITCH_DEFAULT, "loc_321"),
    )


    label("loc_2FC")

    OP_A2(0x1957)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_321")

    label("loc_30E")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_31E")

    OP_B4(0x0)
    Return()

    label("loc_321")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16B, 1)"), scpexpr(EXPR_END)), "loc_36D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\x6B\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1956)
    Jump("loc_3CF")

    label("loc_36D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\x6B\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x6B\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_3CF")

    Jump("loc_435")

    label("loc_3D2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05This chest looks sad and deflated now that\x01",
            "you've taken all its stuff.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_435")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_237 end

    SaveToFile()

Try(main)
