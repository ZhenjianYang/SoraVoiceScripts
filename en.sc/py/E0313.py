from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0313   ._SN',
        MapName             = 'Event',
        Location            = 'E0313.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
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
        'Faye',                                 # 9
        'Mechanic Payton',                      # 10
        'Royal Guardsman',                      # 11
        'Royal Guardsman',                      # 12
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
        'ED6_DT07/CH01550 ._CH',             # 00
        'ED6_DT07/CH01450 ._CH',             # 01
        'ED6_DT07/CH01320 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01550P._CP',             # 00
        'ED6_DT07/CH01450P._CP',             # 01
        'ED6_DT07/CH01320P._CP',             # 02
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2270,
        Z                   = 0,
        Y                   = 5880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 2820,
        Z                   = 0,
        Y                   = -90,
        Direction           = 90,
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
        X                   = 2280,
        Z                   = 0,
        Y                   = 6070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )


    DeclEvent(
        X                   = 700,
        Y                   = -2000,
        Z                   = -10500,
        Range               = 3200,
        Unknown_10          = 0xDAC,
        Unknown_14          = 0xFFFFE2B4,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = -30,
        Y                   = -1000,
        Z                   = -7340,
        Range               = 3700,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFDC88,
        Unknown_18          = 0x0,
        Unknown_1C          = 27,
    )


    ScpFunction(
        "Function_0_182",          # 00, 0
        "Function_1_217",          # 01, 1
        "Function_2_3A2",          # 02, 2
        "Function_3_3B8",          # 03, 3
        "Function_4_F37",          # 04, 4
        "Function_5_1704",         # 05, 5
        "Function_6_1AB3",         # 06, 6
        "Function_7_2386",         # 07, 7
        "Function_8_2A2B",         # 08, 8
        "Function_9_2B6A",         # 09, 9
        "Function_10_2D49",        # 0A, 10
        "Function_11_2F60",        # 0B, 11
        "Function_12_3161",        # 0C, 12
        "Function_13_338B",        # 0D, 13
        "Function_14_358C",        # 0E, 14
        "Function_15_37B1",        # 0F, 15
        "Function_16_39B6",        # 10, 16
        "Function_17_3A89",        # 11, 17
        "Function_18_3AA5",        # 12, 18
        "Function_19_3AC1",        # 13, 19
        "Function_20_3ADD",        # 14, 20
        "Function_21_3B0D",        # 15, 21
        "Function_22_3B29",        # 16, 22
        "Function_23_3B62",        # 17, 23
        "Function_24_3BE8",        # 18, 24
        "Function_25_3C77",        # 19, 25
        "Function_26_3D04",        # 1A, 26
        "Function_27_3D91",        # 1B, 27
    )


    def Function_0_182(): pass

    label("Function_0_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_1CF")

    label("loc_199")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4")
    Jump("loc_1CF")

    label("loc_1A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_1CF")

    label("loc_1B4")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 3690, 0, -4710, 90)

    label("loc_1CF")

    Jump("loc_203")

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_1F2")
    SetChrPos(0x8, 3690, 0, -4710, 90)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_203")

    label("loc_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_203")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_216")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_216")

    Return()

    # Function_0_182 end

    def Function_1_217(): pass

    label("Function_1_217")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_235")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_265")
    OP_B1("E0313_1")
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_6F(0x5, 0)
    Jump("loc_26E")

    label("loc_265")

    OP_B1("E0313_2")

    label("loc_26E")

    Jump("loc_2A3")

    label("loc_271")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289")
    OP_B1("E0313_2")
    Jump("loc_2A3")

    label("loc_289")

    OP_B1("E0313_1")
    OP_72(0x5, 0x20)
    OP_72(0x5, 0x8)
    OP_6F(0x5, 0)

    label("loc_2A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CC")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D9")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9")
    OP_22(0x7A, 0x1, 0x46)

    label("loc_2D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_304")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7A, 0x1, 0x46)

    label("loc_304")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_325")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_32C")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_34A")
    OP_71(0x6, 0x4)
    OP_72(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    Jump("loc_3A1")

    label("loc_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_368")
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x9, 0x4)
    Jump("loc_3A1")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_386")
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_72(0x9, 0x4)
    Jump("loc_3A1")

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_3A1")
    OP_72(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)

    label("loc_3A1")

    Return()

    # Function_1_217 end

    def Function_2_3A2(): pass

    label("Function_2_3A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3A2")

    label("loc_3B7")

    Return()

    # Function_2_3A2 end

    def Function_3_3B8(): pass

    label("Function_3_3B8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3D9")

    ChrTalk(    #0
        0xFE,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F33")

    label("loc_3D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC")
    Call(0, 14)
    Jump("loc_F33")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FF")
    Call(0, 12)
    Jump("loc_F33")

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_412")
    Call(0, 10)
    Jump("loc_F33")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_421")
    Call(0, 7)
    Jump("loc_F33")

    label("loc_421")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",         # 0
            "Descend\x01",      # 1
            "Leave\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_559")

    ChrTalk(    #1
        0xFE,
        "Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Hop on the lift, then.\x01",
            "Let's get you down there.\x02",
        )
    )

    CloseMessageWindow()
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_4E9")
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_555")

    label("loc_4E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_50E")
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_555")

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_533")
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_555")

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_555")
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_555")

    Return()

    label("loc_559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A")
    TalkEnd(0xFE)
    Return()

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_745")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D")

    ChrTalk(    #3
        0xFE,
        (
            "The equipment the old man's been working\x01",
            "on is finally ready for prototyping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Once I send you guys down on the lift,\x01",
            "I'll be heading over to help put it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "What does it do, exactly? Hmm...\x01",
            "Well, I'll let that be a surprise\x01",
            "for when it's assembled.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_742")

    label("loc_68D")


    ChrTalk(    #6
        0xFE,
        (
            "The equipment's finally ready to be\x01",
            "prototyped, and I'll help put it together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "What does it do, exactly? Hmm...\x01",
            "Well, I'll let that be a surprise\x01",
            "for when it's assembled.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_742")

    Jump("loc_F33")

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_955")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_899")

    ChrTalk(    #8
        0xFE,
        (
            "One of our central factory guys,\x01",
            "Ray, was walking around muttering\x01",
            "to himself a minute ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Ray's the kind of guy who can dive into anything,\x01",
            "acting like he can take on the world...but he\x01",
            "sometimes gets in over his head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Seeing him like that must mean that whatever\x01",
            "they're working on, it's tough going.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_952")

    label("loc_899")


    ChrTalk(    #11
        0xFE,
        (
            "One of our central factory guys,\x01",
            "Ray, was walking around muttering\x01",
            "to himself a minute ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Seeing him like that must mean that whatever\x01",
            "they're working on, it's tough going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_952")

    Jump("loc_F33")

    label("loc_955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_B15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A67")

    ChrTalk(    #13
        0xFE,
        (
            "Russell is developing some kind\x01",
            "of really specialized orbal device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I caught a peek at the blueprints, but\x01",
            "I couldn't make heads or tails of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I think it's supposed to be an\x01",
            "orbal wave amplifier...? But that's\x01",
            "practically just a guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_B12")

    label("loc_A67")


    ChrTalk(    #16
        0xFE,
        (
            "Russell is developing some kind\x01",
            "of really specialized orbal device.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I think it's supposed to be an\x01",
            "orbal wave amplifier...? But that's\x01",
            "practically just a guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B12")

    Jump("loc_F33")

    label("loc_B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8F")

    ChrTalk(    #18
        0xFE,
        (
            "I haven't heard the details, but it sounds\x01",
            "like the old man's developing some kind\x01",
            "of new gizmo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "And he's short on people, so I got\x01",
            "brought aboard in a hurry.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x1, 0x20)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE2")
    OP_A2(0x3)

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C63")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared Quest Messenger of Love in previous game\x01",      # 0
            "Did not\x01",                                               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C57"),
        (1, "loc_C5D"),
        (SWITCH_DEFAULT, "loc_C63"),
    )


    label("loc_C57")

    OP_A2(0x3)
    Jump("loc_C63")

    label("loc_C5D")

    OP_A3(0x3)
    Jump("loc_C63")

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CB4")

    ChrTalk(    #20
        0xFE,
        (
            "*siiigh* ...I was supposed to be on\x01",
            "vacation with Brahm by now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CFA")

    label("loc_CB4")


    ChrTalk(    #21
        0xFE,
        (
            "*siiigh* ...I was supposed to be on\x01",
            "vacation with Rudi by now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D63")

    ChrTalk(    #22
        0x107,
        (
            "#562FAwww... I'm sorry, Faye.\x02\x03",

            "Grandpa's always giving you so much trouble.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)
    Jump("loc_DA4")

    label("loc_D63")


    ChrTalk(    #23
        0x101,
        "#1016FAh.. haha... I kinda feel for you there, Faye.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    label("loc_DA4")


    ChrTalk(    #24
        0xFE,
        (
            "Yeah, well, I have to admit it feels good\x01",
            "to be part of something like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "It's a job that needs doing, so there's no\x01",
            "time to sweat the small stuff, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "You have any trouble, I've got your back.\x01",
            "I promise.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_F33")

    label("loc_E8F")


    ChrTalk(    #27
        0xFE,
        (
            "The old man's in the middle of working\x01",
            "on another new invention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "As if he's not busy enough analyzing the tower\x01",
            "phenomenon! Where does he find the time?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F33")

    TalkEnd(0x8)
    Return()

    # Function_3_3B8 end

    def Function_4_F37(): pass

    label("Function_4_F37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_1700")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as didn't meet in Chapter 3\x01",      # 0
            "Set as met in Chapter 3\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FBF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123B")

    ChrTalk(    #29
        0xFE,
        (
            "Hello, Estelle.\x01",
            "It's been quite a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1015FEr, you're...uhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Oh, no! Did you forget me?\x01",
            "It's Payton, the mechanic!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I was with you during one of your plans\x01",
            "against Colonel Richard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1008FS-Sorry! A lot's happened since then.\x01",
            "I remember you now, though.\x02\x03",

            "You're the one who got us the Intelligence\x01",
            "Division airship, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Haha, yep! Glad I could be of help. And\x01",
            "glad you didn't completely forget about me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Still, I'd heard there were bracers\x01",
            "aboard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "And the thought crossed my mind that it\x01",
            "might be you guys, but I didn't think I'd\x01",
            "be right on the money! Small world, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1393")

    label("loc_123B")


    ChrTalk(    #37
        0xFE,
        "Hey, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1004FPayton! Why are you here?\x02\x03",

            "#1016FActually...wait.\x01",
            "Duh, that should be obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Haha! Yes, I'm the ship's engineer\x01",
            "for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Still, I'd heard there were bracers\x01",
            "aboard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "And the thought crossed my mind that it\x01",
            "might be you guys, but I didn't think I'd\x01",
            "be right on the money! Small world, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1393")


    ChrTalk(    #42
        0x101,
        (
            "#1006FWe didn't think the Arseille'd be here,\x01",
            "either.\x02\x03",

            "Seems like the Royal Army's pulling out\x01",
            "everything for this mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Yes, I've heard this is the largest Liberlian\x01",
            "military mobilization since the Hundred\x01",
            "Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "And they tell me our target's a\x01",
            "legendary ancient dragon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "...What better way to test the new\x01",
            "engine, though, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1011FYou sure seem confident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Well, hey. In a way, all our tuning of that\x01",
            "thing was in preparation for this day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "The designers from the central factory\x01",
            "are here today, too, to collect data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "It's finally time for the Arseille to make\x01",
            "her grand entrance. I want her to fly like\x01",
            "nothing's flown before!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A73)
    Jump("loc_1700")

    label("loc_1640")


    ChrTalk(    #50
        0xFE,
        (
            "They tell me our target's a legendary\x01",
            "ancient dragon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "...What better way to test the new\x01",
            "engine, though, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I'm sure the Arseille will wow everyone\x01",
            "with its capabilities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1700")

    TalkEnd(0xFE)
    Return()

    # Function_4_F37 end

    def Function_5_1704(): pass

    label("Function_5_1704")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FC")

    ChrTalk(    #53
        0xFE,
        "So, that fallen outrigger...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Amazingly, we ended up retrieving it\x01",
            "by hauling it back with a howitzer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "That was Major Mueller's suggestion.\x01",
            "But then, you don't get to be a tank\x01",
            "commander without some serious smarts!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AAF")

    label("loc_17FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E1")

    ChrTalk(    #56
        0xFE,
        (
            "Ah, we're just about to try Major\x01",
            "Mueller's suggestion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Recovering the fallen outrigger by\x01",
            "dragging it back with a howitzer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Sure not an idea any of us could've\x01",
            "come up with too easily!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_196F")

    label("loc_18E1")


    ChrTalk(    #59
        0xFE,
        (
            "Recovering the fallen outrigger by\x01",
            "dragging it back with a howitzer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Sure not an idea any of us could've\x01",
            "come up with too easily!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196F")

    Jump("loc_1AAF")

    label("loc_1972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A66")

    ChrTalk(    #61
        0xFE,
        "So, that fallen outrigger...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Amazingly, we ended up retrieving it\x01",
            "by hauling it back with a howitzer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "That was Major Mueller's suggestion.\x01",
            "But then, you don't get to be a tank\x01",
            "commander without some serious smarts!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1AAF")

    label("loc_1A66")


    ChrTalk(    #64
        0xFE,
        "Using a howitzer as a tractor, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "That's a new one for sure.\x02",
    )

    CloseMessageWindow()

    label("loc_1AAF")

    TalkEnd(0xFE)
    Return()

    # Function_5_1704 end

    def Function_6_1AB3(): pass

    label("Function_6_1AB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1F4C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAC")

    ChrTalk(    #66
        0xFE,
        (
            "Apparently we're going to be pulling up\x01",
            "the fallen outrigger by attaching it via\x01",
            "chain...to a howitzer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "That's a rough way of doing it, but we\x01",
            "don't really have any other options.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "It's worth trying, at least.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F49")

    label("loc_1BAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC7")

    ChrTalk(    #69
        0xFE,
        (
            "Pulling the fallen outrigger up by\x01",
            "chaining it to a howitzer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "That's a rough way of doing it, but we\x01",
            "don't really have any other options.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "The society's actions are also cause for\x01",
            "concern, so we need to finish repairs as\x01",
            "soon as possible...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1D83")

    label("loc_1CC7")


    ChrTalk(    #72
        0xFE,
        (
            "The society's actions are also cause for\x01",
            "concern, so we need to finish repairs as\x01",
            "soon as possible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "That's a rough way of doing it, but we\x01",
            "don't really have any other options.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D83")

    Jump("loc_1F49")

    label("loc_1D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E95")

    ChrTalk(    #74
        0xFE,
        (
            "Pulling the fallen outrigger up by\x01",
            "chaining it to a howitzer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "That's a rough way of doing it, but we\x01",
            "don't really have any other options.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "The society's actions are also cause for\x01",
            "concern, so we need to finish repairs as\x01",
            "soon as possible...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1F49")

    label("loc_1E95")


    ChrTalk(    #77
        0xFE,
        (
            "The society's actions are also cause for\x01",
            "concern, so we need to finish repairs as\x01",
            "soon as possible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "That's a rough way of doing it,\x01",
            "but if it works, it'll be worth it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F49")

    Jump("loc_2382")

    label("loc_1F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_2019")

    ChrTalk(    #79
        0xFE,
        (
            "Thanks to that workers-only passage, we're\x01",
            "able to get to where we're going a lot quicker\x01",
            "now, which means getting things done faster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I'm sure repairs will go a lot\x01",
            "more smoothly now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2382")

    label("loc_2019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_21DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2114")

    ChrTalk(    #81
        0xFE,
        (
            "Apparently they're going to build a\x01",
            "workers-only passage outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I'm looking around to see if there\x01",
            "are any appropriate materials for\x01",
            "its construction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Hmm. Maybe I could break down a\x01",
            "container for metal plates...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_21D7")

    label("loc_2114")


    ChrTalk(    #84
        0xFE,
        (
            "I'm looking around to see if there are any\x01",
            "appropriate materials to use in constructing\x01",
            "a workers-only passage outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "...Well, worse comes to worst, we can just\x01",
            "break up a container.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D7")

    Jump("loc_2382")

    label("loc_21DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_2382")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DB")

    ChrTalk(    #86
        0xFE,
        (
            "When that second coup attempt happened,\x01",
            "we brought out these orbal-driven howitzers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "They were all busted during the fight,\x01",
            "but we got them repaired quickly enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "We'd have trouble managing ground combat\x01",
            "without these!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2382")

    label("loc_22DB")


    ChrTalk(    #89
        0xFE,
        (
            "When that second coup happened, we brought\x01",
            "out these orbal-driven howitzers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "They were all busted during the fight,\x01",
            "but we got them repaired quickly enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2382")

    TalkEnd(0xFE)
    Return()

    # Function_6_1AB3 end

    def Function_7_2386(): pass

    label("Function_7_2386")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23AB")
    Call(0, 23)
    Call(0, 24)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_23AB")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF8, 900, 0, -5260, 90)
    SetChrPos(0xF9, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277D")
    OP_A2(0x1E02)

    ChrTalk(    #91
        0x8,
        "Hey! There you are.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2636")

    ChrTalk(    #92
        0x101,
        "#1004F#6PHey, it's Faye!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x107,
        (
            "#560F#1PFaye! Why are you on\x01",
            "the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "Old man Russell brought me along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "He was worried about not having\x01",
            "an engineering team along, so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x107,
        (
            "#064F#1PBut, wait, the Arseille must\x01",
            "have a ship's engineer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "Nah, the old man wanted me\x01",
            "along for stuff other than the ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "I guess you could say I'm here to help\x01",
            "him with his latest crazy gizmos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x107,
        "#067F#1POhhh. I, um, can see that...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2700")

    label("loc_2636")


    ChrTalk(    #100
        0x101,
        (
            "#1004F#6PHey, it's Faye!\x02\x03",

            "What are you doing aboard\x01",
            "the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        "Old man Russell brought me along.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "He was worried about not having\x01",
            "an engineering team along, so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1015F#6POh, okay.\x02",
    )

    CloseMessageWindow()

    label("loc_2700")


    ChrTalk(    #104
        0x8,
        (
            "Right now he doesn't need me for much,\x01",
            "so I'm helping out where I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "So, you guys want to use the lift, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_27B5")

    label("loc_277D")


    ChrTalk(    #106
        0xFE,
        "Hey, gang.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "You headin' down to Esmelas Tower?\x02",
    )

    CloseMessageWindow()

    label("loc_27B5")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Descend On The Lift\x01",      # 0
            "Not Just Yet\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286B")

    ChrTalk(    #108
        0xFE,
        (
            "All right, then. When you're\x01",
            "ready, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_286B")


    ChrTalk(    #109
        0x8,
        "Right, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "Okay, just jump on the\x01",
            "plate there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#1006F#6POkay!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2029, 0, -710, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -600, -100, -600, 180)
    SetChrPos(0x102, 600, -100, -600, 180)
    SetChrPos(0xF8, -600, -100, 600, 180)
    SetChrPos(0xF9, 600, -100, 600, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #112
        0xFE,
        "#2PAnd down you go!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "#2PIt should be pretty stable, but,\x01",
            "uh...try to avoid the edges.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0xA)
    OP_22(0xF7, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x101,
        "#1004F#5PWaa-aah!\x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x100000)
    OP_22(0x68, 0x0, 0x64)
    OP_6F(0x5, 10)
    OP_70(0x5, 0x3C)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_2386 end

    def Function_8_2A2B(): pass

    label("Function_8_2A2B")

    EventBegin(0x0)
    OP_6D(0, -250, 0, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -620, -4000, -820, 180)
    SetChrPos(0x102, 750, -4000, -780, 180)
    SetChrPos(0xF8, -700, -4000, 280, 180)
    SetChrPos(0xF9, 600, -4000, 290, 180)
    ClearMapFlags(0x100000)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_73(0x5)
    OP_23(0x68)
    OP_22(0xF7, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(70, 0, -3620, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 70, 0, -3620, 180)
    SetChrPos(0x1, 70, 0, -3620, 180)
    SetChrPos(0x2, 70, 0, -3620, 180)
    SetChrPos(0x3, 70, 0, -3620, 180)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_8_2A2B end

    def Function_9_2B6A(): pass

    label("Function_9_2B6A")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF8, 900, 0, -5260, 90)
    SetChrPos(0xF9, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #115
        0x8,
        "Hey, gang.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        "You headin' down to Esmelas Tower?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Descend On The Lift\x01",      # 0
            "Not Just Yet\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CEC")

    ChrTalk(    #117
        0x8,
        (
            "All right, then. When you're\x01",
            "ready, say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_2CEC")


    ChrTalk(    #118
        0x8,
        "Right, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "Just jump on the plate\x01",
            "and you'll be off.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/R0303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2B6A end

    def Function_10_2D49(): pass

    label("Function_10_2D49")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D6E")
    Call(0, 23)
    Call(0, 25)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2D6E")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(500)

    ChrTalk(    #120
        0xFE,
        "Hey, gang. Good work so far!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Ready to head down to\x01",
            "Carnelia Tower?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Descend On The Lift\x01",      # 0
            "Not Just Yet\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F03")

    ChrTalk(    #122
        0xFE,
        (
            "All right, then. When you're\x01",
            "ready, say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_2F03")


    ChrTalk(    #123
        0xFE,
        "Right, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Just jump on the plate\x01",
            "and you'll be off.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2D49 end

    def Function_11_2F60(): pass

    label("Function_11_2F60")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F85")
    Call(0, 23)
    Call(0, 25)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_2F85")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #125
        0xFE,
        "やあ、お疲れさん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "《紅蓮の塔》の手前に降りるかい？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【リフトで降りる】\x01",      # 0
            "【まだ用事がある】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3100")

    ChrTalk(    #127
        0xFE,
        (
            "わかった。\x01",
            "必要なら声をかけてよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_3100")


    ChrTalk(    #128
        0xFE,
        "ん、わかった。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "それじゃあ早速、\x01",
            "リフトの上に乗っちゃって。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R3104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2F60 end

    def Function_12_3161(): pass

    label("Function_12_3161")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3186")
    Call(0, 23)
    Call(0, 26)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_3186")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #130
        0x8,
        (
            "You guys are really working it.\x01",
            "Keep it up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "Time to attack the Sapphirl\x01",
            "Tower, I bet.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Descend On The Lift\x01",      # 0
            "Not Just Yet\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332E")

    ChrTalk(    #132
        0xFE,
        (
            "All right, then. When you're\x01",
            "ready, say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_332E")


    ChrTalk(    #133
        0xFE,
        "Right, then!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "Just jump on the plate\x01",
            "and you'll be off.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3161 end

    def Function_13_338B(): pass

    label("Function_13_338B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33B0")
    Call(0, 23)
    Call(0, 26)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_33B0")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #135
        0x8,
        "やあ、お疲れさん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        "《紺碧の塔》の手前に降りるかい？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【リフトで降りる】\x01",      # 0
            "【まだ用事がある】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352B")

    ChrTalk(    #137
        0xFE,
        (
            "わかった。\x01",
            "必要なら声をかけてよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_352B")


    ChrTalk(    #138
        0xFE,
        "ん、わかった。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "それじゃあ早速、\x01",
            "リフトの上に乗っちゃって。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_338B end

    def Function_14_358C(): pass

    label("Function_14_358C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35B1")
    Call(0, 23)
    Call(0, 24)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_35B1")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #140
        0x8,
        (
            "Last tower. Keep going, guys.\x01",
            "You can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        "You ready to head down?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Descend On The Lift\x01",      # 0
            "Not Just Yet\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3748")

    ChrTalk(    #142
        0xFE,
        (
            "No problem. Just give the\x01",
            "word when you're ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_3748")


    ChrTalk(    #143
        0xFE,
        "Okay, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "You know what to do. And guys?\x01",
            "May Aidios be with you.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_358C end

    def Function_15_37B1(): pass

    label("Function_15_37B1")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37D6")
    Call(0, 23)
    Call(0, 24)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_37D6")

    Fade(1000)
    OP_6D(3010, 0, -4350, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(3150, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2200, 0, -5260, 90)
    SetChrPos(0x102, 2200, 0, -4400, 90)
    SetChrPos(0xF9, 900, 0, -5260, 90)
    SetChrPos(0xF8, 900, 0, -4400, 90)
    OP_8C(0x8, 270, 0)
    OP_4A(0x8, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #145
        0x8,
        "いよいよ最後の塔だね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        "《琥珀の塔》の手前に降りるかい？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【リフトで降りる】\x01",      # 0
            "【まだ用事がある】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3955")

    ChrTalk(    #147
        0xFE,
        (
            "わかった。\x01",
            "必要なら声をかけてよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    label("loc_3955")


    ChrTalk(    #148
        0xFE,
        "ん、わかった。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "それじゃあ早速、\x01",
            "リフトの上に乗っちゃって。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_37B1 end

    def Function_16_39B6(): pass

    label("Function_16_39B6")

    Sleep(300)
    Fade(500)
    OP_6D(2029, 0, -710, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -600, -100, -600, 180)
    SetChrPos(0x102, 600, -100, -600, 180)
    SetChrPos(0xF8, -600, -100, 600, 180)
    SetChrPos(0xF9, 600, -100, 600, 180)
    OP_0D()
    Sleep(300)
    OP_8C(0x8, 90, 400)
    Sleep(1000)
    OP_6F(0x5, 0)
    OP_70(0x5, 0xA)
    OP_22(0xF7, 0x0, 0x64)
    Sleep(1000)
    SetMapFlags(0x100000)
    OP_22(0x68, 0x0, 0x64)
    OP_6F(0x5, 10)
    OP_70(0x5, 0x3C)
    Sleep(1000)
    Return()

    # Function_16_39B6 end

    def Function_17_3A89(): pass

    label("Function_17_3A89")

    OP_8E(0xFE, 0xFFFFFDDA, 0xFFFFFF06, 0xFFFFFDDA, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_3A89 end

    def Function_18_3AA5(): pass

    label("Function_18_3AA5")

    OP_8E(0xFE, 0xFFFFFDDA, 0xFFFFFF06, 0x226, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_3AA5 end

    def Function_19_3AC1(): pass

    label("Function_19_3AC1")

    OP_8E(0xFE, 0x226, 0xFFFFFF06, 0xFFFFFDDA, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_3AC1 end

    def Function_20_3ADD(): pass

    label("Function_20_3ADD")

    OP_8E(0xFE, 0x226, 0x0, 0x11B2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x226, 0xFFFFFF06, 0x226, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_20_3ADD end

    def Function_21_3B0D(): pass

    label("Function_21_3B0D")

    OP_8E(0xFE, 0x8B6, 0x0, 0x18D8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_21_3B0D end

    def Function_22_3B29(): pass

    label("Function_22_3B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3B61")
    EventBegin(0x2)
    FadeToDark(500, 0, -1)
    OP_8C(0x0, 180, 0)
    OP_91(0x0, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
    OP_0D()
    NewScene("ED6_DT21/C5900   ._SN", 102, 0, 0)
    IdleLoop()

    label("loc_3B61")

    Return()

    # Function_22_3B29 end

    def Function_23_3B62(): pass

    label("Function_23_3B62")

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
        (0, "loc_3BDB"),
        (1, "loc_3BE1"),
        (SWITCH_DEFAULT, "loc_3BE7"),
    )


    label("loc_3BDB")

    OP_A2(0x1200)
    Jump("loc_3BE7")

    label("loc_3BE1")

    OP_A2(0x1201)
    Jump("loc_3BE7")

    label("loc_3BE7")

    Return()

    # Function_23_3B62 end

    def Function_24_3BE8(): pass

    label("Function_24_3BE8")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_24_3BE8 end

    def Function_25_3C77(): pass

    label("Function_25_3C77")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_25_3C77 end

    def Function_26_3D04(): pass

    label("Function_26_3D04")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_26_3D04 end

    def Function_27_3D91(): pass

    label("Function_27_3D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E05")
    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #150
        "\x07\x05The door is tightly closed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_3E05")

    Return()

    # Function_27_3D91 end

    SaveToFile()

Try(main)
