from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4137   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4137.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        '\u3000',                               # 9
        '\u3000',                               # 10
        '\u3000',                               # 11
        '\u3000',                               # 12
        '\u3000',                               # 13
        '\u3000',                               # 14
        'Baral',                                # 15
        'Connor',                               # 16
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
        'ED6_DT06/CH20020 ._CH',             # 00
        'ED6_DT07/CH01100 ._CH',             # 01
        'ED6_DT07/CH01143 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT06/CH20020P._CP',             # 00
        'ED6_DT07/CH01100P._CP',             # 01
        'ED6_DT07/CH01143P._CP',             # 02
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65536,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572864,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572864,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572864,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 61020,
        Z                   = 0,
        Y                   = 2490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 65800,
        Z                   = 100,
        Y                   = -3410,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclActor(
        TriggerX            = 60700,
        TriggerZ            = 0,
        TriggerY            = 550,
        TriggerRange        = 400,
        ActorX              = 61020,
        ActorZ              = 1500,
        ActorY              = 2490,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E6",          # 00, 0
        "Function_1_1E7",          # 01, 1
        "Function_2_1F9",          # 02, 2
        "Function_3_20F",          # 03, 3
        "Function_4_214",          # 04, 4
        "Function_5_4B2",          # 05, 5
    )


    def Function_0_1E6(): pass

    label("Function_0_1E6")

    Return()

    # Function_0_1E6 end

    def Function_1_1E7(): pass

    label("Function_1_1E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F8")

    Return()

    # Function_1_1E7 end

    def Function_2_1F9(): pass

    label("Function_2_1F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1F9")

    label("loc_20E")

    Return()

    # Function_2_1F9 end

    def Function_3_20F(): pass

    label("Function_3_20F")

    Call(0, 4)
    Return()

    # Function_3_20F end

    def Function_4_214(): pass

    label("Function_4_214")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Curry of Dreams] - 900 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0xCB)
    OP_56(0x0)
    TalkEnd(0xE)
    Return()

    label("loc_291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_36B")
    SubMira(900)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06Ate #2CCurry of Dreams#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x640)
    OP_31(0x1, 0xFD, 0x640)
    OP_31(0x2, 0xFD, 0x640)
    OP_31(0x3, 0xFD, 0x640)
    OP_31(0x4, 0xFD, 0x640)
    OP_31(0x5, 0xFD, 0x640)
    OP_31(0x6, 0xFD, 0x640)
    OP_31(0x7, 0xFD, 0x640)
    OP_31(0x8, 0xFD, 0x640)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0xB)"), scpexpr(EXPR_END)), "loc_32C")
    Jump("loc_35D")

    label("loc_32C")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06Learned [#2CCurry of Dreams#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_35D")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_393")

    label("loc_36B")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_393")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xE)
    Return()

    label("loc_3A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BF")
    FadeToBright(300, 0)
    TalkEnd(0xE)
    Return()

    label("loc_3BF")

    FadeToBright(300, 0)

    ChrTalk(    #3
        0xE,
        "You look like you're in a hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xE,
        (
            "I know we're normally closed at this\x01",
            "hour, but I just felt like staying open\x01",
            "a little longer than usual today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xE,
        (
            "So really, there's no rush! I don't\x01",
            "mind you taking your time one bit.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_4_214 end

    def Function_5_4B2(): pass

    label("Function_5_4B2")

    TalkBegin(0xFE)

    ChrTalk(    #6
        0xFE,
        (
            "I'm SO happy that the cafe's\x01",
            "open this late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "It means I can take my sweet\x01",
            "time reading the new edition of\x01",
            "the Liberl News.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_4B2 end

    SaveToFile()

Try(main)
