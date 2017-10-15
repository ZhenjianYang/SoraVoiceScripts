from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3302   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3302.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        'ED6_DT09/CH10630 ._CH',             # 00
        'ED6_DT09/CH10631 ._CH',             # 01
        'ED6_DT09/CH10640 ._CH',             # 02
        'ED6_DT09/CH10641 ._CH',             # 03
        'ED6_DT09/CH10650 ._CH',             # 04
        'ED6_DT09/CH10651 ._CH',             # 05
        'ED6_DT09/CH10660 ._CH',             # 06
        'ED6_DT09/CH10661 ._CH',             # 07
        'ED6_DT09/CH10670 ._CH',             # 08
        'ED6_DT09/CH10671 ._CH',             # 09
        'ED6_DT09/CH10680 ._CH',             # 0A
        'ED6_DT09/CH10681 ._CH',             # 0B
        'ED6_DT09/CH10690 ._CH',             # 0C
        'ED6_DT09/CH10691 ._CH',             # 0D
        'ED6_DT09/CH10700 ._CH',             # 0E
        'ED6_DT09/CH10701 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10630P._CP',             # 00
        'ED6_DT09/CH10631P._CP',             # 01
        'ED6_DT09/CH10640P._CP',             # 02
        'ED6_DT09/CH10641P._CP',             # 03
        'ED6_DT09/CH10650P._CP',             # 04
        'ED6_DT09/CH10651P._CP',             # 05
        'ED6_DT09/CH10660P._CP',             # 06
        'ED6_DT09/CH10661P._CP',             # 07
        'ED6_DT09/CH10670P._CP',             # 08
        'ED6_DT09/CH10671P._CP',             # 09
        'ED6_DT09/CH10680P._CP',             # 0A
        'ED6_DT09/CH10681P._CP',             # 0B
        'ED6_DT09/CH10690P._CP',             # 0C
        'ED6_DT09/CH10691P._CP',             # 0D
        'ED6_DT09/CH10700P._CP',             # 0E
        'ED6_DT09/CH10701P._CP',             # 0F
    )

    DeclMonster(
        X                   = 30300,
        Z                   = 40,
        Y                   = -25110,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 9980,
        Z                   = 50,
        Y                   = -43520,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 29520,
        Z                   = -20,
        Y                   = 6960,
        Unknown_0C          = 180,
        Unknown_0E          = 14,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -3210,
        Z                   = -10,
        Y                   = 11040,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 12970,
        Z                   = -20,
        Y                   = 37620,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -8470,
        TriggerZ            = 40,
        TriggerY            = -39450,
        TriggerRange        = 1000,
        ActorX              = -9080,
        ActorZ              = 1460,
        ActorY              = -38880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5030,
        TriggerZ            = -20,
        TriggerY            = -16020,
        TriggerRange        = 1000,
        ActorX              = -5630,
        ActorZ              = 1480,
        ActorY              = -16340,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1FE",          # 00, 0
        "Function_1_1FF",          # 01, 1
        "Function_2_237",          # 02, 2
        "Function_3_3B9",          # 03, 3
    )


    def Function_0_1FE(): pass

    label("Function_0_1FE")

    Return()

    # Function_0_1FE end

    def Function_1_1FF(): pass

    label("Function_1_1FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211")
    OP_6F(0x0, 0)
    Jump("loc_218")

    label("loc_211")

    OP_6F(0x0, 60)

    label("loc_218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A")
    OP_6F(0x1, 0)
    Jump("loc_231")

    label("loc_22A")

    OP_6F(0x1, 60)

    label("loc_231")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_1FF end

    def Function_2_237(): pass

    label("Function_2_237")

    OP_EA(0x2, 0xBC, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3D5, 1)"), scpexpr(EXPR_END)), "loc_2A8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xD5\x03\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1537)
    Jump("loc_30C")

    label("loc_2A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xD5\x03\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xD5\x03\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_30C")

    Jump("loc_3AB")

    label("loc_30F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05This chest has already given you everything it\x01",
            "had in support of your noble cause. You would\x01",
            "be remiss to ask any more of it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3AB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_237 end

    def Function_3_3B9(): pass

    label("Function_3_3B9")

    OP_EA(0x2, 0xBD, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_491")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_42A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1538)
    Jump("loc_48E")

    label("loc_42A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_48E")

    Jump("loc_50D")

    label("loc_491")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Every empty chest we open takes a little bit of my\x01",
            "soul with it. Soon, I, too, will be empty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_50D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3B9 end

    SaveToFile()

Try(main)
