from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3133   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3133.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3133   ._SN',
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
        'Professor Russell',                    # 9
        'Tita',                                 # 10
        'Cassius',                              # 11
        'Gospel',                               # 12
        'Sword',                                # 13
        "Tita's Report",                        # 14
        'Lane',                                 # 15
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH00065 ._CH',             # 02
        'ED6_DT27/CH03003 ._CH',             # 03
        'ED6_DT07/CH00053 ._CH',             # 04
        'ED6_DT07/CH00023 ._CH',             # 05
        'ED6_DT07/CH00043 ._CH',             # 06
        'ED6_DT07/CH00033 ._CH',             # 07
        'ED6_DT07/CH00063 ._CH',             # 08
        'ED6_DT07/CH02023 ._CH',             # 09
        'ED6_DT27/CH03670 ._CH',             # 0A
        'ED6_DT06/CH20021 ._CH',             # 0B
        'ED6_DT06/CH20140 ._CH',             # 0C
        'ED6_DT06/CH20141 ._CH',             # 0D
        'ED6_DT07/CH00061 ._CH',             # 0E
        'ED6_DT07/CH01450 ._CH',             # 0F
        'ED6_DT26/CH20278 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH00065P._CP',             # 02
        'ED6_DT27/CH03003P._CP',             # 03
        'ED6_DT07/CH00053P._CP',             # 04
        'ED6_DT07/CH00023P._CP',             # 05
        'ED6_DT07/CH00043P._CP',             # 06
        'ED6_DT07/CH00033P._CP',             # 07
        'ED6_DT07/CH00063P._CP',             # 08
        'ED6_DT07/CH02023P._CP',             # 09
        'ED6_DT27/CH03670P._CP',             # 0A
        'ED6_DT06/CH20021P._CP',             # 0B
        'ED6_DT06/CH20140P._CP',             # 0C
        'ED6_DT06/CH20141P._CP',             # 0D
        'ED6_DT07/CH00061P._CP',             # 0E
        'ED6_DT07/CH01450P._CP',             # 0F
        'ED6_DT26/CH20278P._CP',             # 10
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 917515,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 131088,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 32950,
        Z                   = -1000,
        Y                   = 10430,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_282",          # 01, 1
        "Function_2_283",          # 02, 2
        "Function_3_86D",          # 03, 3
        "Function_4_C42",          # 04, 4
        "Function_5_1A71",         # 05, 5
        "Function_6_3F60",         # 06, 6
        "Function_7_3FCA",         # 07, 7
        "Function_8_4057",         # 08, 8
        "Function_9_563D",         # 09, 9
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_236")
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_236")
    SetChrPos(0xE, 34650, -1000, 2160, 90)

    label("loc_236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_255")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_281")

    label("loc_255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D")
    Event(0, 4)

    label("loc_26D")

    Jump("loc_281")

    label("loc_270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_281")

    Return()

    # Function_0_212 end

    def Function_1_282(): pass

    label("Function_1_282")

    Return()

    # Function_1_282 end

    def Function_2_283(): pass

    label("Function_2_283")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_437")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        "Whoa! Wh-Who is it?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x107,
        "#064FHuh? Lane...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)

    ChrTalk(    #2
        0xFE,
        "Oh, it's you, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Sorry. Didn't mean to jump\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I've been checking orbments\x01",
            "all over town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Looks like this machine's down,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        "#063FYeah... Looks like it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Anyway, I'll be fiddling around\x01",
            "here for a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "I'll finish up as quickly as I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        "#560FOkay, understood.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x20BF)
    Jump("loc_869")

    label("loc_437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_6CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4EA")

    ChrTalk(    #10
        0xFE,
        (
            "It's so frustrating! None of\x01",
            "the machines here are working,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "There's no way we can resume\x01",
            "our research with all this stuff\x01",
            "that's been going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CA")

    label("loc_4EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_622")

    ChrTalk(    #12
        0xFE,
        (
            "Russell's currently out helping\x01",
            "the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Some researchers hand-picked\x01",
            "by Russell are with him, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I guess this means that the fate\x01",
            "of the kingdom's been entrusted\x01",
            "to them, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "As a fellow member of the central\x01",
            "factory, I feel like I can live proudly\x01",
            "with my head held high.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6CA")

    label("loc_622")


    ChrTalk(    #16
        0xFE,
        (
            "The fate of the kingdom's practically\x01",
            "been entrusted to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "As a fellow member of the central\x01",
            "factory, I feel like I can live proudly\x01",
            "with my head held high.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CA")

    Jump("loc_869")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CF")

    ChrTalk(    #18
        0xFE,
        (
            "I'm going around town checking\x01",
            "over the orbments on Chief Murdock's\x01",
            "orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "It's so frustrating! None of the\x01",
            "machines here are working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "*sigh* How the heck are we\x01",
            "supposed to restart research in\x01",
            "a situation like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_869")

    label("loc_7CF")


    ChrTalk(    #21
        0xFE,
        (
            "It's so frustrating! None of the\x01",
            "machines here are working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "There's no way we can resume\x01",
            "our research with all this stuff\x01",
            "that's been going on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_869")

    TalkEnd(0xFE)
    Return()

    # Function_2_283 end

    def Function_3_86D(): pass

    label("Function_3_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_887")
    Call(0, 9)
    FadeToBright(0, 0)

    label("loc_887")

    EventBegin(0x0)
    SetChrPos(0x101, -1220, 0, -2240, 0)
    SetChrPos(0xF7, -2340, 0, -2240, 0)
    SetChrPos(0x105, -1220, 0, -3260, 0)
    SetChrPos(0x104, -2340, 0, -3260, 0)
    OP_6D(-960, 0, 4280, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_C8(0x200, 0x46, "C_PLAC08._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_92E():
        OP_67(0, 6150, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92E)
    OP_6D(-490, 0, -1760, 2500)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #23
        0x101,
        (
            "#1015F#4PHuh... Are Professor Russell\x01",
            "and Tita even in?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9E1")

    ChrTalk(    #24
        0x106,
        (
            "#051F#6PKnowin' Russell, they might be\x01",
            "at the central factory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A43")

    label("loc_9E1")


    ChrTalk(    #25
        0x103,
        (
            "#027F#6PFrom what I know of Russell, it wouldn't\x01",
            "surprise me if he's at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A43")

    SetChrPos(0x8, 3920, 0, -830, 270)

    NpcTalk(    #26
        0x8,
        "Girl's Voice",
        (
            "#1S#6PGrandpaaaaa!\x01",
            "The second floor's cleaned up!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A9E():
        OP_6D(1720, 0, -1220, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A9E)
    Sleep(100)

    def lambda_ABB():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABB)
    Sleep(100)

    def lambda_ACE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_ACE)
    Sleep(100)

    def lambda_AE1():
        OP_8C(0xFE, 88, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AE1)
    Sleep(100)

    def lambda_AF4():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF4)
    WaitChrThread(0x101, 0x2)

    NpcTalk(    #27
        0x8,
        "Old Man's Voice",
        "#1S#1PThank you, Tita!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x8,
        "Old Man's Voice",
        "#1S#1PCould you organize the parts next?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #29
        0x8,
        "Girl's Voice",
        "#1S#5POkaaaay!\x02",
    )

    CloseMessageWindow()

    def lambda_B92():
        OP_6D(-490, 0, -1760, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B92)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #30
        0x101,
        (
            "#1017F#6PHaha! I don't think we have to\x01",
            "worry about finding them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C20")

    ChrTalk(    #31
        0x106,
        "#051F#6PSounds like. C'mon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3C")

    label("loc_C20")


    ChrTalk(    #32
        0x103,
        "#021F#6PCome on, then.\x02",
    )

    CloseMessageWindow()

    label("loc_C3C")

    OP_A2(0x1409)
    EventEnd(0x0)
    Return()

    # Function_3_86D end

    def Function_4_C42(): pass

    label("Function_4_C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C5C")
    Call(0, 9)
    FadeToBright(0, 0)

    label("loc_C5C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(35500, -1000, 10320, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(503, 0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 2)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 34400, -1000, 8900, 0)
    SetChrPos(0x9, 34650, -1000, 2190, 90)
    FadeToBright(1000, 0)

    def lambda_CEA():
        OP_6D(36140, -1000, 7440, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEA)

    def lambda_D02():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D02)
    Sleep(1000)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    Sleep(500)
    OP_8E(0x9, 0x8700, 0xFFFFFC18, 0x10FE, 0x7D0, 0x0)
    OP_8C(0x9, 90, 400)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 2)
    Sleep(1000)
    SetChrChipByIndex(0x9, 1)
    OP_0D()
    Sleep(500)
    OP_8E(0x9, 0x875A, 0xFFFFFC18, 0x88E, 0x7D0, 0x0)
    OP_8C(0x9, 90, 400)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 2)
    Sleep(500)

    ChrTalk(    #33
        0x9,
        (
            "#5PMmmmph...\x01",
            "Errrrrrmph...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_106F")
    SetChrPos(0x106, 25790, 0, -130, 90)

    ChrTalk(    #34
        0x106,
        "#2PYo! You doin' all right, shortstuff?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_E17():
        OP_6D(34640, -1000, 5940, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E17)

    def lambda_E2F():
        OP_8E(0x106, 0x7EF4, 0xFFFFFC18, 0x6E0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_E2F)
    SetChrChipByIndex(0x9, 1)
    TurnDirection(0x9, 0x106, 400)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x106, 400)
    Sleep(800)

    ChrTalk(    #35
        0x9,
        "#560F#2PHuh...? AGATE!!\x02",
    )

    CloseMessageWindow()

    def lambda_E9B():
        OP_8E(0x8, 0x7EF4, 0xFFFFFC18, 0xD20, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E9B)

    def lambda_EB6():
        OP_8F(0x9, 0x82DC, 0xFFFFFC18, 0x6E0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EB6)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #36
        0x9,
        (
            "#061F#2PYay! You're back!\x01",
            "Where've you been?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #37
        0x8,
        (
            "#100F#5PHmmmmm? I do believe my work is\x01",
            "being disrupted by a big, loud oaf\x01",
            "with a sword the size of an airship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #38
        0x106,
        (
            "#551FI can always just stop visitin',\x01",
            "you know.\x02\x03",

            "#051FStill good to see you two again.\x01",
            "Place is a bit of a mess, though.\x02\x03",

            "Lemme guess, that little shake-up\x01",
            "knocked everything over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#067F#2PHeehee! Yeah, sorry for the mess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12A0")

    label("loc_106F")

    SetChrPos(0x103, 25790, 0, -130, 90)

    ChrTalk(    #40
        0x103,
        "#2PWorking hard, Tita?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10CB():
        OP_6D(34640, -1000, 5940, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10CB)

    def lambda_10E3():
        OP_8E(0x103, 0x7EF4, 0xFFFFFC18, 0x6E0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10E3)
    SetChrChipByIndex(0x9, 1)
    TurnDirection(0x9, 0x103, 400)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x103, 400)
    Sleep(800)

    ChrTalk(    #41
        0x9,
        "#064F#2PHuh? Oh, Schera!\x02",
    )

    CloseMessageWindow()

    def lambda_1150():
        OP_8E(0x8, 0x7EF4, 0xFFFFFC18, 0xD20, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1150)

    def lambda_116B():
        OP_8F(0x9, 0x82DC, 0xFFFFFC18, 0x6E0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_116B)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #42
        0x9,
        "#061F#2PHi! What brings you here?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #43
        0x8,
        (
            "#103F#5PHmm? Wait, I remember you.\x01",
            "Cassius Bright's apprentice, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #44
        0x103,
        (
            "#021FMm-hmm! It's been a while, you two.\x02\x03",

            "#027FIt's really a bit of a mess in here...\x01",
            "Is it because of the earthquake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        "#067F#2POh, yeah. Sorry...\x02",
    )

    CloseMessageWindow()

    label("loc_12A0")

    SetChrPos(0x101, 25230, 0, -750, 90)
    SetChrPos(0x105, 24390, 0, 660, 90)
    SetChrPos(0x104, 23490, 0, -870, 90)

    ChrTalk(    #46
        0x101,
        "#2PHiya, everyone!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x9,
        "#064F#2PWha...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)

    def lambda_133F():

        label("loc_133F")

        TurnDirection(0x8, 0x101, 400)
        OP_48()
        Jump("loc_133F")

    QueueWorkItem2(0x8, 2, lambda_133F)

    def lambda_1350():
        OP_6D(33140, -1000, 3940, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1350)

    def lambda_1368():
        OP_8E(0xFE, 0x73AA, 0xFFFFFC18, 0x140, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1368)
    Sleep(500)

    def lambda_1388():
        OP_8E(0xFE, 0x756C, 0xFFFFFC18, 0x3D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1388)
    Sleep(200)

    def lambda_13A8():
        OP_8E(0xFE, 0x7634, 0xFFFFFC18, 0xFFFFFFD8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13A8)
    WaitChrThread(0x101, 0x1)

    def lambda_13C8():
        OP_8E(0xFE, 0x7C56, 0xFFFFFC18, 0x686, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13C8)
    OP_8C(0xF7, 180, 400)

    def lambda_13EA():
        OP_8E(0xFE, 0x7E2B, 0xFFFFFC18, 0x190, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_13EA)
    WaitChrThread(0xF7, 0x1)

    def lambda_140A():

        label("loc_140A")

        TurnDirection(0xF7, 0x101, 400)
        OP_48()
        Jump("loc_140A")

    QueueWorkItem2(0xF7, 2, lambda_140A)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #48
        0x101,
        (
            "#1016F#5PEh-heheh...\x01",
            "Sorry I haven't been in touch.\x02",
        )
    )

    WaitChrThread(0x104, 0x1)
    TurnDirection(0x104, 0x9, 400)
    OP_44(0xF7, 0x2)
    OP_44(0x8, 0x2)
    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "#103F#6PEstelle! Hello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        "#065F#2PEs... Est...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #51
        0x9,
        "#068F#2P#3SEsteeeeeeelle...!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)

    def lambda_14E6():
        OP_6D(32640, -1000, 3440, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14E6)

    def lambda_14FE():
        OP_6B(1770, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14FE)

    def lambda_150E():

        label("loc_150E")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_150E")

    QueueWorkItem2(0x8, 1, lambda_150E)
    SetChrChipByIndex(0x9, 14)
    OP_92(0x9, 0x101, 0x190, 0x1388, 0x0)

    def lambda_1532():
        OP_94(0x1, 0x9, 0x0, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1532)
    OP_48()
    OP_8C(0x9, 270, 0)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 13)
    SetChrSubChip(0x9, 0)
    OP_8C(0x101, 90, 0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x7D0, 0x0)
    WaitChrThread(0x9, 0x3)

    ChrTalk(    #52
        0x101,
        "#1004F#5PWaa-aaah! Tita?! What's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#069F#2PIt's... Uwaaaaah...\x02\x03",

            "It's really you...\x01",
            "I thought you were gone forever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1016F#5PWait, hang on, 'gone forever'?\x01",
            "I'd never do that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        (
            "#069F#2PB-B-But...\x02\x03",

            "I heard Joshua ran away...\x02\x03",

            "And then you left the country...\x02\x03",

            "#562FI thought I was never gonna\x01",
            "see you agaaaain...\x01",
            "Uwaaah-haaah...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1025F#5POh, Tita...\x02\x03",

            "I'm sorry... I shouldn't have left\x01",
            "without saying anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0x1)

    ChrTalk(    #57
        0x8,
        (
            "#100F#6PAs I recall, Cassius sent you off to that\x01",
            "bracer school in Leman, didn't he?\x02\x03",

            "When did you get home?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 32350, -1000, 1670, 270)
    OP_0D()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1017F#5PI got back just a little while ago.\x02\x03",

            "I was working in Ruan after getting\x01",
            "back... I only just arrived in Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "#101F#6PI see. Well, welcome back!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #60
        0x8,
        "#103F#6PAh, wait, the two with you...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #61
        0x105,
        (
            "#048FHello, Professor, Tita. I'm sorry\x01",
            "I've been out of touch as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x104,
        "#031F#2PHeh. Pardon our intrusion, good sir.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 400)

    ChrTalk(    #63
        0x9,
        (
            "#560F#2PKloe, Olivier... Everyone's here...\x01",
            "This is wonderful!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #64
        0x101,
        (
            "#1006F#5PThey're helping us with our investigation.\x02\x03",

            "A lot of stuff happened in Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#104F#6PHmm...\x02\x03",

            "#100FWell, let's get comfortable and hear the story,\x01",
            "eh? Come, I'll show you to the living room.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Call(0, 5)
    Return()

    # Function_4_C42 end

    def Function_5_1A71(): pass

    label("Function_5_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A8B")
    Call(0, 9)
    FadeToBright(0, 0)

    label("loc_1A8B")

    OP_6D(-860, 0, 1560, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(40000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    SetChrFlags(0x3, 0x4)
    SetChrPos(0x101, -2270, 200, 480, 90)
    SetChrPos(0xF7, -2270, 200, 1700, 90)
    SetChrPos(0x8, 270, 200, 1700, 270)
    SetChrPos(0x9, 250, 200, 480, 270)
    SetChrPos(0x105, -1100, 200, -800, 0)
    SetChrPos(0x104, -1100, 200, 2650, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B51")
    SetChrChipByIndex(0xF7, 4)
    Jump("loc_1B56")

    label("loc_1B51")

    SetChrChipByIndex(0xF7, 5)

    label("loc_1B56")

    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x105, 6)
    SetChrChipByIndex(0x104, 7)
    SetChrChipByIndex(0x9, 8)
    SetChrChipByIndex(0x8, 9)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #66
        0x8,
        (
            "#104FSo the true force behind the\x01",
            "coup is on the move again...\x02\x03",

            "#102FAnd they had another Gospel\x01",
            "with them? Troubling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#065FA holographic projector that can show\x01",
            "an image all the way across a region?\x02\x03",

            "How... How is that even possible?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #68
        0x8,
        (
            "#100F#6PWell, the CONCEPT of a projected\x01",
            "holograph is nothing new.\x02\x03",

            "I've been kicking around ideas\x01",
            "for pulling it off myself, even.\x02\x03",

            "#104FBut a device that can project a lifelike,\x01",
            "three-dimensional image great distances\x01",
            "away from its origin point?\x02\x03",

            "#102FI...can scarcely even imagine the physics\x01",
            "behind such a thing. Hmmmmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1007F#1PThat weirdo we fought said something about\x01",
            "an 'experiment' with a 'new Gospel.'\x02\x03",

            "#1015FIt did seem bigger than the one from before,\x01",
            "but it didn't stop our orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1EFD")

    ChrTalk(    #70
        0x106,
        (
            "#050FOh, yeah, speakin' of, how's the\x01",
            "Gospel we captured in the coup?\x02\x03",

            "You figure anything out about it yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F72")

    label("loc_1EFD")


    ChrTalk(    #71
        0x103,
        (
            "#020FSay, on that note. How is the Gospel\x01",
            "we captured a while ago?\x02\x03",

            "Have you made any progress in analyzing it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F72")

    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #72
        0x8,
        (
            "#104FMmm. About that.\x02\x03",

            "The more I investigate that little\x01",
            "enigma, the stranger it gets.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x101,
        "#1004F#1PStranger?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#102FYes. Let me start at the end, actually.\x02\x03",

            "I am convinced the 'Orbal Shutdown Phenomenon'\x01",
            "is not a function of the device itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1020F#1PWh... What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x105,
        (
            "#043FB-But...\x02\x03",

            "That Black Orbment has stopped other\x01",
            "orbments dead in their tracks.\x01",
            "We've SEEN it, Professor!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #77
        0x8,
        (
            "#104F#6PYou've seen orbments stop in its presence.\x01",
            "That isn't quite the same thing, milady.\x02\x03",

            "#102FNo matter how I look at it, though, the quartz\x01",
            "in the device simply cannot actually do that.\x02\x03",

            "It can certainly warp orbal fields--oh, how it\x01",
            "can do that--but suppress them? No.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#042FWarp orbal fields...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#560FOh, 'orbal field' refers to the electromagnetic\x01",
            "field generated by an individual orbal device.\x02\x03",

            "With normal orbments, you can describe an\x01",
            "orbal field by drawing its 'field lines,' and those\x01",
            "follow very specific rules...\x02\x03",

            "When Grandpa tested the Gospel, though,\x01",
            "its field didn't obey those rules at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x104,
        (
            "#034F#6PThis is going a little above my\x01",
            "pretty little head, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x101,
        "#1007F#1PYeeeah... Afraid not much is registering.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #82
        0x8,
        (
            "#100FIn layman's terms, it's a warped orbal\x01",
            "field that doesn't obey the laws of such\x01",
            "things as we understand them.\x02\x03",

            "#104FRegardless of that, though...ultimately,\x01",
            "an orbal field amounts to nothing more\x01",
            "than orbal energy in an area.\x02\x03",

            "Unless you were to apply very specific direction\x01",
            "and purpose to them, you shouldn't get the 'Orbal\x01",
            "Shutdown Phenomenon' effect regardless...\x02\x03",

            "#100FTo be honest, I'd been utterly stuck on this,\x01",
            "but with your report of this holographic\x01",
            "business...I may have an idea.\x02\x03",

            "#101FThank you for letting me know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1016F#1PHaha... Well, I'm not sure how that\x01",
            "was useful, but...you're welcome?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2752")

    ChrTalk(    #84
        0x106,
        (
            "#051FThe Royal Army oughtta have possession\x01",
            "of the hologram thing the enemy was using.\x02\x03",

            "If you want to have a look,\x01",
            "get in touch with 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27E1")

    label("loc_2752")


    ChrTalk(    #85
        0x103,
        (
            "#020FThe Royal Army has custody of the\x01",
            "device the Ouroboros agent used.\x02\x03",

            "I'm sure they'll let you have a \x01",
            "look at it if you contact them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E1")


    ChrTalk(    #86
        0x8,
        (
            "#104FHmm. I may just do that.\x02\x03",

            "#100FSpeaking of which, what are\x01",
            "you going to be up to now?\x02\x03",

            "Will you be working in Zeiss for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#1006F#1POh, yeah, about that...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #88
        (
            "\x07\x05Estelle explained the situation concerning the\x01",
            "guild's request to investigate the earthquakes.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #89
        0x8,
        (
            "#103FAh, so Kilika thinks the earthquakes... Hmm.\x02\x03",

            "#102FWell, it is true that earthquakes\x01",
            "are rare here in Liberl.\x02\x03",

            "And she is correct about the\x01",
            "earthquake at the Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "#064FThree days ago...\x02\x03",

            "#063FI think Ms. Kilika is right!\x01",
            "I don't remember Zeiss getting\x01",
            "any tremors at all!\x02\x03",

            "That IS kinda weird...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1006F#1PWell, it's a natural phenomenon, so\x01",
            "I kinda doubt the society is involved.\x02\x03",

            "It's still pretty weird, though, and we'd\x01",
            "like to figure out what's going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#104FIndeed. Earthquakes, hmm?\x02\x03",

            "I wonder if it would be useful...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#1004F#1PHuh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2BAE")

    ChrTalk(    #94
        0x106,
        (
            "#552FGramps, if you haul out another\x01",
            "weird invention, I swear...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C0C")

    label("loc_2BAE")


    ChrTalk(    #95
        0x103,
        (
            "#526FLet me guess, Professor. You have an old\x01",
            "invention in the toolbox which might help?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C0C")


    ChrTalk(    #96
        0x8,
        (
            "#102FHmm... I do have something in mind.\x02\x03",

            "But then how would we...? Wait, transmit\x01",
            "the data back here using...and then hook\x01",
            "it in to the Capel! Of course!\x02\x03",

            "#101FHah! Yes! It'd work perfectly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1016F#1PUh, Professor Russell?\x01",
            "Could you keep the rest of us in the loop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#100FAh, don't worry. I need to check a few\x01",
            "things regardless before we start.\x02\x03",

            "I'd recommend heading to the Wolf Fort,\x01",
            "and learn from them what happened.\x02\x03",

            "I'll see about preparing you\x01",
            "a little something useful for\x01",
            "when you get back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#1025F#1PWell, I definitely won't say no, but...\x02\x03",

            "What 'little something' are\x01",
            "we talking about, here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#101FHah! That'd spoil the surprise!\x01",
            "Just you wait.\x02\x03",

            "Now, if you'll excuse me, I need to get\x01",
            "to the central factory! Just have to\x01",
            "browbeat Murdock into going along...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #101
        0x8,
        (
            "#100F#6PTita, would you mind helping\x01",
            "your ol' Grandpa?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_326C")
    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #102
        0x9,
        "#560FOh, sure...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    Sleep(300)

    ChrTalk(    #103
        0x9,
        (
            "#561FEstelle, Agate, I'm sorry.\x02\x03",

            "We finally met again after\x01",
            "so long, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1016F#1PHaha! It's okay, don't worry.\x02\x03",

            "#1017FI'm just happy I got a chance\x01",
            "to see you again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        "#066FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x106,
        (
            "#051FHey, no tears now, kiddo. Besides,\x01",
            "we'll be here in Zeiss for a while.\x02\x03",

            "We'll have plenty of chances to see\x01",
            "each other later. Just you wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        "#067FYeah!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 360, 0, 2530, 225)
    SetChrFlags(0x8, 0x4)
    OP_0D()
    SetChrSubChip(0x9, 0)
    Sleep(100)
    SetChrChipByIndex(0x9, 1)

    def lambda_3149():
        OP_96(0xFE, 0x17C, 0x0, 0xFFFFFF38, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3149)
    OP_8C(0x9, 180, 1000)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x105, 2)
    Sleep(500)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #108
        0x9,
        (
            "#560F#4PUm, um... I'm sorry we couldn't\x01",
            "give you much of a welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x105,
        "#048F#5PHaha! Don't worry, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x104,
        (
            "#031F#6PFear not! We shall stop by again.\x02\x03",

            "Perhaps, on that day, I too\x01",
            "can be greeted with such\x01",
            "moist, welcoming eyes!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3548")

    label("loc_326C")

    SetChrSubChip(0x9, 2)
    Sleep(300)

    ChrTalk(    #111
        0x9,
        "#560FUm... Maybe...?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    Sleep(300)

    ChrTalk(    #112
        0x9,
        (
            "#561FEstelle, I'm sorry.\x02\x03",

            "We finally meet again after\x01",
            "so long, and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1016F#1PHaha! It's okay, don't worry.\x02\x03",

            "#1017FI'm just happy I got to see you again!\x02\x03",

            "We'll be in Zeiss for a good long\x01",
            "time, so I'm sure we'll have a chance\x01",
            "to spend some time together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "#560FEstelle...\x02\x03",

            "#067FYeah, I can't wait!\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    SetChrPos(0x8, 360, 0, 2530, 225)
    SetChrFlags(0x8, 0x4)
    OP_0D()
    SetChrSubChip(0x9, 0)
    Sleep(100)
    SetChrChipByIndex(0x9, 1)

    def lambda_340F():
        OP_96(0xFE, 0x17C, 0x0, 0xFFFFFF38, 0x258, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_340F)
    OP_8C(0x9, 180, 1000)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x105, 2)
    Sleep(500)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #115
        0x9,
        (
            "#560F#4PUm, um... I'm sorry we couldn't\x01",
            "give you much of a welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x105,
        "#048F#5PHaha! Don't worry, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#021FWe'll stop by again if the chance\x01",
            "comes up, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x104,
        (
            "#031F#6PPerhaps, on that day, I too\x01",
            "can be greeted with such\x01",
            "moist, welcoming eyes!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3548")

    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #119
        0x101,
        (
            "#1019F#2PAnd on that day you'll\x01",
            "have two black eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        "#067F#4PUm, haha...ha? Anyway, see you later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        "#101FWe'll contact the guild once we're ready!\x02",
    )

    CloseMessageWindow()

    def lambda_35F9():
        OP_6D(-980, 0, -50, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35F9)
    OP_43(0x9, 0x1, 0x0, 0x6)
    OP_43(0x8, 0x1, 0x0, 0x7)
    SetChrSubChip(0x101, 0)
    Sleep(50)
    SetChrSubChip(0xF7, 2)
    Sleep(50)
    SetChrSubChip(0x101, 2)
    WaitChrThread(0x8, 0x1)
    OP_6D(-860, 0, 1560, 1000)
    SetChrSubChip(0x105, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #122
        0x101,
        "#1016F#1PWell, those two haven't changed at all.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A65")

    ChrTalk(    #123
        0x106,
        (
            "#551F#3PStill inside all the time fiddling\x01",
            "with machines at her age...\x02\x03",

            "Kinda makes me worry, you know?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #124
        0x101,
        (
            "#1015F#2PMmm. She doesn't do a\x01",
            "lot of 'girl stuff,' I guess.\x02\x03",

            "#1006FBut hey, I didn't at that age, either,\x01",
            "and I turned out okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x106,
        (
            "#552F#3PHer parents oughtta be the ones\x01",
            "worried about it, dang it.\x02\x03",

            "I guess they can't, being out of the country.\x02\x03",

            "Think I might have to talk to Gramps\x01",
            "about it the next time we see him.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(    #126
        0x104,
        (
            "#031F#7PWhy, Agate. That's quite a...\x01",
            "brotherly thing to say.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x106, 0)
    Sleep(75)
    SetChrSubChip(0x106, 1)
    Sleep(300)

    ChrTalk(    #127
        0x106,
        "#055F#6PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x104,
        (
            "#035F#7POr perhaps a fatherly thing to say.\x02\x03",

            "#037FAh, what a fine daughter! You would\x01",
            "make any man jealous, Mr. Crosner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x106,
        "#555F#6P...You lookin' to lose some teeth, blondie?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x104,
        (
            "#031F#7PNot at all.\x02\x03",

            "Indeed, I do envy your bond\x01",
            "with that girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x105,
        (
            "#041FHaha! To be honest, I understand\x01",
            "what Olivier means.\x02\x03",

            "#048FTita's the kind of girl you wish was\x01",
            "your little sister. I envy you, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CCC")

    label("loc_3A65")


    ChrTalk(    #132
        0x103,
        (
            "#021F#3PYes, Tita hasn't lost any\x01",
            "of her adorableness.\x02\x03",

            "I was having to fight the urge to\x01",
            "just pick her up and hug her.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 2)
    Sleep(300)

    ChrTalk(    #133
        0x104,
        (
            "#035F#6PIndeed.\x02\x03",

            "A lost little girl, being swept up into\x01",
            "the arms of a loving, brotherly\x01",
            "minstrel after ages of separation...\x02\x03",

            "#037FSuch a dramatic scene!\x01",
            "The thought makes my heart swell.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #134
        0x101,
        (
            "#1019F#2PIf YOU tried to grab her out of the\x01",
            "blue like that, I'd have to arrest\x01",
            "you for abduction, you nitwit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x105,
        (
            "#041FHaha! To be honest, I understand\x01",
            "what Scherazard means.\x02\x03",

            "#048FTita's the kind of girl you\x01",
            "wish was your little sister.\x01",
            "I envy you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CCC")

    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 2)
    Sleep(300)

    ChrTalk(    #136
        0x101,
        (
            "#1016F#1PH-Hey, Kloe, cut it out...\x02\x03",

            "#1006FWell, don't worry! Everyone'll get\x01",
            "to know her soon enough!\x01",
            "Except for Olivier, maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x104,
        "#036F#6PEstelle! An arrow, my heart!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E0E")
    SetChrSubChip(0x106, 0)
    Sleep(75)
    SetChrSubChip(0x106, 2)
    Sleep(300)

    ChrTalk(    #138
        0x106,
        (
            "#551F#3POh, for... I can't keep up with this.\x02\x03",

            "#555FLet's get this show on the road, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E89")

    label("loc_3E0E")


    ChrTalk(    #139
        0x103,
        (
            "#020F#3PAll's fair in love and siblings, my dear\x01",
            "Lenheim. Now, then...\x02\x03",

            "Let's get started on our guild business,\x01",
            "hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E89")

    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #140
        0x101,
        (
            "#1006F#2PYou're right, we should.\x02\x03",

            "So let's make our way over to the\x01",
            "Wolf Fort while we work on those\x01",
            "other jobs!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x104, 65535)
    ClearChrFlags(0x0, 0x4)
    ClearChrFlags(0x1, 0x4)
    ClearChrFlags(0x2, 0x4)
    ClearChrFlags(0x3, 0x4)
    OP_A2(0x140A)
    OP_28(0x85, 0x1, 0x2)
    OP_28(0x85, 0x1, 0x4)
    NewScene("ED6_DT21/T3100   ._SN", 118, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1A71 end

    def Function_6_3F60(): pass

    label("Function_6_3F60")

    ClearChrFlags(0xFE, 0x20)
    OP_8E(0xFE, 0x32, 0x0, 0xFFFFFA2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7AE, 0x0, 0xFFFFF0BA, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_3FA4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FA4)
    OP_8E(0xFE, 0xFFFFF79A, 0xFFFFFE0C, 0xFFFFE73C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_3F60 end

    def Function_7_3FCA(): pass

    label("Function_7_3FCA")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x49C, 0x0, 0x988, 0x9C4, 0x0)
    OP_8E(0xFE, 0x532, 0x0, 0xFFFFFF42, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF7D6, 0x0, 0xFFFFF0C4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF827, 0xFFFFFE0C, 0xFFFFEE3A, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)

    def lambda_402C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_402C)
    OP_8E(0xFE, 0xFFFFF79A, 0xFFFFFE0C, 0xFFFFE73C, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_7_3FCA end

    def Function_8_4057(): pass

    label("Function_8_4057")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(30650, -1000, 330, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(33000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, 29950, -1000, 8750, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xB, 34450, -350, 10510, 0)
    SetChrPos(0xC, 28600, -850, 7700, 0)
    SetChrPos(0xD, 28750, -900, 8450, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    def lambda_4108():
        OP_6D(29210, 0, 8080, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4108)

    def lambda_4120():
        OP_67(0, 6000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4120)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #141
        0x8,
        (
            "#102F#6PI see, so now we have a Gospel influencing\x01",
            "people's minds...\x02\x03",

            "Using the fog's particulate matter as a\x01",
            "medium to exert mental control over a\x01",
            "large area...\x02\x03",

            "#104FWell, that settles one question, at least.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, 22550, 0, 0, 45)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #142
        0xA,
        "Man's Voice",
        "#2PExcuse me, Professor.\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4285():
        OP_6D(26250, 0, 4030, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4285)

    def lambda_429D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_429D)
    OP_6B(3000, 2500)

    ChrTalk(    #143
        0x8,
        (
            "#103F#6PCassius, you old dog, good timing!\x02\x03",

            "Escaped Leiston, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xA,
        (
            "#1120F#5PYes, I finally managed to finish a bit of work.\x02\x03",

            "I thought I would stop by and see how\x01",
            "you're holding up.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4377():

        label("loc_4377")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_4377")

    QueueWorkItem2(0x8, 1, lambda_4377)

    def lambda_4388():
        OP_6D(30720, -1000, 7630, 6500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4388)

    def lambda_43A0():
        OP_6B(2750, 6500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43A0)
    OP_8E(0xA, 0x779C, 0xFFFFFC18, 0x32A, 0x9C4, 0x0)
    OP_8E(0xA, 0x779C, 0xFFFFFC18, 0x155E, 0x9C4, 0x0)
    TurnDirection(0xA, 0x8, 400)
    Sleep(1000)
    OP_44(0x8, 0x1)

    def lambda_43E8():

        label("loc_43E8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_43E8")

    QueueWorkItem2(0xA, 1, lambda_43E8)

    ChrTalk(    #145
        0xA,
        (
            "#1120FWhat's this...?\x01",
            "A report from your granddaughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        (
            "#101F#6PYes, just arrived express from Rolent.\x02\x03",

            "#100FThanks to Tita's report,\x01",
            "I'm quite certain of my theory now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xA,
        "#1122FAbout the Gospel, I'm assuming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#104F#6PMmm, yes, though it's ultimately still a\x01",
            "hypothesis at this point.\x02\x03",

            "#102FI've gone over it again and again, both on\x01",
            "paper and with the Capel, though, so I'm\x01",
            "reasonably sure of this.\x02\x03",

            "Shall I go over it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        "#1125FAbsolutely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        "#101F#6PRight, then! Ahem!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    OP_8E(0x8, 0x80B6, 0xFFFFFC18, 0x2882, 0x7D0, 0x0)
    TurnDirection(0x8, 0xB, 400)
    Sleep(500)
    OP_22(0x82, 0x0, 0x64)
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    Sleep(500)
    OP_8C(0x8, 180, 400)
    OP_8C(0x8, 270, 400)
    OP_8E(0x8, 0x74FE, 0xFFFFFC18, 0x222E, 0x7D0, 0x0)
    SetChrPos(0xB, 29260, -400, 8750, 0)
    TurnDirection(0x8, 0xB, 400)
    Sleep(500)
    ClearChrFlags(0xB, 0x80)
    OP_22(0x82, 0x0, 0x64)
    OP_44(0xA, 0x1)
    Sleep(1000)

    ChrTalk(    #151
        0x8,
        (
            "#104F#6PSo. What we've been calling the\x01",
            "Gospel's 'Orbal Shutdown Phenomenon'...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(    #152
        0x8,
        (
            "#100F#6PTell me, what do you think it is,\x01",
            "based on what you've seen and heard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xA,
        (
            "#1122FIt's an effect that occurs to any orbal\x01",
            "device located near an active Gospel,\x01",
            "chaining from one device to another.\x02\x03",

            "And it renders these devices inert while\x01",
            "a Gospel is active. That's how it seems\x01",
            "to me, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "#100F#6PMmm. Half right, half wrong.\x02\x03",

            "#104FWhat you're describing is closer to the\x01",
            "Orbal Art 'Anti-Sept.'\x02\x03",

            "That shorts out the internal quartz-circuits\x01",
            "of an orbment to temporarily suspend its\x01",
            "functionality.\x02\x03",

            "#102FThe phenomenon generated by a Gospel,\x01",
            "however, is fundamentally different.\x02\x03",

            "It steals all the orbal energy formed in an\x01",
            "orbment, down to the very last joule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xA,
        (
            "#1122FSo it's more of an 'orbal absorption phenomenon,'\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#100FYes. To make a comparison to a combustion\x01",
            "engine, it's like siphoning out the petrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "#1128FHmm.\x02\x03",

            "#1122FBut...wait.\x02\x03",

            "Unless I badly misunderstand physics,\x01",
            "that means the Gospel should absorb\x01",
            "and store all that power, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "#101F#6PGood eye, lad!\x01",
            "You've noticed a very important fact.\x02\x03",

            "#100FSo, I've measured a Gospel after it 'absorbs'\x01",
            "energy, but the Gospel does not actually hold\x01",
            "any of it.\x02\x03",

            "Not even a single EP's worth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        (
            "#1122FIs it possible the energy is being\x01",
            "vented into the wider environment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#104F#6PNo. Not at all.\x02\x03",

            "The energy disappears. Completely. Utterly.\x01",
            "And...quite impossibly, thanks to thermodynamics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xA,
        "#1128F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "#100F#6PFurthermore, these 'new' Gospels Estelle's\x01",
            "group has been encountering...\x02\x03",

            "Every time they're encountered, they cause\x01",
            "unbelievable phenomena that even our best\x01",
            "orbal engineering can't explain.\x02\x03",

            "#104FIt's unclear how they're causing such\x01",
            "effects, but...\x02\x03",

            "I can say one thing with confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xA,
        "#1124FAnd that is?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "#102F#6PThey're too small.\x02\x03",

            "I can say with absolute certainty that ANY\x01",
            "device enabling such massive effects could\x01",
            "not fit into the palm of one's hand.\x02\x03",

            "Even if the society somehow possesses technology\x01",
            "CENTURIES ahead of our own, nothing that small\x01",
            "could contain that much potential energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "#1123FAh... I think I'm starting to see where this\x01",
            "is going.\x02\x03",

            "#1120FYou're saying the Gospels must be terminals,\x01",
            "then? Access points of some sort?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "#101FExactly!\x02\x03",

            "#100FThe only function the Gospel unit itself has\x01",
            "is an ability to manifest an abnormal warp\x01",
            "in a local orbal field.\x02\x03",

            "That warp then resonates with any local\x01",
            "orbal devices, expands, and draws energy\x01",
            "from the devices.\x02\x03",

            "The energy then disappears though the warp.\x02\x03",

            "#104FWell, no. It does not 'disappear.'\x02\x03",

            "#102FIt is sent...elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xA,
        (
            "#1125FAnd whatever is located 'elsewhere'\x01",
            "is capable of causing the impossible\x01",
            "effects we've seen.\x02\x03",

            "#1122FYou know, I HOPE I'm misunderstanding\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        (
            "#102FI'm afraid you get a passing grade here,\x01",
            "old friend.\x02\x03",

            "The society can use the Gospels to draw\x01",
            "out and spread the power of whatever this\x01",
            "thing is.\x02\x03",

            "#104FHmph. Spreading the influence of a\x01",
            "mysterious force... No wonder the society\x01",
            "named them 'Gospels.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xA,
        (
            "#1128F...\x02\x03",

            "In that case...the nature of this 'thing'\x01",
            "bothers me.\x02\x03",

            "As you said, even if it's an orbment out\x01",
            "of our purest fiction...or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        (
            "#104F#6PAs far as that goes, I'm afraid I have\x01",
            "no real clue.\x02\x03",

            "I've thought of a number of possibilities,\x01",
            "but that would be pure speculation at this point.\x02\x03",

            "#100FNow, Cassius. I will ask you the same\x01",
            "question I asked you ten years ago.\x02\x03",

            "We're in quite the pickle.\x01",
            "What do you need me to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "#1120FHaha... The exact same words as when I asked\x01",
            "you to develop the patrol airship.\x02\x03",

            "#1125FWell, then...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    Sleep(1200)
    OP_90(0xA, 0x258, 0x0, 0x0, 0x3E8, 0x0)
    Sleep(800)
    OP_8C(0xA, 270, 400)
    Sleep(1000)
    OP_90(0xA, 0xFFFFFB50, 0x0, 0x0, 0x3E8, 0x0)
    Sleep(1500)
    TurnDirection(0xA, 0x8, 400)
    Sleep(500)

    ChrTalk(    #172
        0xA,
        (
            "#1122FThe key, I think, must lie in this 'warp'\x01",
            "the Gospel creates.\x02\x03",

            "Russell. Can you develop some kind of plan\x01",
            "or method of stopping the resonance?\x01",
            "The spread?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#101F#6PHeh heh! Thought you'd ask that.\x02\x03",

            "#100FI'm just about done with my current invention,\x01",
            "anyway.\x02\x03",

            "I'll get to work as soon as I'm done\x01",
            "with that.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/E0001   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_8_4057 end

    def Function_9_563D(): pass

    label("Function_9_563D")

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
        (0, "loc_56B6"),
        (1, "loc_56BC"),
        (SWITCH_DEFAULT, "loc_56C2"),
    )


    label("loc_56B6")

    OP_A2(0x1200)
    Jump("loc_56C2")

    label("loc_56BC")

    OP_A2(0x1201)
    Jump("loc_56C2")

    label("loc_56C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_56D0")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_56D4")

    label("loc_56D0")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_56D4")

    Return()

    # Function_9_563D end

    SaveToFile()

Try(main)
