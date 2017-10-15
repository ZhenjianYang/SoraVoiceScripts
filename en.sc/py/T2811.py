from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2811   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2811.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Deborah',                              # 11
        'Targeting Camera',                     # 12
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH02393 ._CH',             # 03
        'ED6_DT07/CH02553 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH02393P._CP',             # 03
        'ED6_DT07/CH02553P._CP',             # 04
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_176",          # 00, 0
        "Function_1_18A",          # 01, 1
        "Function_2_1DD",          # 02, 2
        "Function_3_35A",          # 03, 3
        "Function_4_35F",          # 04, 4
        "Function_5_578",          # 05, 5
        "Function_6_77D",          # 06, 6
        "Function_7_A2B",          # 07, 7
        "Function_8_A4F",          # 08, 8
        "Function_9_1421",         # 09, 9
        "Function_10_1CAF",        # 0A, 10
    )


    def Function_0_176(): pass

    label("Function_0_176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_189")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 7)

    label("loc_189")

    Return()

    # Function_0_176 end

    def Function_1_18A(): pass

    label("Function_1_18A")

    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -1810, 300, -1250, 269)
    SetChrPos(0x9, -3520, 300, 200, 158)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    Return()

    # Function_1_18A end

    def Function_2_1DD(): pass

    label("Function_2_1DD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_344")

    label("loc_202")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_344")

    label("loc_21B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_234")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_344")

    label("loc_234")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_344")

    label("loc_24D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_266")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_344")

    label("loc_266")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_344")

    label("loc_27F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_298")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_344")

    label("loc_298")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_344")

    label("loc_2B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_344")

    label("loc_2CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_344")

    label("loc_2E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_344")

    label("loc_2FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_344")

    label("loc_315")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_344")

    label("loc_32E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_344")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_359")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_344")

    label("loc_359")

    Return()

    # Function_2_1DD end

    def Function_3_35A(): pass

    label("Function_3_35A")

    Call(0, 4)
    Return()

    # Function_3_35A end

    def Function_4_35F(): pass

    label("Function_4_35F")

    TalkBegin(0xA)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                               # 0
            "Shop\x01",                               # 1
            "[Young Lady Plate] - 800 mira\x01",      # 2
            "Leave\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x72)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_3DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B9")
    SubMira(800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06Ate #2CYoung Lady Plate#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x4B0)
    OP_31(0x1, 0xFD, 0x4B0)
    OP_31(0x2, 0xFD, 0x4B0)
    OP_31(0x3, 0xFD, 0x4B0)
    OP_31(0x4, 0xFD, 0x4B0)
    OP_31(0x5, 0xFD, 0x4B0)
    OP_31(0x6, 0xFD, 0x4B0)
    OP_31(0x7, 0xFD, 0x4B0)
    OP_31(0x8, 0xFD, 0x4B0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_479")
    Jump("loc_4AB")

    label("loc_479")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06Learned [#2CYoung Lady Plate#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_4AB")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_4E1")

    label("loc_4B9")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_4E1")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xA)
    Return()

    label("loc_4F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50D")
    FadeToBright(300, 0)
    TalkEnd(0xA)
    Return()

    label("loc_50D")

    FadeToBright(300, 0)

    ChrTalk(    #3
        0xA,
        (
            "Where are you heading off\x01",
            "to at a time like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        "It's dark outside, so be careful.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_4_35F end

    def Function_5_578(): pass

    label("Function_5_578")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_59D")
    SetChrSubChip(0x8, 2)
    Jump("loc_5CE")

    label("loc_59D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B3")
    SetChrSubChip(0x8, 1)
    Jump("loc_5CE")

    label("loc_5B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C9")
    SetChrSubChip(0x8, 0)
    Jump("loc_5CE")

    label("loc_5C9")

    SetChrSubChip(0x8, 2)

    label("loc_5CE")

    OP_8C(0x8, 269, 0)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_END)), "loc_6B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_672")

    ChrTalk(    #5
        0x8,
        (
            "#640FA secret underground room, huh?\x02\x03",

            "And you've got those weird card\x01",
            "riddles to deal with on top of that.\x01",
            "Sure sounds fun to me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B3")

    label("loc_672")

    OP_A2(0x0)

    ChrTalk(    #6
        0x8,
        (
            "#640FA secret underground room, huh?\x02\x03",

            "The plot thickens!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B3")

    Jump("loc_774")

    label("loc_6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_774")

    ChrTalk(    #7
        0x8,
        (
            "#640FI don't think either of us wanna\x01",
            "slow you guys down, so we'll wait\x01",
            "here. Sound good?\x02\x03",

            "And be careful, okay?\x01",
            "I'm expecting some fun anecdotes\x01",
            "once this is all said and done!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_774")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_5_578 end

    def Function_6_77D(): pass

    label("Function_6_77D")

    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A2")
    SetChrSubChip(0x9, 1)
    Jump("loc_7D3")

    label("loc_7A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xE1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B8")
    SetChrSubChip(0x9, 0)
    Jump("loc_7D3")

    label("loc_7B8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CE")
    SetChrSubChip(0x9, 2)
    Jump("loc_7D3")

    label("loc_7CE")

    SetChrSubChip(0x9, 0)

    label("loc_7D3")

    OP_8C(0x9, 172, 0)
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 2)), scpexpr(EXPR_END)), "loc_9D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8A1")

    ChrTalk(    #8
        0x9,
        (
            "#730FSure, it's a spooky schoolhouse\x01",
            "now, but before that it was an old\x01",
            "fortress.\x02\x03",

            "It wouldn't be all that surprising\x01",
            "if it ended up having a few secret\x01",
            "underground rooms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CE")

    label("loc_8A1")

    OP_A2(0x1)

    ChrTalk(    #9
        0x9,
        (
            "#730FA hidden staircase?\x02\x03",

            "There wasn't anything like that\x01",
            "mentioned in the documents.\x02\x03",

            "Anything's possible, though. I never\x01",
            "told you this, but before it was a spooky\x01",
            "schoolhouse, it was an old fortress.\x02\x03",

            "It wouldn't be all that surprising\x01",
            "if it ended up having a few secret\x01",
            "underground rooms.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CE")

    Jump("loc_A22")

    label("loc_9D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_A22")

    ChrTalk(    #10
        0x9,
        (
            "#730FWe'll be on standby here in case\x01",
            "anything happens.\x02\x03",

            "Be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A22")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_6_77D end

    def Function_7_A2B(): pass

    label("Function_7_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3C")
    Call(0, 10)

    label("loc_A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A4A")
    Call(0, 8)
    Jump("loc_A4E")

    label("loc_A4A")

    Call(0, 9)

    label("loc_A4E")

    Return()

    # Function_7_A2B end

    def Function_8_A4F(): pass

    label("Function_8_A4F")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrPos(0x101, 240, 0, -2890, 225)
    SetChrPos(0xF7, 560, 0, -3920, 275)
    SetChrPos(0x105, -600, 0, -2190, 185)
    SetChrPos(0x104, -260, 0, -5270, 0)
    SetChrPos(0x127, -1510, 0, -5190, 45)
    SetChrPos(0x8, -1990, 0, -4400, 45)
    SetChrPos(0x9, -8610, 0, -3090, 90)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_6D(1300, 0, 4690, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)

    def lambda_B3C():
        OP_6D(-120, 0, -3010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B3C)

    def lambda_B54():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B54)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_B8A():

        label("loc_B8A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_B8A")

    QueueWorkItem2(0x101, 1, lambda_B8A)

    def lambda_B9B():

        label("loc_B9B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_B9B")

    QueueWorkItem2(0xF7, 1, lambda_B9B)

    def lambda_BAC():

        label("loc_BAC")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_BAC")

    QueueWorkItem2(0x105, 1, lambda_BAC)

    def lambda_BBD():

        label("loc_BBD")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_BBD")

    QueueWorkItem2(0x104, 1, lambda_BBD)

    def lambda_BCE():

        label("loc_BCE")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_BCE")

    QueueWorkItem2(0x127, 1, lambda_BCE)

    def lambda_BDF():

        label("loc_BDF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_BDF")

    QueueWorkItem2(0x8, 1, lambda_BDF)

    def lambda_BF0():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_BF0)

    def lambda_C02():
        OP_8E(0xFE, 0xFFFFF63C, 0x0, 0xFFFFF36C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C02)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #11
        0x9,
        (
            "#730F#3PAll right, I got the key to the back\x01",
            "gate from the teachers.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x9, 0x101, 0x3E8, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #12
        "\x07\x00Received #1011i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x3F3, 1)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x127, 0x1)
    OP_44(0x8, 0x1)
    OP_8F(0x9, 0xFFFFF768, 0x0, 0xFFFFF36C, 0x7D0, 0x0)

    ChrTalk(    #13
        0x101,
        "#1006FThanks, Hans!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x106,
        (
            "#552FI'm glad you're fired up,\x01",
            "but...you sure you're okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #15
        0x101,
        (
            "#1019FOf course I'm okay! Why wouldn't I be okay?\x01",
            "When have I ever given the impression\x01",
            "ghosts paralyze me with fear? That's silly!\x02\x03",

            "We're gonna go into this schoolhouse,\x01",
            "punch the ghost in the face, and drag\x01",
            "him back to the guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x106,
        "#055FUh... If you say so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#031F#4PHeh heh. We're finally entering Estelle's\x01",
            "element, it seems.\x02\x03",

            "#030FWell, then.\x01",
            "Let us begin our test of courage.\x02\x03",

            "Monsters may have taken root in the ruin,\x01",
            "so only those skilled at the art of combat\x01",
            "should enter.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #18
        0x106,
        (
            "#053FGood thinking. (For once...)\x02\x03",

            "#050FThe camera girl can come, but\x01",
            "the others should stay behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#648F#5PYeah, I know. We'll leave everything\x01",
            "to you big, tough fighting-types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "#730F#3PWe'll be waiting here in case\x01",
            "something happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x105,
        (
            "#043FUm... Agate?\x02\x03",

            "May I...accompany you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1078():
        TurnDirection(0x101, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1078)

    ChrTalk(    #22
        0x106,
        (
            "#052FWhat? Uh, excuse me, Princess.\x02\x03",

            "Isn't this a little dangerous for the\x01",
            "possible heir to Liberl?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x105,
        (
            "#047FThe children at the orphanage have seen this...\x01",
            "whatever it is. I cannot simply let it be.\x02\x03",

            "#040FI've also been inside the old schoolhouse on a\x01",
            "few occasions... I think I may be able to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#053FTch... Fine, okay.\x02\x03",

            "#051F'Course when I think about it, you're probably\x01",
            "skilled enough to help us out anyway, what with\x01",
            "how you went up against Richard and all.\x02\x03",

            "Just be careful and don't overdo it,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        "#542FI'll be careful, I promise.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(    #26
        0x101,
        (
            "#1006FOkay, then!\x02\x03",

            "Let's head into the schoolhouse\x01",
            "and catch us a ghost!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x127,
        "#151FYeah!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-2290, 0, -3350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -2290, 0, -3350, 270)
    SetChrPos(0xF7, -2290, 0, -3350, 270)
    SetChrPos(0x105, -2290, 0, -3350, 270)
    SetChrPos(0x104, -2290, 0, -3350, 270)
    SetChrPos(0x127, -2290, 0, -3350, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -1810, 300, -1250, 269)
    SetChrPos(0x9, -3520, 300, 200, 158)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    OP_0D()
    FadeToBright(1000, 0)
    OP_A2(0x1222)
    OP_28(0x83, 0x1, 0x80)
    OP_28(0x84, 0x4, 0x2)
    OP_28(0x84, 0x4, 0x8)
    EventEnd(0x0)
    Return()

    # Function_8_A4F end

    def Function_9_1421(): pass

    label("Function_9_1421")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrPos(0x101, 240, 0, -2890, 225)
    SetChrPos(0xF7, 560, 0, -3920, 275)
    SetChrPos(0x105, -600, 0, -2190, 185)
    SetChrPos(0x104, -260, 0, -5270, 0)
    SetChrPos(0x127, -1510, 0, -5190, 45)
    SetChrPos(0x8, -1990, 0, -4400, 45)
    SetChrPos(0x9, -8610, 0, -3090, 90)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_6D(1300, 0, 4690, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)

    def lambda_150E():
        OP_6D(-120, 0, -3010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_150E)

    def lambda_1526():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1526)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_155C():

        label("loc_155C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_155C")

    QueueWorkItem2(0x101, 1, lambda_155C)

    def lambda_156D():

        label("loc_156D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_156D")

    QueueWorkItem2(0xF7, 1, lambda_156D)

    def lambda_157E():

        label("loc_157E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_157E")

    QueueWorkItem2(0x105, 1, lambda_157E)

    def lambda_158F():

        label("loc_158F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_158F")

    QueueWorkItem2(0x104, 1, lambda_158F)

    def lambda_15A0():

        label("loc_15A0")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_15A0")

    QueueWorkItem2(0x127, 1, lambda_15A0)

    def lambda_15B1():

        label("loc_15B1")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_15B1")

    QueueWorkItem2(0x8, 1, lambda_15B1)

    def lambda_15C2():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_15C2)

    def lambda_15D4():
        OP_8E(0x9, 0xFFFFF63C, 0x0, 0xFFFFF36C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_15D4)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #28
        0x9,
        (
            "#730F#3PAll right, I got the key to the back\x01",
            "gate from the teachers.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x9, 0x101, 0x3E8, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x00Received #1011i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x3F3, 1)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x104, 0x1)
    OP_44(0x127, 0x1)
    OP_44(0x8, 0x1)
    OP_8F(0x9, 0xFFFFF768, 0x0, 0xFFFFF36C, 0x7D0, 0x0)

    ChrTalk(    #30
        0x101,
        (
            "#1006FThanks, Hans!\x02\x03",

            "Let's get into the schoolhouse,\x01",
            "punch this ghost in the face,\x01",
            "and drag him back to the guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x104,
        (
            "#031F#4PHeh heh. We're finally entering Estelle's\x01",
            "element, it seems.\x02\x03",

            "#030FWell, then.\x01",
            "Let us begin our test of courage.\x02\x03",

            "Monsters may have taken root in the ruin,\x01",
            "so only those skilled at the art of combat\x01",
            "should enter.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #32
        0x103,
        (
            "#020FA good idea.\x02\x03",

            "Dorothy can come, but I'm afraid our\x01",
            "student friends need to remain here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#648F#5PYeah, I know.\x01",
            "We'll leave everything to you big,\x01",
            "tough fighting-types.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#730F#3PWe'll be waiting here in\x01",
            "case something happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        (
            "#043FUm... Scherazard?\x02\x03",

            "May I...accompany you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1951():
        TurnDirection(0x101, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1951)

    ChrTalk(    #36
        0x103,
        (
            "#023FHm? Ah, Princess...\x02\x03",

            "#522FI...don't think it would be very wise\x01",
            "for you to do something this dangerous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#047FThe children at the orphanage have seen this...\x01",
            "whatever it is. I cannot simply let it be.\x02\x03",

            "#040FI've also been inside the old schoolhouse on a\x01",
            "few occasions... I think I may be able to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        (
            "#026FHmmmmm... I see.\x02\x03",

            "#020FWell, you certainly proved you're\x01",
            "quite the fighter during the coup...\x02\x03",

            "All right, then. Just be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        "#542FI will, I promise.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(400)

    ChrTalk(    #40
        0x101,
        (
            "#1006FOkay then!\x02\x03",

            "Let's head into the schoolhouse\x01",
            "and catch us a ghost!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x127,
        "#151FYeah!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-2290, 0, -3350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -2290, 0, -3350, 270)
    SetChrPos(0xF7, -2290, 0, -3350, 270)
    SetChrPos(0x105, -2290, 0, -3350, 270)
    SetChrPos(0x104, -2290, 0, -3350, 270)
    SetChrPos(0x127, -2290, 0, -3350, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, -1810, 300, -1250, 269)
    SetChrPos(0x9, -3520, 300, 200, 158)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    OP_0D()
    FadeToBright(1000, 0)
    OP_A2(0x1222)
    OP_28(0x83, 0x1, 0x80)
    OP_28(0x84, 0x4, 0x2)
    OP_28(0x84, 0x4, 0x8)
    EventEnd(0x0)
    Return()

    # Function_9_1421 end

    def Function_10_1CAF(): pass

    label("Function_10_1CAF")

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
        (0, "loc_1D28"),
        (1, "loc_1D2E"),
        (SWITCH_DEFAULT, "loc_1D34"),
    )


    label("loc_1D28")

    OP_A2(0x1200)
    Jump("loc_1D34")

    label("loc_1D2E")

    OP_A2(0x1201)
    Jump("loc_1D34")

    label("loc_1D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1D42")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1D46")

    label("loc_1D42")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1D46")

    Return()

    # Function_10_1CAF end

    SaveToFile()

Try(main)
