from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3220   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3220.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'ED6_DT07/CH01210 ._CH',             # 09
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
        'ED6_DT07/CH01210P._CP',             # 09
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
        TalkScenaIndex      = 11,
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
        TalkScenaIndex      = 12,
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
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25E",          # 00, 0
        "Function_1_3EA",          # 01, 1
        "Function_2_40C",          # 02, 2
        "Function_3_422",          # 03, 3
        "Function_4_557",          # 04, 4
        "Function_5_55E",          # 05, 5
        "Function_6_565",          # 06, 6
        "Function_7_6A5",          # 07, 7
        "Function_8_6AC",          # 08, 8
        "Function_9_6B3",          # 09, 9
        "Function_10_6BA",         # 0A, 10
        "Function_11_6C1",         # 0B, 11
        "Function_12_1088",        # 0C, 12
        "Function_13_135F",        # 0D, 13
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_402")
    OP_B1("t3220_y")
    Jump("loc_40B")

    label("loc_402")

    OP_B1("t3220_n")

    label("loc_40B")

    Return()

    # Function_1_3EA end

    def Function_2_40C(): pass

    label("Function_2_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_421")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_40C")

    label("loc_421")

    Return()

    # Function_2_40C end

    def Function_3_422(): pass

    label("Function_3_422")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_42F")
    Jump("loc_553")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_439")
    Jump("loc_553")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_443")
    Jump("loc_553")

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_44D")
    Jump("loc_553")

    label("loc_44D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_457")
    Jump("loc_553")

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_461")
    Jump("loc_553")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4C7")

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
    Jump("loc_53F")

    label("loc_4C7")

    OP_A2(0x9)

    ChrTalk(    #2
        0xFE,
        (
            "It's too early to eat and with the\x01",
            "pump broken I can't go in the\x01",
            "hot springs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "I guess it's time to shop!\x02",
    )

    CloseMessageWindow()

    label("loc_53F")

    Jump("loc_553")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_54C")
    Jump("loc_553")

    label("loc_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_553")

    label("loc_553")

    TalkEnd(0xFE)
    Return()

    # Function_3_422 end

    def Function_4_557(): pass

    label("Function_4_557")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_4_557 end

    def Function_5_55E(): pass

    label("Function_5_55E")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_5_55E end

    def Function_6_565(): pass

    label("Function_6_565")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_572")
    Jump("loc_6A1")

    label("loc_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_57C")
    Jump("loc_6A1")

    label("loc_57C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_586")
    Jump("loc_6A1")

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_590")
    Jump("loc_6A1")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_59A")
    Jump("loc_6A1")

    label("loc_59A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_686")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_619")

    ChrTalk(    #4
        0xFE,
        (
            "Looks like I have everything\x01",
            "I need...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 330, 800)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #5
        0xFE,
        "Oh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "This is a cute plate.\x02",
    )

    CloseMessageWindow()
    Jump("loc_683")

    label("loc_619")

    OP_A2(0x2)

    ChrTalk(    #7
        0xFE,
        (
            "Let me see...we're out of soy\x01",
            "sauce and sake...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I don't think we need anything\x01",
            "else for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_683")

    Jump("loc_6A1")

    label("loc_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_690")
    Jump("loc_6A1")

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_69A")
    Jump("loc_6A1")

    label("loc_69A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6A1")

    label("loc_6A1")

    TalkEnd(0xFE)
    Return()

    # Function_6_565 end

    def Function_7_6A5(): pass

    label("Function_7_6A5")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_6A5 end

    def Function_8_6AC(): pass

    label("Function_8_6AC")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_6AC end

    def Function_9_6B3(): pass

    label("Function_9_6B3")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_6B3 end

    def Function_10_6BA(): pass

    label("Function_10_6BA")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_6BA end

    def Function_11_6C1(): pass

    label("Function_11_6C1")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_721")
    OP_0D()
    OP_A9(0x44)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_721")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_732")
    TalkEnd(0xF)
    Return()

    label("loc_732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_827")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_7A1")

    ChrTalk(    #9
        0xF,
        (
            "Thanks to the Royal Birthday\x01",
            "Celebration we're empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xF,
        "It's so hard to stay awake...\x02",
    )

    CloseMessageWindow()
    Jump("loc_824")

    label("loc_7A1")

    OP_A2(0x7)

    ChrTalk(    #11
        0xF,
        "What have we here...customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xF,
        (
            "I was just about to close up\x01",
            "for the night, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xF,
        "Well, please have a look around.\x02",
    )

    CloseMessageWindow()

    label("loc_824")

    Jump("loc_1084")

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_97B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_8AB")

    ChrTalk(    #14
        0xF,
        (
            "I'm sorry, but I don't think you'll\x01",
            "find any clues here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xF,
        (
            "But since you're here...why\x01",
            "not buy a souvenir?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_978")

    label("loc_8AB")

    OP_A2(0x7)

    ChrTalk(    #16
        0xF,
        "Ah, welcome back everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xF,
        "I heard all about you from Mrs. Mao.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xF,
        (
            "I doubt you'll find any clues\x01",
            "around this quiet little town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        (
            "But have a look around. Maybe\x01",
            "pick up a souvenir or two?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_978")

    Jump("loc_1084")

    label("loc_97B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_B3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_A49")

    ChrTalk(    #20
        0xF,
        (
            "I think I was happiest when\x01",
            "I was a young boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xF,
        (
            "I was about Quantay's age when\x01",
            "I first met my wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xF,
        (
            "To think I was Quantay's age\x01",
            "myself once...even I find it\x01",
            "hard to believe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B38")

    label("loc_A49")

    OP_A2(0x7)

    ChrTalk(    #23
        0xF,
        (
            "All the adults are in shock\x01",
            "because of what happened\x01",
            "in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xF,
        (
            "But Quantay and the other kids\x01",
            "are outside playing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xF,
        (
            "I think I was happiest when\x01",
            "I was a young boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xF,
        (
            "I was about Quantay's age when\x01",
            "I first met my wife.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B38")

    Jump("loc_1084")

    label("loc_B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_BD0")

    ChrTalk(    #27
        0xF,
        "Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xF,
        (
            "Ready to leave already? How about\x01",
            "a little something to remember your\x01",
            "visit by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xF,
        "Everyone buys at least one...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1084")

    label("loc_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_CB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_C48")

    ChrTalk(    #30
        0xF,
        "Oh, my back...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xF,
        (
            "After I'm done with the cleaning,\x01",
            "I think I'll go over to the Maple\x01",
            "Leaf Inn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAE")

    label("loc_C48")

    OP_A2(0x7)

    ChrTalk(    #32
        0xF,
        "What have we here...customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xF,
        (
            "I was just about to close up,\x01",
            "so finish up your shopping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAE")

    Jump("loc_1084")

    label("loc_CB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_DAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_CF9")

    ChrTalk(    #34
        0xF,
        "And down goes the sun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xF,
        "Another day finished.\x02",
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_CF9")

    OP_A2(0x7)

    ChrTalk(    #36
        0xF,
        (
            "I mostly sell souvenirs to the\x01",
            "people passing through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xF,
        (
            "But I also keep some daily goods\x01",
            "to sell to my neighbors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xF,
        (
            "There isn't any other real store\x01",
            "in this town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAB")

    Jump("loc_1084")

    label("loc_DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_E27")

    ChrTalk(    #39
        0xF,
        (
            "Finally, we have some customers\x01",
            "coming in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xF,
        (
            "I recommend our pottery, we have\x01",
            "a wide selection.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA4")

    label("loc_E27")

    OP_A2(0x7)

    ChrTalk(    #41
        0xF,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xF,
        (
            "Finally, we have some customers\x01",
            "coming in!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        (
            "I recommend our pottery, we have\x01",
            "a wide selection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA4")

    Jump("loc_1084")

    label("loc_EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_F67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_F0C")

    ChrTalk(    #44
        0xF,
        (
            "My boy Quantay is a light-hearted\x01",
            "young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xF,
        "He takes after my late wife.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F64")

    label("loc_F0C")

    OP_A2(0x7)

    ChrTalk(    #46
        0xF,
        "Not many customers today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xF,
        (
            "I hope Quantay's inviting them\x01",
            "to see the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F64")

    Jump("loc_1084")

    label("loc_F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1002")

    ChrTalk(    #48
        0xF,
        "Hello, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xF,
        (
            "You can eat our spring-boiled\x01",
            "eggs in a variety of ways!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xF,
        (
            "The recipes are limited only by\x01",
            "your imagination!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1084")

    label("loc_1002")

    OP_A2(0x7)

    ChrTalk(    #51
        0xF,
        "What have we here...customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xF,
        (
            "Come right in! Have a look around\x01",
            "the place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xF,
        "I recommend our spring-boiled eggs!\x02",
    )

    CloseMessageWindow()

    label("loc_1084")

    TalkEnd(0xF)
    Return()

    # Function_11_6C1 end

    def Function_12_1088(): pass

    label("Function_12_1088")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1095")
    Jump("loc_135B")

    label("loc_1095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_109F")
    Jump("loc_135B")

    label("loc_109F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_10A9")
    Jump("loc_135B")

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_1104")

    ChrTalk(    #54
        0xFE,
        "Ugh, what a chore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "After I finish opening the store\x01",
            "I'm going outside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_135B")

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_11C8")

    ChrTalk(    #56
        0xFE,
        (
            "Now Dad's all worried about the\x01",
            "customers. And watch, he's going\x01",
            "to make me ask people in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "He's always asking me to do\x01",
            "embarrassing stuff like that.\x01",
            "Why can't he do it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1276")

    label("loc_11C8")

    OP_A2(0x8)

    ChrTalk(    #58
        0xFE,
        (
            "My dad doesn't care about\x01",
            "selling stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "He gets this look when people\x01",
            "come into the store when he's\x01",
            "tired and wants to close up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "He just isn't a salesman.\x02",
    )

    CloseMessageWindow()

    label("loc_1276")

    Jump("loc_135B")

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_END)), "loc_1340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_12C7")

    ChrTalk(    #61
        0xFE,
        "Would you like to buy an egg?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "They're really good!\x02",
    )

    CloseMessageWindow()
    Jump("loc_133D")

    label("loc_12C7")

    OP_A2(0x8)

    ChrTalk(    #63
        0xFE,
        "Eggs! Who'd like an egg?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Who can say no to one of these\x01",
            "firm and delicious, fresh spring-\x01",
            "boiled eggs?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133D")

    Jump("loc_135B")

    label("loc_1340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_END)), "loc_134A")
    Jump("loc_135B")

    label("loc_134A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1354")
    Jump("loc_135B")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_135B")

    label("loc_135B")

    TalkEnd(0xFE)
    Return()

    # Function_12_1088 end

    def Function_13_135F(): pass

    label("Function_13_135F")

    Call(0, 11)
    Return()

    # Function_13_135F end

    SaveToFile()

Try(main)
