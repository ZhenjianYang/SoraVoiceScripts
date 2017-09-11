from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3222   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3222.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Percy',                                # 9
        'Ed',                                   # 10
        'Lynn',                                 # 11
        'Recia',                                # 12
        'Cyril',                                # 13
        'Addy',                                 # 14
        'Lucky',                                # 15
        'Sima',                                 # 16
        'Quantay',                              # 17
        'Edel',                                 # 18
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
        'ED6_DT07/CH01040 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01030 ._CH',             # 02
        'ED6_DT07/CH01150 ._CH',             # 03
        'ED6_DT07/CH01120 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
        'ED6_DT07/CH01160 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01060 ._CH',             # 08
        'ED6_DT07/CH01130 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01040P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01030P._CP',             # 02
        'ED6_DT07/CH01150P._CP',             # 03
        'ED6_DT07/CH01120P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
        'ED6_DT07/CH01160P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01060P._CP',             # 08
        'ED6_DT07/CH01130P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 2440,
        TriggerZ            = 250,
        TriggerY            = 2960,
        TriggerRange        = 400,
        ActorX              = 2550,
        ActorZ              = 1750,
        ActorY              = 4470,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25E",          # 00, 0
        "Function_1_3EA",          # 01, 1
        "Function_2_3EB",          # 02, 2
        "Function_3_401",          # 03, 3
        "Function_4_4B4",          # 04, 4
        "Function_5_4BB",          # 05, 5
        "Function_6_4C2",          # 06, 6
        "Function_7_5E4",          # 07, 7
        "Function_8_5EB",          # 08, 8
        "Function_9_5F2",          # 09, 9
        "Function_10_5F9",         # 0A, 10
        "Function_11_600",         # 0B, 11
        "Function_12_605",         # 0C, 12
        "Function_13_FCC",         # 0D, 13
    )


    def Function_0_25E(): pass

    label("Function_0_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_27E")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_29E")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2BE")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2F4")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -960, 250, -2580, 188)
    Jump("loc_3E9")

    label("loc_2F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_32A")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -5240, 500, -330, 108)
    Jump("loc_3E9")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_376")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 590, 250, 2540, 10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4130, 0, -2220, 291)
    Jump("loc_3E9")

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_3AC")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -3250, 250, 4820, 348)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_3AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3CC")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)
    Jump("loc_3E9")

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E9")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 2550, 250, 4470, 192)

    label("loc_3E9")

    Return()

    # Function_0_25E end

    def Function_1_3EA(): pass

    label("Function_1_3EA")

    Return()

    # Function_1_3EA end

    def Function_2_3EB(): pass

    label("Function_2_3EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_400")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3EB")

    label("loc_400")

    Return()

    # Function_2_3EB end

    def Function_3_401(): pass

    label("Function_3_401")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_40E")
    Jump("loc_4B0")

    label("loc_40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_418")
    Jump("loc_4B0")

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_422")
    Jump("loc_4B0")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_42C")
    Jump("loc_4B0")

    label("loc_42C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_436")
    Jump("loc_4B0")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_440")
    Jump("loc_4B0")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_49F")

    ChrTalk(    #0
        0xFE,
        "How fascinating!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Is this Eastern pottery? The design\x01",
            "work is so exquisite!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B0")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_4A9")
    Jump("loc_4B0")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4B0")

    label("loc_4B0")

    TalkEnd(0xFE)
    Return()

    # Function_3_401 end

    def Function_4_4B4(): pass

    label("Function_4_4B4")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_4_4B4 end

    def Function_5_4BB(): pass

    label("Function_5_4BB")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_4BB end

    def Function_6_4C2(): pass

    label("Function_6_4C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_4CF")
    Jump("loc_5E0")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_4D9")
    Jump("loc_5E0")

    label("loc_4D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_4E3")
    Jump("loc_5E0")

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4ED")
    Jump("loc_5E0")

    label("loc_4ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_4F7")
    Jump("loc_5E0")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_5C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_558")

    ChrTalk(    #2
        0xFE,
        (
            "Looks like I have everything\x01",
            "I need...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "This is a cute plate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C2")

    label("loc_558")

    OP_A2(0x2)

    ChrTalk(    #5
        0xFE,
        (
            "Let me see...we're out of soy\x01",
            "sauce and sake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I don't think we need anything\x01",
            "else for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C2")

    Jump("loc_5E0")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_5CF")
    Jump("loc_5E0")

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_5D9")
    Jump("loc_5E0")

    label("loc_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5E0")

    label("loc_5E0")

    TalkEnd(0xFE)
    Return()

    # Function_6_4C2 end

    def Function_7_5E4(): pass

    label("Function_7_5E4")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_5E4 end

    def Function_8_5EB(): pass

    label("Function_8_5EB")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_5EB end

    def Function_9_5F2(): pass

    label("Function_9_5F2")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_5F2 end

    def Function_10_5F9(): pass

    label("Function_10_5F9")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_5F9 end

    def Function_11_600(): pass

    label("Function_11_600")

    Call(0, 12)
    Return()

    # Function_11_600 end

    def Function_12_605(): pass

    label("Function_12_605")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_665")
    OP_0D()
    OP_A9(0x44)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_665")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_676")
    TalkEnd(0xF)
    Return()

    label("loc_676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_76B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6E5")

    ChrTalk(    #7
        0xF,
        (
            "Thanks to the Royal Birthday\x01",
            "Celebration we're empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        "It's so hard to stay awake...\x02",
    )

    CloseMessageWindow()
    Jump("loc_768")

    label("loc_6E5")

    OP_A2(0x7)

    ChrTalk(    #9
        0xF,
        "What have we here...customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xF,
        (
            "I was just about to close up\x01",
            "for the night, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xF,
        "Well, please have a look around.\x02",
    )

    CloseMessageWindow()

    label("loc_768")

    Jump("loc_FC8")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_8BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7EF")

    ChrTalk(    #12
        0xF,
        (
            "I'm sorry, but I don't think you'll\x01",
            "find any clues here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xF,
        (
            "But since you're here...why\x01",
            "not buy a souvenir?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BC")

    label("loc_7EF")

    OP_A2(0x7)

    ChrTalk(    #14
        0xF,
        "Ah, welcome back everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xF,
        "I heard all about you from Mrs. Mao.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xF,
        (
            "I doubt you'll find any clues\x01",
            "around this quiet little town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xF,
        (
            "But have a look around. Maybe\x01",
            "pick up a souvenir or two?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BC")

    Jump("loc_FC8")

    label("loc_8BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_A7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_98D")

    ChrTalk(    #18
        0xF,
        (
            "I think I was happiest when\x01",
            "I was a young boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        (
            "I was about Quantay's age when\x01",
            "I first met my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xF,
        (
            "To think I was Quantay's age\x01",
            "myself once...even I find it\x01",
            "hard to believe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7C")

    label("loc_98D")

    OP_A2(0x7)

    ChrTalk(    #21
        0xF,
        (
            "All the adults are in shock\x01",
            "because of what happened\x01",
            "in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xF,
        (
            "But Quantay and the other kids\x01",
            "are outside playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xF,
        (
            "I think I was happiest when\x01",
            "I was a young boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xF,
        (
            "I was about Quantay's age when\x01",
            "I first met my wife.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7C")

    Jump("loc_FC8")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B14")

    ChrTalk(    #25
        0xF,
        "Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xF,
        (
            "Ready to leave already? How about\x01",
            "a little something to remember your\x01",
            "visit by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xF,
        "Everyone buys at least one...\x02",
    )

    CloseMessageWindow()
    Jump("loc_FC8")

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_BF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_B8C")

    ChrTalk(    #28
        0xF,
        "Oh, my back...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xF,
        (
            "After I'm done with the cleaning,\x01",
            "I think I'll go over to the Maple\x01",
            "Leaf Inn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2")

    label("loc_B8C")

    OP_A2(0x7)

    ChrTalk(    #30
        0xF,
        "What have we here...customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xF,
        (
            "I was just about to close up,\x01",
            "so finish up your shopping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF2")

    Jump("loc_FC8")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_CF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_C3D")

    ChrTalk(    #32
        0xF,
        "And down goes the sun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xF,
        "Another day finished.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CEF")

    label("loc_C3D")

    OP_A2(0x7)

    ChrTalk(    #34
        0xF,
        (
            "I mostly sell souvenirs to the\x01",
            "people passing through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xF,
        (
            "But I also keep some daily goods\x01",
            "to sell to my neighbors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xF,
        (
            "There isn't any other real store\x01",
            "in this town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEF")

    Jump("loc_FC8")

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_DEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D6B")

    ChrTalk(    #37
        0xF,
        (
            "Finally, we have some customers\x01",
            "coming in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xF,
        (
            "I recommend our pottery, we have\x01",
            "a wide selection.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE8")

    label("loc_D6B")

    OP_A2(0x7)

    ChrTalk(    #39
        0xF,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xF,
        (
            "Finally, we have some customers\x01",
            "coming in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "I recommend our pottery, we have\x01",
            "a wide selection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE8")

    Jump("loc_FC8")

    label("loc_DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_EAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E50")

    ChrTalk(    #42
        0xF,
        (
            "My boy Quantay is a light-hearted\x01",
            "young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        "He takes after my late wife.\x02",
    )

    CloseMessageWindow()
    Jump("loc_EA8")

    label("loc_E50")

    OP_A2(0x7)

    ChrTalk(    #44
        0xF,
        "Not many customers today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xF,
        (
            "I hope Quantay's inviting them\x01",
            "to see the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA8")

    Jump("loc_FC8")

    label("loc_EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_FC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_F46")

    ChrTalk(    #46
        0xF,
        "Hello, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xF,
        (
            "You can eat our spring-boiled\x01",
            "eggs in a variety of ways!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xF,
        (
            "The recipes are limited only by\x01",
            "your imagination!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC8")

    label("loc_F46")

    OP_A2(0x7)

    ChrTalk(    #49
        0xF,
        "What have we here...customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "Come right in! Have a look around\x01",
            "the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xF,
        "I recommend our spring-boiled eggs!\x02",
    )

    CloseMessageWindow()

    label("loc_FC8")

    TalkEnd(0xF)
    Return()

    # Function_12_605 end

    def Function_13_FCC(): pass

    label("Function_13_FCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_FD9")
    Jump("loc_129F")

    label("loc_FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_FE3")
    Jump("loc_129F")

    label("loc_FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_FED")
    Jump("loc_129F")

    label("loc_FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1048")

    ChrTalk(    #52
        0xFE,
        "Ugh, what a chore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "After I finish opening the store\x01",
            "I'm going outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129F")

    label("loc_1048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_11BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_110C")

    ChrTalk(    #54
        0xFE,
        (
            "Now Dad's all worried about the\x01",
            "customers. And watch, he's going\x01",
            "to make me ask people in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "He's always asking me to do\x01",
            "embarrassing stuff like that.\x01",
            "Why can't he do it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BA")

    label("loc_110C")

    OP_A2(0x8)

    ChrTalk(    #56
        0xFE,
        (
            "My dad doesn't care about\x01",
            "selling stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "He gets this look when people\x01",
            "come into the store when he's\x01",
            "tired and wants to close up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "He just isn't a salesman.\x02",
    )

    CloseMessageWindow()

    label("loc_11BA")

    Jump("loc_129F")

    label("loc_11BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_1284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_120B")

    ChrTalk(    #59
        0xFE,
        "Would you like to buy an egg?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "They're really good!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1281")

    label("loc_120B")

    OP_A2(0x8)

    ChrTalk(    #61
        0xFE,
        "Eggs! Who'd like an egg?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Who can say no to one of these\x01",
            "firm and delicious, fresh spring-\x01",
            "boiled eggs?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1281")

    Jump("loc_129F")

    label("loc_1284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_128E")
    Jump("loc_129F")

    label("loc_128E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1298")
    Jump("loc_129F")

    label("loc_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_129F")

    label("loc_129F")

    TalkEnd(0xFE)
    Return()

    # Function_13_FCC end

    SaveToFile()

Try(main)
