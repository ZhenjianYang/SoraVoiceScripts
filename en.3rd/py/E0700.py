from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0700   ._SN',
        MapName             = 'Event',
        Location            = 'E0700.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        'Dorothy',                              # 9
        'Gull',                                 # 10
        'Gull',                                 # 11
        'Gull',                                 # 12
        'Gull',                                 # 13
        'Gull',                                 # 14
        'Armand',                               # 15
        'Ellie',                                # 16
        'Passenger',                            # 17
        'Child',                                # 18
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT06/CH20063 ._CH',             # 00
        'ED6_DT06/CH20064 ._CH',             # 01
        'ED6_DT07/CH01740 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01160 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT06/CH20063P._CP',             # 00
        'ED6_DT06/CH20064P._CP',             # 01
        'ED6_DT07/CH01740P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01160P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2850,
        Z                   = 5000,
        Y                   = -3440,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2910,
        Z                   = 5000,
        Y                   = -4850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -20,
        Z                   = 5000,
        Y                   = -8840,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -20,
        Z                   = 5000,
        Y                   = -10140,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_241",          # 01, 1
        "Function_2_253",          # 02, 2
        "Function_3_3D0",          # 03, 3
        "Function_4_3F4",          # 04, 4
        "Function_5_487",          # 05, 5
        "Function_6_5FC",          # 06, 6
        "Function_7_7A1",          # 07, 7
        "Function_8_939",          # 08, 8
        "Function_9_A4D",          # 09, 9
        "Function_10_16F2",        # 0A, 10
        "Function_11_172E",        # 0B, 11
        "Function_12_177A",        # 0C, 12
        "Function_13_18C7",        # 0D, 13
        "Function_14_193F",        # 0E, 14
        "Function_15_19CB",        # 0F, 15
        "Function_16_1A57",        # 10, 16
        "Function_17_1ACF",        # 11, 17
        "Function_18_1B6E",        # 12, 18
        "Function_19_1B91",        # 13, 19
        "Function_20_1BB4",        # 14, 20
        "Function_21_1BD7",        # 15, 21
        "Function_22_1BFA",        # 16, 22
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_239")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    Event(0, 9)

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 6)), scpexpr(EXPR_END)), "loc_240")

    label("loc_240")

    Return()

    # Function_0_222 end

    def Function_1_241(): pass

    label("Function_1_241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 6)), scpexpr(EXPR_END)), "loc_252")
    OP_22(0x79, 0x1, 0x46)
    OP_22(0x1C3, 0x1, 0x64)

    label("loc_252")

    Return()

    # Function_1_241 end

    def Function_2_253(): pass

    label("Function_2_253")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_278")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3BA")

    label("loc_278")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3BA")

    label("loc_291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3BA")

    label("loc_2AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3BA")

    label("loc_2C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3BA")

    label("loc_2DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3BA")

    label("loc_2F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3BA")

    label("loc_30E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3BA")

    label("loc_327")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_340")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3BA")

    label("loc_340")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_359")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3BA")

    label("loc_359")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3BA")

    label("loc_372")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3BA")

    label("loc_38B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3BA")

    label("loc_3A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3CF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3BA")

    label("loc_3CF")

    Return()

    # Function_2_253 end

    def Function_3_3D0(): pass

    label("Function_3_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3")
    OP_8D(0xFE, 1100, -9840, -1100, -10840, 2000)
    Jump("Function_3_3D0")

    label("loc_3F3")

    Return()

    # Function_3_3D0 end

    def Function_4_3F4(): pass

    label("Function_4_3F4")

    TalkBegin(0xFE)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    ChrTalk(    #0
        0x10,
        (
            "#150F◆That onion hotpot I had over in Calvard really\x01",
            "was amazing.\x02\x03",

            "◆Heehee. I'm drooling just thinking of it. ♪\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_3F4 end

    def Function_5_487(): pass

    label("Function_5_487")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_54B")

    ChrTalk(    #1
        0xFE,
        (
            "I think we'd probably be best going for\x01",
            "somewhere that feels warm and homey,\x01",
            "even if it's not that big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Something like a house on a hill near a forest...\x01",
            "What do you think?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F8")

    label("loc_54B")


    ChrTalk(    #3
        0xFE,
        "We're finally back home in Liberl!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "*cough* Which means it's time to start thinking\x01",
            "of getting a house for ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "What kind of house would you like?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x25B9)

    label("loc_5F8")

    TalkEnd(0xFE)
    Return()

    # Function_5_487 end

    def Function_6_5FC(): pass

    label("Function_6_5FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6BA")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #6
        0xFE,
        (
            "Heehee. I can't believe he's already thinking\x01",
            "of finding a place for us to live!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "But that does sound like the perfect place to\x01",
            "start a lovely, happy family. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79D")

    label("loc_6BA")


    ChrTalk(    #8
        0xFE,
        (
            "The two of us have spent the past half a year\x01",
            "traveling all around the continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "I couldn't have wished for a better honeymoon.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0xFE,
        "I'm so glad I chose him to spend my life with...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x25BA)

    label("loc_79D")

    TalkEnd(0xFE)
    Return()

    # Function_6_5FC end

    def Function_7_7A1(): pass

    label("Function_7_7A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_7E4")

    ChrTalk(    #11
        0xFE,
        "*sigh* I wish I could be as carefree as he is...\x02",
    )

    CloseMessageWindow()
    Jump("loc_935")

    label("loc_7E4")


    ChrTalk(    #12
        0xFE,
        "My wife... My wife...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "My wife went back to her family's home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I mean, I'm as aware as anyone that I've been\x01",
            "so busy with work lately that I haven't been able\x01",
            "to spend any time with her, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "*sigh* If I'd known it was going to come to this,\x01",
            "I would have sat down and talked to her about it\x01",
            "a long time ago...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x25BB)

    label("loc_935")

    TalkEnd(0xFE)
    Return()

    # Function_7_7A1 end

    def Function_8_939(): pass

    label("Function_8_939")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A0A")

    ChrTalk(    #16
        0xFE,
        "Heehee. We're gonna see Mommy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "You wanna come?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1068FI'm not sure you should be inviting complete\x01",
            "strangers to family gatherings, kiddo.\x02\x03",

            "#1066FYou go have fun with your mom, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A49")

    label("loc_A0A")


    ChrTalk(    #19
        0xFE,
        "Heehee. Wheeeee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "Being out here feels amazing!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    OP_A2(0x25BC)

    label("loc_A49")

    TalkEnd(0xFE)
    Return()

    # Function_8_939 end

    def Function_9_A4D(): pass

    label("Function_9_A4D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_23(0x79)
    OP_23(0x1C3)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS537._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(3000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0xFFEC, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS538._CH")
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(5000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C4(0x0, 0x4000)
    SetChrPos(0x109, 150, 5100, -360, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 3000, 5000, -3240, 90)
    OP_4A(0x10, 255)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x11, 15000, 8200, -12100, 0)
    SetChrPos(0x12, 16100, 7900, -11100, 0)
    SetChrPos(0x13, 18100, 8200, -10000, 0)
    SetChrPos(0x14, 19800, 8100, -11000, 0)
    SetChrPos(0x15, 22000, 8300, -11800, 0)
    OP_43(0x11, 0x2, 0x0, 0xD)
    OP_43(0x12, 0x2, 0x0, 0xE)
    OP_43(0x13, 0x2, 0x0, 0xF)
    OP_43(0x14, 0x2, 0x0, 0x10)
    OP_43(0x15, 0x2, 0x0, 0x11)
    OP_6D(5330, 5100, 38370, 0)
    OP_67(0, 14100, -10000, 0)
    OP_6B(5120, 0)
    OP_6C(225000, 0)
    OP_6E(457, 0)
    LoadEffect(0x0, "map\\mp032_00.eff")
    OP_43(0x10, 0x0, 0x0, 0xC)

    def lambda_C62():

        label("loc_C62")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_C62")

    QueueWorkItem2(0x10, 1, lambda_C62)

    def lambda_C73():
        OP_6D(6370, 3250, -2770, 13000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C73)

    def lambda_C8B():
        OP_67(0, 6310, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C8B)

    def lambda_CA3():
        OP_6B(5720, 11000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CA3)

    def lambda_CB3():
        OP_6C(225000, 11000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_CB3)

    def lambda_CC3():
        OP_6E(490, 11000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_CC3)
    OP_1D(0x1)
    OP_22(0x1C3, 0x1, 0x64)
    OP_43(0x16, 0x1, 0x0, 0xA)
    FadeToBright(3000, 0)
    Sleep(5000)
    OP_C8(0x80, 0x172, "C_PLAC30._CH", 0x1, 0x3E8)
    WaitChrThread(0x109, 0x0)

    def lambda_D09():
        OP_6D(8630, 4000, -6870, 12000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D09)

    def lambda_D21():
        OP_67(0, 8000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D21)

    def lambda_D39():
        OP_6B(4500, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D39)

    def lambda_D49():
        OP_6C(327000, 13000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_D49)

    def lambda_D59():
        OP_6E(490, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_D59)
    Sleep(3500)
    OP_A2(0x1)
    WaitChrThread(0x11, 0x2)
    WaitChrThread(0x12, 0x2)
    WaitChrThread(0x13, 0x2)
    WaitChrThread(0x14, 0x2)
    WaitChrThread(0x15, 0x2)
    OP_43(0x11, 0x2, 0x0, 0x12)
    OP_43(0x12, 0x2, 0x0, 0x13)
    OP_43(0x13, 0x2, 0x0, 0x14)
    OP_43(0x14, 0x2, 0x0, 0x15)
    OP_43(0x15, 0x2, 0x0, 0x16)
    Sleep(2000)

    def lambda_DB2():
        OP_6D(8630, 4000, -2870, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DB2)
    OP_44(0x10, 0x1)
    OP_8C(0x10, 180, 400)
    OP_8F(0x10, 0xBF4, 0x1388, 0xFFFFEF52, 0x7D0, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_23(0x155)
    Fade(1000)
    OP_24(0x79, 0x46)
    OP_6D(2320, 5000, -4880, 0)
    OP_67(0, 6700, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(224000, 0)
    OP_6E(239, 0)
    OP_0D()
    Sleep(100)
    OP_44(0x10, 0x0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #21
        0x10,
        (
            "#150F#5PAww... They've gone out of sight now.\x02\x03",

            "I wonder if they're busy migrating? It looks like\x01",
            "they can't keep up with this ship, though.\x01",
            "Guess not every bird can be as fast as Sieg...\x02\x03",

            "#151FBut they were just the cyuuutest! ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(600)

    NpcTalk(    #22
        0x109,
        "Young Man's Voice",
        "#1PWell, look who it is!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(-220, 5100, -960, 0)
    OP_67(0, 4820, -10000, 0)
    OP_6B(3850, 0)
    OP_6C(315000, 0)
    OP_6E(207, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_43(0x109, 0x0, 0x0, 0xB)

    def lambda_FFD():
        OP_6D(1230, 5000, -3040, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_FFD)

    def lambda_1015():
        OP_67(0, 4820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1015)

    def lambda_102D():
        OP_6B(3850, 3000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_102D)

    def lambda_103D():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_103D)

    def lambda_104D():
        OP_6E(207, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_104D)

    def lambda_105D():

        label("loc_105D")

        TurnDirection(0x10, 0x109, 400)
        OP_48()
        Jump("loc_105D")

    QueueWorkItem2(0x109, 3, lambda_105D)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10, 0x0)

    ChrTalk(    #23
        0x10,
        "#153FI-I know you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1061F#5PIt really is you! Long time no see, Dorothy!\x02\x03",

            "#1062FI sure wasn't expecting to run into you here. \x01",
            "Funny coincidence, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#151F#6PHeehee. It really is!\x02\x03",

            "It's good to see you again, too...uhhh...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #26
        0x10,
        "#153F#6P...Fatheeer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1064F#5P...\x02\x03",

            "#1068F...You don't remember my name, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "#151F#6PD-Don't be silly! Of course I do!\x02\x03",

            "#155FIt's...uhhh....\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #29
        0x10,
        "#151F#6P#3SOh, I remember! It's Onion Graham!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1062F#5PBut of course! How lucky I am to have been\x01",
            "named after such a multi-purpose plant?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #31
        0x109,
        "#1068F#5P#3SThat's not even a NAME, Dorothy!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #32
        0x109,
        (
            "#1063F#5PYou really did forget, didn't you?\x02\x03",

            "And yet you somehow managed to remember\x01",
            "my last name like it was nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#151F#6PHeehee. I was just being silly.\x02\x03",

            "#150FA couple of days ago, I had this amaaazing \x01",
            "onion hotpot over in the Eastern Quarter in\x01",
            "Calvard, so I've still got onions on the brain.\x02\x03",

            "I couldn't believe a hotpot with just onions in\x01",
            "it could taste that good, but I swear it did!\x01",
            "It was so comforting and sweet!\x02\x03",

            "#151FSo that's how I ended up saying onion instead\x01",
            "of your name.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #34
        0x109,
        (
            "#1068F#5P*sigh* Well, whatever...\x02\x03",

            "#1066FSo if you insist you haven't forgotten,\x01",
            "what IS my name, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "#150F#6PI DO insist. I'd never forget!\x02\x03",

            "#151F#3SIt's lovely to see you again, Jasmine Graham!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1061F#5PBut of course! How lucky I am to have been\x01",
            "named after such a fragrant plant?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #37
        0x109,
        (
            "#1069F#3S#5PThat might be an actual name this time,\x01",
            "but it's a WOMAN'S name!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0710   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_9_A4D end

    def Function_10_16F2(): pass

    label("Function_10_16F2")

    OP_22(0x79, 0x1, 0x0)
    Sleep(200)
    OP_24(0x79, 0xA)
    Sleep(200)
    OP_24(0x79, 0x14)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Return()

    # Function_10_16F2 end

    def Function_11_172E(): pass

    label("Function_11_172E")

    OP_8E(0xFE, 0xF0, 0x1388, 0xFFFFF7F4, 0x7D0, 0x0)
    OP_71(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0x5FA, 0x1388, 0xFFFFF038, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_11_172E end

    def Function_12_177A(): pass

    label("Function_12_177A")

    Sleep(5000)

    label("loc_177F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18C6")
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_22(0x7C, 0x0, 0x32)
    PlayEffect(0x0, 0xFF, 0x10, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_177F")

    label("loc_18C6")

    Return()

    # Function_12_177A end

    def Function_13_18C7(): pass

    label("Function_13_18C7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_193E")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(6300)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x3A98, 0x2328, 0xFFFFC75C, 0x320, 0x0)

    def lambda_1909():

        label("loc_1909")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_1909")

    QueueWorkItem2(0xFE, 3, lambda_1909)
    OP_8F(0xFE, 0x3A98, 0x2008, 0xFFFFD0BC, 0x320, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_193B")
    Jump("loc_193E")

    label("loc_193B")

    Jump("Function_13_18C7")

    label("loc_193E")

    Return()

    # Function_13_18C7 end

    def Function_14_193F(): pass

    label("Function_14_193F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19CA")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(3000)

    def lambda_1964():

        label("loc_1964")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_1964")

    QueueWorkItem2(0xFE, 3, lambda_1964)
    OP_8F(0xFE, 0x3E80, 0x1CE8, 0xFFFFDAE4, 0x3E8, 0x0)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x3EE4, 0x206C, 0xFFFFD88C, 0x1F4, 0x0)
    OP_8F(0xFE, 0x3EE4, 0x1EDC, 0xFFFFD4A4, 0x1F4, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19C7")
    Jump("loc_19CA")

    label("loc_19C7")

    Jump("Function_14_193F")

    label("loc_19CA")

    Return()

    # Function_14_193F end

    def Function_15_19CB(): pass

    label("Function_15_19CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A56")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(2400)
    OP_8F(0xFE, 0x46B4, 0x2328, 0xFFFFDE68, 0x320, 0x0)

    def lambda_1A04():

        label("loc_1A04")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_1A04")

    QueueWorkItem2(0xFE, 3, lambda_1A04)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x46B4, 0x2134, 0xFFFFDCD8, 0x384, 0x0)
    OP_8F(0xFE, 0x46B4, 0x2008, 0xFFFFD8F0, 0x384, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A53")
    Jump("loc_1A56")

    label("loc_1A53")

    Jump("Function_15_19CB")

    label("loc_1A56")

    Return()

    # Function_15_19CB end

    def Function_16_1A57(): pass

    label("Function_16_1A57")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1ACE")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(3000)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x4D58, 0x1BBC, 0xFFFFD120, 0x320, 0x0)

    def lambda_1A99():

        label("loc_1A99")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_1A99")

    QueueWorkItem2(0xFE, 3, lambda_1A99)
    OP_8F(0xFE, 0x4D58, 0x1FA4, 0xFFFFD508, 0x384, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1ACB")
    Jump("loc_1ACE")

    label("loc_1ACB")

    Jump("Function_16_1A57")

    label("loc_1ACE")

    Return()

    # Function_16_1A57 end

    def Function_17_1ACF(): pass

    label("Function_17_1ACF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B6D")
    SetChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    OP_22(0x155, 0x1, 0x32)
    Sleep(2200)
    OP_44(0xFE, 0x3)
    SetChrSubChip(0xFE, 7)
    OP_8F(0xFE, 0x55F0, 0x2328, 0xFFFFCE00, 0x320, 0x0)

    def lambda_1B11():

        label("loc_1B11")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1B11")

    QueueWorkItem2(0xFE, 3, lambda_1B11)
    OP_8F(0xFE, 0x55F0, 0x1F40, 0xFFFFCE00, 0x320, 0x0)

    def lambda_1B38():

        label("loc_1B38")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_1B38")

    QueueWorkItem2(0xFE, 3, lambda_1B38)
    OP_8F(0xFE, 0x55F0, 0x206C, 0xFFFFD1E8, 0x44C, 0x0)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B6A")
    Jump("loc_1B6D")

    label("loc_1B6A")

    Jump("Function_17_1ACF")

    label("loc_1B6D")

    Return()

    # Function_17_1ACF end

    def Function_18_1B6E(): pass

    label("Function_18_1B6E")

    Sleep(300)
    OP_8F(0xFE, 0x3A98, 0x2008, 0xFFFF8A6C, 0x9C4, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_1B6E end

    def Function_19_1B91(): pass

    label("Function_19_1B91")

    Sleep(400)
    OP_8F(0xFE, 0x3EE4, 0x1EDC, 0xFFFF8A6C, 0x8FC, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_1B91 end

    def Function_20_1BB4(): pass

    label("Function_20_1BB4")

    Sleep(500)
    OP_8F(0xFE, 0x46B4, 0x2008, 0xFFFF8AD0, 0x898, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_1BB4 end

    def Function_21_1BD7(): pass

    label("Function_21_1BD7")

    Sleep(450)
    OP_8F(0xFE, 0x4D58, 0x1FA4, 0xFFFF8AD0, 0x8CA, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_1BD7 end

    def Function_22_1BFA(): pass

    label("Function_22_1BFA")

    Sleep(350)
    OP_8F(0xFE, 0x55F0, 0x206C, 0xFFFF87B0, 0x992, 0x0)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_1BFA end

    SaveToFile()

Try(main)
