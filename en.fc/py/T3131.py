from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3131   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T3131   ._SN',
            'ED6_DT01/T3131_1 ._SN',
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
        'Dodge',                                # 9
        'Ben',                                  # 10
        'Ursus',                                # 11
        'Randall',                              # 12
        'Cosimo',                               # 13
        'Igor',                                 # 14
        'Rehmann',                              # 15
        'Constance',                            # 16
        'Ray',                                  # 17
        'Terry',                                # 18
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
        'ED6_DT07/CH01140 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01270 ._CH',             # 02
        'ED6_DT07/CH01003 ._CH',             # 03
        'ED6_DT07/CH01100 ._CH',             # 04
        'ED6_DT07/CH01250 ._CH',             # 05
        'ED6_DT07/CH01450 ._CH',             # 06
        'ED6_DT07/CH01230 ._CH',             # 07
        'ED6_DT07/CH01220 ._CH',             # 08
        'ED6_DT07/CH01660 ._CH',             # 09
        'ED6_DT07/CH01000 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH01140P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01270P._CP',             # 02
        'ED6_DT07/CH01003P._CP',             # 03
        'ED6_DT07/CH01100P._CP',             # 04
        'ED6_DT07/CH01250P._CP',             # 05
        'ED6_DT07/CH01450P._CP',             # 06
        'ED6_DT07/CH01230P._CP',             # 07
        'ED6_DT07/CH01220P._CP',             # 08
        'ED6_DT07/CH01660P._CP',             # 09
        'ED6_DT07/CH01000P._CP',             # 0A
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
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 13,
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
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 8,
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
        TalkScenaIndex      = 7,
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
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -530,
        TriggerZ            = -1000,
        TriggerY            = 4660,
        TriggerRange        = 400,
        ActorX              = -2470,
        ActorZ              = 500,
        ActorY              = 4710,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_266",          # 00, 0
        "Function_1_63F",          # 01, 1
        "Function_2_6D4",          # 02, 2
        "Function_3_6EA",          # 03, 3
        "Function_4_70E",          # 04, 4
        "Function_5_732",          # 05, 5
        "Function_6_756",          # 06, 6
        "Function_7_7FF",          # 07, 7
        "Function_8_C7C",          # 08, 8
        "Function_9_CE9",          # 09, 9
        "Function_10_1024",        # 0A, 10
        "Function_11_119A",        # 0B, 11
        "Function_12_119B",        # 0C, 12
        "Function_13_11A0",        # 0D, 13
        "Function_14_2587",        # 0E, 14
        "Function_15_3090",        # 0F, 15
        "Function_16_399E",        # 10, 16
    )


    def Function_0_266(): pass

    label("Function_0_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 790, -1000, 6110, 1)
    Jump("loc_63E")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2FE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63E")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_34A")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63E")

    label("loc_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_406")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1280, 4000, 2970, 200)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -580, -1000, 8800, 356)
    OP_43(0x9, 0x0, 0x0, 0x3)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -260, 4000, 7710, 192)
    OP_43(0xC, 0x0, 0x0, 0x5)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 790, -1000, 6110, 1)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -80, -1000, 3290, 275)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -2630, 4000, 7900, 182)
    SetChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -3680, 4000, 6510, 76)
    SetChrFlags(0x11, 0x10)
    Jump("loc_63E")

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_459")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1200, -1000, 5200, 97)
    OP_43(0xA, 0x0, 0x0, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -750, 2230, 105)
    Jump("loc_63E")

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_4A5")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63E")

    label("loc_4A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_50C")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -580, -1000, 8800, 356)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x10)
    SetChrChipByIndex(0xB, 10)
    SetChrPos(0xB, 1200, -1000, 5200, 97)
    OP_43(0xB, 0x0, 0x0, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -330, -1000, 3220, 270)
    Jump("loc_63E")

    label("loc_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_558")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3450, -1000, 8500, 185)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63E")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_5A4")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -450, -650, 2280, 266)
    Jump("loc_63E")

    label("loc_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_5F0")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -750, 2230, 105)
    Jump("loc_63E")

    label("loc_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_63E")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -580, -1000, 8800, 356)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -2470, -1000, 4710, 82)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 1810, -750, 2230, 105)

    label("loc_63E")

    Return()

    # Function_0_266 end

    def Function_1_63F(): pass

    label("Function_1_63F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_657")
    OP_B1("t3131_y")
    Jump("loc_660")

    label("loc_657")

    OP_B1("t3131_n")

    label("loc_660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_66A")
    Jump("loc_6D3")

    label("loc_66A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_674")
    Jump("loc_6D3")

    label("loc_674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_67E")
    Jump("loc_6D3")

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_68C")
    OP_64(0x0, 0x1)
    Jump("loc_6D3")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_696")
    Jump("loc_6D3")

    label("loc_696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_6A0")
    Jump("loc_6D3")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_6AE")
    OP_64(0x0, 0x1)
    Jump("loc_6D3")

    label("loc_6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_6B8")
    Jump("loc_6D3")

    label("loc_6B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_6C2")
    Jump("loc_6D3")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_6CC")
    Jump("loc_6D3")

    label("loc_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6D3")

    label("loc_6D3")

    Return()

    # Function_1_63F end

    def Function_2_6D4(): pass

    label("Function_2_6D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_6D4")

    label("loc_6E9")

    Return()

    # Function_2_6D4 end

    def Function_3_6EA(): pass

    label("Function_3_6EA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70D")
    OP_8D(0xFE, -1880, 8780, 440, 8570, 2000)
    Jump("Function_3_6EA")

    label("loc_70D")

    Return()

    # Function_3_6EA end

    def Function_4_70E(): pass

    label("Function_4_70E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_731")
    OP_8D(0xFE, 400, 5540, 5960, 4780, 2000)
    Jump("Function_4_70E")

    label("loc_731")

    Return()

    # Function_4_70E end

    def Function_5_732(): pass

    label("Function_5_732")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_755")
    OP_8D(0xFE, -1460, 6310, 0, 9500, 2000)
    Jump("Function_5_732")

    label("loc_755")

    Return()

    # Function_5_732 end

    def Function_6_756(): pass

    label("Function_6_756")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_7FB")

    ChrTalk(    #0
        0xFE,
        (
            "I wouldn't call a scheme pulled out\x01",
            "of your rear end 'forward thinking.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Branding that disgusting tomato isn't\x01",
            "going to make it sell any better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FB")

    TalkEnd(0xFE)
    Return()

    # Function_6_756 end

    def Function_7_7FF(): pass

    label("Function_7_7FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_9F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_8A1")

    ChrTalk(    #2
        0xFE,
        (
            "Terry, you're just not forward-\x01",
            "thinking enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "You've got to be ready to make\x01",
            "lemonade with the box of\x01",
            "chocolates life hands you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F0")

    label("loc_8A1")

    OP_A2(0x8)

    ChrTalk(    #4
        0xFE,
        (
            "Terry, you're just not forward-\x01",
            "thinking enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Take that bitter tomato. All we\x01",
            "need to do is brand it properly,\x01",
            "and it'll sell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "We could call it something inspired\x01",
            "like...'The Bitter Tomato'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Or maybe go by a more...scientific sounding\x01",
            "moniker. Hmm...'The Acerbic Tomato'?\x01",
            "Certainly SOUNDS officious enough...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F0")

    Jump("loc_C78")

    label("loc_9F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_C78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_AEE")

    ChrTalk(    #8
        0xFE,
        (
            "When we're working we usually\x01",
            "end up eating traditional foods\x01",
            "found in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Terry is having some serious\x01",
            "problems keeping up with us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Being shut up in your lab all\x01",
            "day isn't the best way to find\x01",
            "some inspiration...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C78")

    label("loc_AEE")

    OP_A2(0x8)

    ChrTalk(    #11
        0xFE,
        (
            "When we're working we usually\x01",
            "end up eating traditional foods\x01",
            "found in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "It doesn't have much going for\x01",
            "it in terms of subtlety...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "But if you need something to jolt\x01",
            "your head back into the game,\x01",
            "Zeiss cooking is it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I'd really like to see some\x01",
            "measures taken to allow\x01",
            "us to choose our meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Who knows? Inspiration can\x01",
            "sometimes come from the\x01",
            "strangest places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C78")

    TalkEnd(0xFE)
    Return()

    # Function_7_7FF end

    def Function_8_C7C(): pass

    label("Function_8_C7C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_CE5")

    ChrTalk(    #16
        0xFE,
        (
            "Today was an especially\x01",
            "exhausting day for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I need to blow off all\x01",
            "this stress...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE5")

    TalkEnd(0xFE)
    Return()

    # Function_8_C7C end

    def Function_9_CE9(): pass

    label("Function_9_CE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_EB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_D77")

    ChrTalk(    #18
        0xFE,
        (
            "Here I am, aid to the heroic rescue\x01",
            "of Professor Russell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "...and I'm not allowed to brag\x01",
            "to anybody about it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAF")

    label("loc_D77")

    OP_A2(0x6)

    ChrTalk(    #20
        0xFE,
        (
            "Yeah, I heard you did a number\x01",
            "on Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I feel proud enough being on\x01",
            "the team and helping from\x01",
            "the sidelines...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "But I was a little nervous when\x01",
            "all those soldiers surrounded\x01",
            "the container.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "We can look back and laugh\x01",
            "about it now. But at the time,\x01",
            "we all nearly peed ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAF")

    Jump("loc_1020")

    label("loc_EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1020")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_F4D")

    ChrTalk(    #24
        0xFE,
        (
            "Tomorrow I've got to take a\x01",
            "factory ship out to Leiston\x01",
            "Fortress again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Recently the army has been\x01",
            "placing all kinds of orders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1020")

    label("loc_F4D")

    OP_A2(0x6)

    ChrTalk(    #26
        0xFE,
        (
            "Tomorrow I've got to take a\x01",
            "factory ship out to Leiston\x01",
            "Fortress again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Everybody's busy getting all the\x01",
            "prep work taken care of...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Times like this make me glad\x01",
            "I'm a pilot, and not a laborer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1020")

    TalkEnd(0xFE)
    Return()

    # Function_9_CE9 end

    def Function_10_1024(): pass

    label("Function_10_1024")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_10CA")

    ChrTalk(    #29
        0xFE,
        (
            "I came all this way just to see\x01",
            "Randall and wouldn't you know,\x01",
            "he's already gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Oh well. May as well order up\x01",
            "an old favorite or two.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1196")

    label("loc_10CA")

    OP_A2(0x4)

    ChrTalk(    #31
        0xFE,
        "Hmph. Just my luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I came all this way just to see\x01",
            "Randall and wouldn't you know,\x01",
            "he's already gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "He's the kind of guy you're\x01",
            "always just missin'. Been\x01",
            "like that since he was young.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1196")

    TalkEnd(0xFE)
    Return()

    # Function_10_1024 end

    def Function_11_119A(): pass

    label("Function_11_119A")

    Return()

    # Function_11_119A end

    def Function_12_119B(): pass

    label("Function_12_119B")

    Call(0, 13)
    Return()

    # Function_12_119B end

    def Function_13_11A0(): pass

    label("Function_13_11A0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1257")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                  # 0
            "Shop\x01",                  # 1
            "Show ingredients\x01",      # 2
            "Leave\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122B")
    OP_0D()
    OP_A9(0x41)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_122B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1243")
    Call(1, 2)
    TalkEnd(0x9)
    Return()

    label("loc_1243")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1254")
    TalkEnd(0x9)
    Return()

    label("loc_1254")

    Jump("loc_12C5")

    label("loc_1257")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B4")
    OP_0D()
    OP_A9(0x41)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_12B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C5")
    TalkEnd(0x9)
    Return()

    label("loc_12C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_131D")

    ChrTalk(    #34
        0x9,
        "Thanks for today, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        (
            "Keep an eye out for my\x01",
            "latest creation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_131D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1514")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1442")

    ChrTalk(    #36
        0x9,
        (
            "Lately I've been hearing about\x01",
            "this strange tomato they grew\x01",
            "in the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "I got a sample to see if I\x01",
            "could use it somehow...and\x01",
            "it is INCREDIBLE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "I've already placed a big\x01",
            "advance order for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "I plan to feature them on the\x01",
            "menu, so watch for it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1511")

    label("loc_1442")

    OP_A2(0x1)

    ChrTalk(    #40
        0x9,
        (
            "Hey, you guys. I really want to\x01",
            "thank you for before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "I was just on my way to the\x01",
            "factory to place an advance\x01",
            "order on those tomatoes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "I should have them on the menu\x01",
            "in no time. Just wait!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1511")

    Jump("loc_2583")

    label("loc_1514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_15E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15A0")

    ChrTalk(    #43
        0x9,
        "Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        "I just finished the lunch rush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "How'd you like an EXTRA bitter\x01",
            "Tomato Sandwich?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#506FEr, pass.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15E5")

    label("loc_15A0")


    ChrTalk(    #47
        0x9,
        "Hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        "I just finished the lunch rush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        "Take a load off.\x02",
    )

    CloseMessageWindow()

    label("loc_15E5")

    Jump("loc_2583")

    label("loc_15E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_168C")

    ChrTalk(    #50
        0x9,
        (
            "I've been working on some new\x01",
            "dishes lately that have really\x01",
            "been keeping me busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "I suppose I need to pace myself\x01",
            "so I don't fall over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1894")

    label("loc_168C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16F4")

    ChrTalk(    #52
        0x9,
        "I've been really busy lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "I suppose I need to pace myself\x01",
            "so I don't fall over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1894")

    label("loc_16F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17F2")
    OP_A2(0xB)

    ChrTalk(    #54
        0x9,
        "I've been so busy lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "In addition to my regular work\x01",
            "I've also been tinkering with\x01",
            "some new dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "If I keep this up I'm sure to\x01",
            "burn out sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "We working-class Joes need to\x01",
            "watch out for each other, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1894")

    label("loc_17F2")

    OP_A2(0x1)

    ChrTalk(    #58
        0x9,
        "I've been real busy lately...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "If I keep this up I'm sure to\x01",
            "burn out sometime soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "We working-class Joes need to\x01",
            "watch out for each other, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1894")

    Jump("loc_2583")

    label("loc_1897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_19C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(    #61
        0x9,
        "Damn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "Ursus has gone home and Randall's\x01",
            "not around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        "Guess I better get working.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "I've got to finish those new\x01",
            "tomato dishes, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BD")

    label("loc_1950")


    ChrTalk(    #66
        0x9,
        "Damn it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "Ursus has gone home and Randall's\x01",
            "not around...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        "Guess I better get working.\x02",
    )

    CloseMessageWindow()

    label("loc_19BD")

    Jump("loc_2583")

    label("loc_19C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1A60")

    ChrTalk(    #70
        0x9,
        (
            "Sounds like there was a heck\x01",
            "of a fuss over at the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "I bet some guys snuck in trying\x01",
            "to steal one of the new top-secret\x01",
            "experiments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_1A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1C6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1AC2")
    TurnDirection(0x9, 0xB, 400)

    ChrTalk(    #72
        0x9,
        "Okay, Randall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "First I need you to have a\x01",
            "taste of this tomato.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6C")

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1AFF")

    ChrTalk(    #74
        0x9,
        (
            "So, Randall. What are we talking\x01",
            "about today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6C")

    label("loc_1AFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1BBC")
    OP_A2(0xB)

    ChrTalk(    #75
        0x9,
        (
            "He's really been putting in some\x01",
            "hard work while Ursus has been\x01",
            "out of the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "Today I think I'll leave the store\x01",
            "to him while I come up with\x01",
            "some new entrees.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C6C")

    label("loc_1BBC")

    OP_A2(0x1)

    ChrTalk(    #77
        0x9,
        (
            "He's really been putting in some\x01",
            "hard work while Ursus has been\x01",
            "out of the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "Today I think I'll leave the store\x01",
            "to him while I come up with\x01",
            "some new entrees.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C6C")

    Jump("loc_2583")

    label("loc_1C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C9A")

    ChrTalk(    #79
        0x9,
        "Randall! Saute's up!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E14")

    label("loc_1C9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D5E")
    OP_A2(0x1)

    ChrTalk(    #80
        0x9,
        (
            "Right now Ursus isn't here, \x01",
            "so I've got to stir pots...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "...but honestly, cooking can\x01",
            "be pretty interesting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "I've been coming up with so\x01",
            "many ideas for that tomato.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E14")

    label("loc_1D5E")

    OP_A2(0x1)

    ChrTalk(    #83
        0x9,
        (
            "Right now Ursus isn't here, \x01",
            "so I've got to stir pots...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        (
            "...but honestly, cooking can\x01",
            "be pretty interesting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "I've been coming up with a lot\x01",
            "of ideas for new foods.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E14")

    Jump("loc_2583")

    label("loc_1E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_1F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1EDB")

    ChrTalk(    #86
        0x9,
        (
            "But I really need something\x01",
            "that'll grab customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        (
            "I've pretty much exhausted all\x01",
            "the traditional stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "I need to add some new things\x01",
            "to the menu soon or else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F5A")

    label("loc_1EDB")

    OP_A2(0x1)

    ChrTalk(    #89
        0x9,
        (
            "Everybody gets tired of the\x01",
            "same thing every day, be it\x01",
            "crackers or caviar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "Maybe he's just a selfish\x01",
            "old geezer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F5A")

    Jump("loc_2583")

    label("loc_1F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_20D0")

    ChrTalk(    #91
        0x9,
        (
            "Of course it'll be a big problem if\x01",
            "orbments stopped again like they\x01",
            "did yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "Kids today can't even imagine a\x01",
            "world without orbments in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        "Lights, heaters, vacuums, laundry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "Pretty much everything in our\x01",
            "daily life depends on having\x01",
            "the orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "Thinking about it that way really\x01",
            "makes you admire Professor\x01",
            "Russell even more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_20D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_24A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_21E1")

    ChrTalk(    #96
        0x9,
        (
            "People tied up in research have\x01",
            "always been seen as having...\x01",
            "health issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "That's how provincial Zeiss food\x01",
            "came about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "Easy to cook, easy to eat,\x01",
            "and nutritious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "We Zeiss cooks all make our\x01",
            "recipes around those three\x01",
            "basic criteria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A5")

    label("loc_21E1")

    OP_A2(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_END)), "loc_22BB")

    ChrTalk(    #100
        0x9,
        (
            "Zeiss cooking is full of recipes\x01",
            "suited for engineers without\x01",
            "time to cook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "Easy to cook, easy to eat,\x01",
            "and nutritious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "We Zeiss cooks all make our\x01",
            "recipes around those three\x01",
            "basic criteria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A5")

    label("loc_22BB")

    OP_A2(0x576)
    TurnDirection(0x9, 0x107, 0)

    ChrTalk(    #103
        0x9,
        (
            "Well, isn't this a treat!\x01",
            "How are you, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "And how's Professor Russell?\x01",
            "Same as ever, I trust?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x107,
        (
            "#061FYes, sir, he's doing well!\x02\x03",

            "He's been spending all of his\x01",
            "time lately working on new\x01",
            "experiments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "I don't know if that's entirely\x01",
            "healthy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "You should try to get him\x01",
            "outside a little more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x107,
        (
            "#065FOkay, I'll try.\x02\x03",

            "#561FBut once he gets into a new project,\x01",
            "it's really hard to get him to listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "That sounds like your grandfather,\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A5")

    Jump("loc_2583")

    label("loc_24A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2583")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(    #110
        0x9,
        (
            "We serve traditional Zeiss\x01",
            "foods here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "'Simple and Efficient,' that's the\x01",
            "motto for Zeiss cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2583")

    label("loc_2526")

    OP_A2(0x1)

    ChrTalk(    #112
        0x9,
        (
            "Hello!  Haven't seen you all\x01",
            "before... Passing through?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x9,
        "Well, come in and rest!\x02",
    )

    CloseMessageWindow()

    label("loc_2583")

    TalkEnd(0x9)
    Return()

    # Function_13_11A0 end

    def Function_14_2587(): pass

    label("Function_14_2587")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_261D")

    ChrTalk(    #114
        0xFE,
        (
            "It looks like Louise is going to be\x01",
            "busy with work for a while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I hope the new stuff Ben comes\x01",
            "up with tastes good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268B")

    label("loc_261D")

    OP_A2(0x2)

    ChrTalk(    #116
        0xFE,
        (
            "Lately, Ben's been trying to think\x01",
            "of some new dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I'm a little...torn...about\x01",
            "the prospect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268B")

    Jump("loc_308C")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_2739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_26D5")

    ChrTalk(    #118
        0xFE,
        (
            "I sure hope Louise's work goes\x01",
            "smoothly for her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2736")

    label("loc_26D5")

    OP_A2(0x2)

    ChrTalk(    #119
        0xFE,
        (
            "Whew.\x01",
            "Finally, lunch hour is finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Things should be quiet now\x01",
            "until dinnertime.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2736")

    Jump("loc_308C")

    label("loc_2739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_28C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27F5")

    ChrTalk(    #121
        0xFE,
        (
            "Being dedicated to your job\x01",
            "is good and all, but everyone\x01",
            "needs a break sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "All work and no play...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "...makes me worry about turning\x01",
            "into Ben one day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C4")

    label("loc_27F5")

    OP_A2(0x2)

    ChrTalk(    #124
        0xFE,
        (
            "Yesterday I made this new soup\x01",
            "I just learned about and had\x01",
            "Louise eat some...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "She's been so busy lately she\x01",
            "hasn't had time to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "At least her sister, Yuriel, seemed\x01",
            "to enjoy it though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28C4")

    Jump("loc_308C")

    label("loc_28C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_29D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2979")

    ChrTalk(    #127
        0xFE,
        (
            "Louise has been all wrapped up\x01",
            "in her orbal research and isn't\x01",
            "getting any exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "She's so out of shape she'd probably\x01",
            "lose a shadow boxing match. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29D2")

    label("loc_2979")

    OP_A2(0x2)

    ChrTalk(    #129
        0xFE,
        (
            "Hey! Did you hear about the\x01",
            "central factory?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "I really hope Louise is okay.\x02",
    )

    CloseMessageWindow()

    label("loc_29D2")

    Jump("loc_308C")

    label("loc_29D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_2AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A36")

    ChrTalk(    #131
        0xFE,
        "Grr, this is frustrating!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I hate it when we get a rush\x01",
            "for no reason!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADE")

    label("loc_2A36")

    OP_A2(0x2)

    ChrTalk(    #133
        0xFE,
        (
            "Let's see. Saute's next...no, wait,\x01",
            "it was the soup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "When did all these dishes get\x01",
            "backed up like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Ben! We could really use your\x01",
            "help right now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ADE")

    Jump("loc_308C")

    label("loc_2AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_2C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BB4")

    ChrTalk(    #136
        0xFE,
        (
            "Louise has been acting kind of\x01",
            "strange lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "She's hasn't been spending time\x01",
            "with her family, she hardly eats\x01",
            "at meals...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "It's like she feels like she\x01",
            "doesn't have time for it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C6E")

    label("loc_2BB4")

    OP_A2(0x2)

    ChrTalk(    #139
        0xFE,
        (
            "That Louise. Who does she think\x01",
            "I am, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "'Oh, Ursus, can you take care of my\x01",
            "sister? I've got work,' she asks me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Her job gives her more free\x01",
            "time than mine does!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6E")

    Jump("loc_308C")

    label("loc_2C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_2DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2CD9")

    ChrTalk(    #142
        0xFE,
        (
            "I'm really surprised I didn't\x01",
            "fall down the stairs there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "Lucky me, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DC0")

    label("loc_2CD9")

    OP_A2(0x2)

    ChrTalk(    #144
        0xFE,
        (
            "I tell you, I couldn't believe\x01",
            "it yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "I was bussing a table on the\x01",
            "second floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "I was just coming down the\x01",
            "stairs when suddenly everything\x01",
            "went black.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I don't even know how I didn't\x01",
            "break the dishes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC0")

    Jump("loc_308C")

    label("loc_2DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2E2F")

    ChrTalk(    #148
        0xFE,
        "That recipe is really simple.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I'll try it out at my girlfriend's\x01",
            "house sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F12")

    label("loc_2E2F")

    OP_A2(0x2)

    ChrTalk(    #150
        0xFE,
        (
            "I know this soup looks a\x01",
            "little bit strange...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "...but when I actually tried it,\x01",
            "it was delicious! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "Just throw it all in a pot and\x01",
            "warm it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "I'm impressed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "You're not just some lazy slug\x01",
            "after all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F12")

    Jump("loc_308C")

    label("loc_2F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_308C")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_END)), "loc_2FC9")

    ChrTalk(    #155
        0xFE,
        (
            "Seems like this soup can help\x01",
            "you concentrate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "...but I wonder if it really\x01",
            "does anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "I mean, it's water, bouillon,\x01",
            "vegetables and pepper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308C")

    label("loc_2FC9")

    OP_A2(0x2)

    ChrTalk(    #158
        0xFE,
        (
            "Let's see here...first the bouillon,\x01",
            "then the vegetables, and then a\x01",
            "dash of pepper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "Skim off the fat while it simmers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "What? Is that it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "Seriously. Is that it?\x02",
    )

    CloseMessageWindow()

    label("loc_308C")

    TalkEnd(0xFE)
    Return()

    # Function_14_2587 end

    def Function_15_3090(): pass

    label("Function_15_3090")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_30FB")

    ChrTalk(    #163
        0xFE,
        "You're something else, Ben.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "Looks like the only thing you\x01",
            "worked today is your jaw.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399A")

    label("loc_30FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_319E")

    ChrTalk(    #165
        0xFE,
        (
            "Hoho! All that talk of new recipes\x01",
            "and hard work...and with a straight\x01",
            "face the whole time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "That Ben really had me goin' there\x01",
            "for a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399A")

    label("loc_319E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_32A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3209")

    ChrTalk(    #167
        0xFE,
        (
            "Still though, I got so caught up\x01",
            "in the conversation I didn't notice\x01",
            "outside at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_329D")

    label("loc_3209")

    OP_A2(0x3)

    ChrTalk(    #168
        0xFE,
        (
            "There used to be guys trying\x01",
            "to steal from the factory all\x01",
            "the time back in the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "I'd say they've refined their\x01",
            "methods these days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329D")

    Jump("loc_399A")

    label("loc_32A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_33D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3301")

    ChrTalk(    #170
        0xFE,
        "Oh, yeah. Ben...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "I heard you found some kind\x01",
            "of secret ingredient.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D4")

    label("loc_3301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3361")

    ChrTalk(    #172
        0xFE,
        (
            "I think I'll tell young Ben about\x01",
            "that incident I had in the Ruan\x01",
            "souvenir shop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D4")

    label("loc_3361")

    OP_A2(0x3)

    ChrTalk(    #173
        0xFE,
        (
            "Ha ha ha, workin's a job for\x01",
            "the young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "It does me good to see these\x01",
            "young folks all so hard at work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D4")

    Jump("loc_399A")

    label("loc_33D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_34E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_346F")

    ChrTalk(    #175
        0xFE,
        (
            "I help out here when Ursus\x01",
            "isn't around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(    #176
        0xFE,
        (
            "Hey, Ben! Is that saute ready\x01",
            "yet or not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "You've got customers waiting!\x02",
    )

    CloseMessageWindow()
    Jump("loc_34E2")

    label("loc_346F")

    OP_A2(0x3)

    ChrTalk(    #178
        0xFE,
        (
            "I help out here when Ursus\x01",
            "isn't around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "It gets so busy here at lunchtime\x01",
            "it'll make your head spin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E2")

    Jump("loc_399A")

    label("loc_34E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3563")

    ChrTalk(    #180
        0xFE,
        "It's tough, though...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I've been coming here so much\x01",
            "I'm sick of the food. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "I'd love something spicy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_399A")

    label("loc_3563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3651")

    ChrTalk(    #183
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Everybody running around like\x01",
            "headless chickens just because\x01",
            "the orbments stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "Try thinking about life before we had\x01",
            "them! Why, when I was young we...ah...\x01",
            "What were we talkin' about again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399A")

    label("loc_3651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_38A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3714")
    OP_A2(0x577)

    ChrTalk(    #186
        0xFE,
        (
            "Gotta hand it to ol' Russell,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "I was an old clockmaker,\x01",
            "right alongside him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "I had to retire because of my eyes,\x01",
            "but I sure hope Russell's a lifer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38A1")

    label("loc_3714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3794")

    ChrTalk(    #189
        0xFE,
        (
            "Sure, Ben's food is a bit simple,\x01",
            "but it tastes good enough, and\x01",
            "it's cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "One could say he's economical.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38A1")

    label("loc_3794")

    OP_A2(0x3)

    ChrTalk(    #191
        0xFE,
        (
            "You need to watch yourself around\x01",
            "the owner, Ben.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "He loves to come up with all\x01",
            "kinds of justifications for his\x01",
            "plain cooking.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x9, 255)
    ClearMapFlags(0x1)
    OP_69(0x9, 0x3E8)

    ChrTalk(    #193
        0x9,
        "HEY!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x9,
        (
            "What are you telling my new\x01",
            "customers?!\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x0, 0x3E8)
    SetMapFlags(0x1)

    ChrTalk(    #195
        0xFE,
        (
            "What?\x01",
            "I'm just tellin' it like it is!\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)

    label("loc_38A1")

    Jump("loc_399A")

    label("loc_38A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_399A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3909")

    ChrTalk(    #196
        0xFE,
        (
            "Yeah, I just got back from a\x01",
            "little trip to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "But it don't beat home.\x02",
    )

    CloseMessageWindow()
    Jump("loc_399A")

    label("loc_3909")

    OP_A2(0x3)

    ChrTalk(    #198
        0xFE,
        "Ahh, home at last!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "Yeah, I just got back from a\x01",
            "little trip to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "I had a good time, but I sure am\x01",
            "glad to be back at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399A")

    TalkEnd(0xFE)
    Return()

    # Function_15_3090 end

    def Function_16_399E(): pass

    label("Function_16_399E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3A3D")

    ChrTalk(    #201
        0xFE,
        (
            "Lots of the food here is simple,\x01",
            "but it tastes good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "You can tell the cook here\x01",
            "doesn't want to spend his\x01",
            "time actually cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD8")

    label("loc_3A3D")

    OP_A2(0x0)

    ChrTalk(    #203
        0xFE,
        (
            "The hotel's kitchen is closed,\x01",
            "so I found this restaurant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "In a town full of engineers,\x01",
            "the food's pretty simple.\x01",
            "But it's also pretty tasty.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD8")

    TalkEnd(0xFE)
    Return()

    # Function_16_399E end

    SaveToFile()

Try(main)
