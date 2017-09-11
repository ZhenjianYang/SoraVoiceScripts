from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3172   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3172.x',
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
        'Professor Russell',                    # 9
        'Factory Chief Murdock',                # 10
        'Orbment',                              # 11
        'Detector Jammer',                      # 12
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
        'ED6_DT07/CH02620 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
        'ED6_DT07/CH00063 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH02620P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
        'ED6_DT07/CH00063P._CP',             # 05
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 917506,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 20,
        Z                   = 700,
        Y                   = 39430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1179650,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 28740,
        Y                   = -2000,
        Z                   = 2700,
        Range               = 30300,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFF060,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_17A",          # 00, 0
        "Function_1_29B",          # 01, 1
        "Function_2_2AC",          # 02, 2
        "Function_3_2C2",          # 03, 3
        "Function_4_420",          # 04, 4
        "Function_5_5B7",          # 05, 5
        "Function_6_C4B",          # 06, 6
        "Function_7_D15",          # 07, 7
        "Function_8_2878",         # 08, 8
        "Function_9_28E4",         # 09, 9
        "Function_10_28F6",        # 0A, 10
        "Function_11_357F",        # 0B, 11
        "Function_12_4479",        # 0C, 12
        "Function_13_4C37",        # 0D, 13
        "Function_14_4DEE",        # 0E, 14
    )


    def Function_0_17A(): pass

    label("Function_0_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_188")
    OP_A3(0x3FA)
    Event(0, 10)

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_19F")
    OP_A3(0x3FB)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_19F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_1AD")
    OP_A3(0x3FC)
    Event(0, 12)

    label("loc_1AD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1BD"),
        (106, "loc_1E6"),
        (SWITCH_DEFAULT, "loc_1F9"),
    )


    label("loc_1BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D0")
    OP_A2(0x50F)
    Event(0, 4)

    label("loc_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E3")
    OP_A2(0x55E)
    Event(0, 13)

    label("loc_1E3")

    Jump("loc_1F9")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F6")
    Event(0, 5)

    label("loc_1F6")

    Jump("loc_1F9")

    label("loc_1F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_END)), "loc_203")
    Jump("loc_220")

    label("loc_203")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_220")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 31850, 0, 30290, 0)

    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_22A")
    Jump("loc_29A")

    label("loc_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_251")
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 30000, -1000, 8900, 270)
    Jump("loc_29A")

    label("loc_251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_271")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 28000, 0, 31400, 180)
    Jump("loc_29A")

    label("loc_271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_29A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 29950, -1000, 8090, 269)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrFlags(0x8, 0x10)

    label("loc_29A")

    Return()

    # Function_0_17A end

    def Function_1_29B(): pass

    label("Function_1_29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AB")
    OP_64(0x0, 0x1)

    label("loc_2AB")

    Return()

    # Function_1_29B end

    def Function_2_2AC(): pass

    label("Function_2_2AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C1")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2AC")

    label("loc_2C1")

    Return()

    # Function_2_2AC end

    def Function_3_2C2(): pass

    label("Function_3_2C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_41C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3DA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36F")

    ChrTalk(    #0
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#010FEstelle, this gentleman seems\x01",
            "a bit preoccupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#010FLet's not disturb him, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#000FYeah, sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D7")

    label("loc_36F")


    ChrTalk(    #5
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#010FThis gentleman seems a\x01",
            "bit preoccupied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#010FLet's not disturb him.\x02",
    )

    CloseMessageWindow()

    label("loc_3D7")

    Jump("loc_41C")

    label("loc_3DA")

    OP_A2(0x0)

    ChrTalk(    #9
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "Looks like the problem's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    label("loc_41C")

    TalkEnd(0xFE)
    Return()

    # Function_3_2C2 end

    def Function_4_420(): pass

    label("Function_4_420")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-380, 0, 8170, 0)
    SetChrPos(0x107, -680, 0, -1960, 225)
    SetChrPos(0x101, -2700, 0, -3100, 0)
    SetChrPos(0x102, -1600, 0, -3600, 0)
    FadeToBright(1000, 0)
    OP_6D(-2000, 0, -600, 3000)

    ChrTalk(    #13
        0x107,
        (
            "#067F#2PHee hee...\x01",
            "This is my house.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #14
        0x101,
        "#001FWow...nice place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        "#010FProfessor Russell is here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x107,
        "#060F#2PNo, I think he's in the workshop.\x02",
    )

    CloseMessageWindow()

    def lambda_53D():
        OP_6D(1070, 0, -1350, 1500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_53D)
    OP_8C(0x107, 90, 400)
    Sleep(300)
    OP_8C(0x102, 90, 400)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x107, 0x2)

    ChrTalk(    #17
        0x107,
        "#060FThrough this door.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#006FWe should go and say hi, then.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_420 end

    def Function_5_5B7(): pass

    label("Function_5_5B7")

    EventBegin(0x0)
    OP_6D(31150, 0, 36720, 0)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x107, 30900, 0, 36300, 225)
    SetChrPos(0x101, 29800, 0, 37500, 180)
    SetChrPos(0x102, 31000, 0, 37400, 225)
    SetChrPos(0x8, 28000, 0, 31400, 180)
    ClearChrFlags(0x107, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x101, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #19
        0x107,
        "#061FI'm home, Grandpa.\x02",
    )

    CloseMessageWindow()
    OP_6D(29900, 0, 34680, 1000)
    Sleep(500)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #20
        0x8,
        (
            "#102F#6PGrrrr...\x02\x03",

            "Okay, maybe this way...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    ChrTalk(    #21
        0x8,
        "#102F#6PGRRRRRR...!!\x02",
    )

    OP_9E(0x8, 0x1E, 0x0, 0x190, 0x1388)
    CloseMessageWindow()
    Sleep(200)

    ChrTalk(    #22
        0x8,
        "#102F#6PAAAAAARRRRGGGGGHHHH...!!\x02",
    )

    OP_9E(0x8, 0x32, 0x0, 0x1F4, 0x1770)
    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        "#065FUhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#501FUh...so this is the professor?\x02",
    )

    CloseMessageWindow()

    def lambda_760():
        OP_6D(29760, 0, 33950, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_760)

    def lambda_778():
        OP_8E(0xFE, 0x7468, 0x0, 0x846C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_778)
    Sleep(800)

    def lambda_798():
        OP_8E(0xFE, 0x797C, 0x0, 0x84D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_798)
    Sleep(200)

    def lambda_7B8():
        OP_8E(0xFE, 0x78B4, 0x0, 0x891C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7B8)
    WaitChrThread(0x101, 0x1)

    def lambda_7D8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D8)
    WaitChrThread(0x107, 0x1)

    def lambda_7EB():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7EB)
    WaitChrThread(0x102, 0x1)

    def lambda_7FE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FE)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #25
        0x101,
        (
            "#006FNice to, um, meet you...\x02\x03",

            "My name is Estelle Bright,\x01",
            "of the Bracer Guild.\x02\x03",

            "We actually came to get\x01",
            "your expert opinion on--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "#102F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#002FUm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "#103F#5S#6PGOT IT!!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #29
        0x101,
        "#004FEek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#101F#6PAh ha ha! I did it!\x01",
            "It's finally complete!\x02\x03",

            "That's right! Who's the man?\x01",
            "I'm the man!\x02\x03",

            "Yes, I should start testing\x01",
            "it at once!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_990():

        label("loc_990")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_990")

    QueueWorkItem2(0x102, 1, lambda_990)

    def lambda_9A1():

        label("loc_9A1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_9A1")

    QueueWorkItem2(0x107, 1, lambda_9A1)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    OP_8C(0x8, 90, 0)
    OP_96(0x8, 0x70A8, 0x0, 0x7CCE, 0x1F4, 0x1770)

    def lambda_9DA():
        OP_6D(29900, 0, 34680, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9DA)

    def lambda_9F2():
        OP_8E(0xFE, 0x7486, 0x0, 0x90BA, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9F2)
    Sleep(200)

    ChrTalk(    #31 op#A op#5
        0x101,
        "#504F#10AWhoa!!\x05\x02",
    )

    OP_43(0x101, 0x1, 0x0, 0x6)
    WaitChrThread(0x8, 0x1)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x4)
    OP_8E(0x8, 0x639C, 0xFFFFF830, 0x91B4, 0x1F40, 0x0)

    def lambda_A51():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_A51)
    OP_8E(0x8, 0x63B0, 0xFFFFF6A0, 0x8778, 0x1F40, 0x0)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    SetChrPos(0x8, 30000, -1000, 8900, 270)

    def lambda_A90():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A90)
    Sleep(1500)
    OP_63(0x101)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 800)
    OP_8C(0x101, 0, 800)

    ChrTalk(    #32
        0x101,
        "#005FWh-What the hell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        (
            "#063FI-I'm sorry, Estelle...\x02\x03",

            "Grandpa kinda goes into a trance when\x01",
            "he's working, and he doesn't really\x01",
            "notice what's going on around him.\x02\x03",

            "I think he just finished up the\x01",
            "device he's been working on for\x01",
            "the past few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        (
            "#014FAh, I see.\x01",
            "He really is something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#007FOh, he's SOMETHING, all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x107,
        "#067FI'm so embarrassed...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x510)
    EventEnd(0x0)
    Return()

    # Function_5_5B7 end

    def Function_6_C4B(): pass

    label("Function_6_C4B")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0x12, 0x0, 0x64)
    OP_8F(0xFE, 0x7620, 0x0, 0x8480, 0x1F40, 0x0)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    OP_8C(0xFE, 270, 1000)
    OP_8C(0xFE, 0, 1000)
    OP_8C(0xFE, 90, 1000)
    OP_8C(0xFE, 180, 1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    OP_62(0xFE, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)
    Return()

    # Function_6_C4B end

    def Function_7_D15(): pass

    label("Function_7_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2877")
    EventBegin(0x0)
    SetMapFlags(0x400000)
    Fade(1000)
    OP_4A(0x8, 255)
    OP_6D(32000, -1000, 10100, 0)
    SetChrPos(0x107, 31500, -1000, 200, 0)
    SetChrPos(0x101, 30600, -1000, -800, 0)
    SetChrPos(0x102, 31800, -1000, -1000, 0)
    OP_0D()

    def lambda_D7C():

        label("loc_D7C")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_D7C")

    QueueWorkItem2(0x101, 1, lambda_D7C)

    def lambda_D8D():

        label("loc_D8D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_D8D")

    QueueWorkItem2(0x102, 1, lambda_D8D)

    def lambda_D9E():

        label("loc_D9E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_D9E")

    QueueWorkItem2(0x107, 1, lambda_D9E)

    def lambda_DAF():
        OP_8E(0xFE, 0x7A44, 0xFFFFFC18, 0x1DB0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_DAF)
    Sleep(100)

    def lambda_DCF():
        OP_8E(0xFE, 0x7788, 0xFFFFFC18, 0x1838, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DCF)
    Sleep(100)

    def lambda_DEF():
        OP_8E(0xFE, 0x7C38, 0xFFFFFC18, 0x189C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DEF)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #37
        0x107,
        (
            "#560F#2PGrandpa!\x02\x03",

            "There are some people here\x01",
            "who need to talk to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "#103F#1PHm...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #39
        0x8,
        (
            "#101F#1POh, Tita! You've come\x01",
            "at just the right time!\x02\x03",

            "I need your help with compiling\x01",
            "the data from these tests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x107,
        "#065F#2PUm, but, Grandpa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "#102F#1PThis new invention will actually\x01",
            "block a biosensor orbment's\x01",
            "detection faculties.\x02\x03",

            "It emits a unique orbal force field\x01",
            "that deflects the energy that a\x01",
            "biosensor sends out when it scans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x107,
        "#064F#2POh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#101F#1PYes, really. Since when do I overstate\x01",
            "my own accomplishments?\x02\x03",

            "Now, come on!\x01",
            "We've got testing to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x107,
        "#061F#2PRight!\x02",
    )

    CloseMessageWindow()

    def lambda_1075():
        OP_6D(32910, -1000, 8880, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1075)

    def lambda_108D():
        OP_8E(0xFE, 0x7EFD, 0xFFFFFC18, 0x2936, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_108D)
    Sleep(300)

    def lambda_10AD():
        OP_8E(0xFE, 0x8692, 0xFFFFFC18, 0x2102, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_10AD)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 400)
    WaitChrThread(0x8, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #45
        (
            "\x07\x05Professor Russell and Tita began working\x01",
            "with some complex-looking equipment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x101,
        "#509FHey now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#019FNever mind, Estelle. I think\x01",
            "we should just let them be\x01",
            "for a little while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #48
        0x8,
        "#102FHey! You, with the black hair!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        "#014FWho? Me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#102FWho else?\x02\x03",

            "On the upstairs bookcase is a notebook\x01",
            "titled, 'Orbal Energy as Applied to Force\x01",
            "Fields.' Go get it!\x02\x03",

            "Go on, be quick about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        "#012FA-All right.\x02",
    )

    CloseMessageWindow()

    def lambda_12F6():

        label("loc_12F6")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_12F6")

    QueueWorkItem2(0x101, 1, lambda_12F6)
    OP_8C(0x102, 180, 600)
    OP_43(0x102, 0x1, 0x0, 0x8)
    Sleep(1000)

    ChrTalk(    #52
        0x101,
        "#004FWait... Joshua...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#102FHey! Young lady! You\x01",
            "with the antenna hair!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #54
        0x101,
        "#509F#4PA-Antenna...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 800)

    ChrTalk(    #55
        0x101,
        "#005F#4POh, no, you didn't!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#102FQuit farting around and\x01",
            "make some coffee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#009F#4PWhy should I have to\x01",
            "make you coffee?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#101FI take it black, by the way.\x02\x03",

            "I want it clear as mud!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#509F#4PYou're not hearing a word\x01",
            "I say...\x02\x03",

            "#007F*sigh*\x01",
            "Fine. Whatever!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 800)
    OP_8E(0x101, 0x797C, 0xFFFFFC18, 0x3E8, 0x1770, 0x0)

    def lambda_14DB():
        OP_8E(0xFE, 0x51A4, 0x0, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14DB)
    OP_6D(34600, -1000, 10700, 2000)

    ChrTalk(    #60
        0x107,
        "#061F#2P...Yep, perfect!♪\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #61
        0x107,
        "#560F#2PAll set, Grandpa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        "#101F#1PJust as fast as ever!\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #63
        0x107,
        "#064F#2POh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)
    Sleep(200)
    OP_8C(0x107, 270, 400)
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x107,
        (
            "#065F#2PUm...\x01",
            "Where are Estelle and Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#103F#1PWho?\x02\x03",

            "...\x02\x03",

            "Come to think of it, I do vaguely\x01",
            "recall a couple of young folks...\x02\x03",

            "Chief Murdock sent along some fresh\x01",
            "faces, then, I presume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x107,
        "#561F#2PG-Grandpa...\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(    #67
        (
            "\x07\x05And so, Estelle and Joshua inadvertently\x01",
            "wound up as assistants in the experiment.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #68
        (
            "\x07\x05After many small (but relatively harmless) explosions\x01",
            "and some singeing of the eyebrows, the day gave way\x01",
            "to evening...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    OP_6D(-300, 0, 2200, 0)
    SetChrPos(0x101, -2000, 0, 2000, 90)
    SetChrPos(0x102, -2000, 0, 500, 90)
    SetChrPos(0x107, 200, 0, 2000, 270)
    SetChrPos(0x8, 200, 0, 500, 270)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    ClearChrFlags(0x102, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x107, 5)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x107, 0x4)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #69
        0x8,
        (
            "#101FHa ha ha!\x01",
            "Sorry about all that.\x02\x03",

            "I just assumed you were\x01",
            "both new employees at the\x01",
            "central factory.\x02\x03",

            "So it's only natural that you\x01",
            "wound up being drafted as\x01",
            "assistants.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#009FGrr...\x01",
            "This is no laughing matter.\x02\x03",

            "Especially since the only thing you had me\x01",
            "helping with was making coffee! Girls can\x01",
            "bang metal parts together, too, old man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#019FRelax, Estelle. We got some\x01",
            "valuable experience out of the\x01",
            "deal, in the end.\x02\x03",

            "How often does one get to participate\x01",
            "in startup tests on a brand-new type\x01",
            "of orbment, after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#103FWell, now. You're a bright lad,\x01",
            "then, aren't you?\x02\x03",

            "Want to give up this bracer \x01",
            "nonsense and start up in the\x01",
            "field of orbal engineering?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x107,
        (
            "#561FGrandpa!\x02\x03",

            "#560FI'm really sorry, guys...\x02\x03",

            "I guess I got caught up in\x01",
            "the moment, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#008FYou don't need to apologize,\x01",
            "sweetie.\x02\x03",

            "#007FBut I thought the 'Father of the\x01",
            "Orbal Revolution' was going to\x01",
            "be some really amazing man...\x02\x03",

            "Not some old fart with \x01",
            "attention deficit issues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#101FHa ha ha!\x01",
            "Please, you're too kind.\x02\x03",

            "#102FMoving on! So I'm being paid a\x01",
            "visit by the children of Cassius.\x02\x03",

            "That's quite the surprise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#501FSo you really do know our dad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#104FYes, from way back when.\x02\x03",

            "I've known him since his army\x01",
            "days, some 20 years or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x107,
        (
            "#064FI've met him, too.\x02\x03",

            "He had the really nice\x01",
            "mustache, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#007FWeeeell... I don't know if I'd\x01",
            "call it 'nice,' so much as\x01",
            "'suspicious-looking.'\x02\x03",

            "#006FBut if he's known dad for that long, it looks\x01",
            "like we'll be safe entrusting you-know-what\x01",
            "with Professor Russell after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        "#010FYes, I have to agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        "#064F???\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#103FWhat are you talking about?\x02\x03",

            "And what was it you wanted\x01",
            "my help with?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#002FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #84
        (
            "\x07\x05Estelle explained to the professor the whole sequence\x01",
            "of events surrounding the black orbment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(500)
    SetChrPos(0xA, -560, 800, 270, 0)
    ClearChrFlags(0xA, 0x80)
    OP_0D()
    Sleep(500)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x8,
        "#103F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x107,
        "#064FWow...a pitch-black orbment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#102FYes. Quite intriguing.\x02\x03",

            "And with no inscribed caliber\x01",
            "or seams...\x02\x03",

            "Look at that frame, too...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #88
        (
            "\x07\x05Professor Russell produced a cutting tool\x01",
            "from his belt.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "\x07\x05Without a word, he pushed the blade's edge\x01",
            "against the outer shell of the orbment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #90
        0x101,
        "#004FWait, what are you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        "#012FIt's a special alloy steel cutter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#102F...\x02\x03",

            "#104FJust as I thought...\x02\x03",

            "#100FHere, take a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#506FO-Okay...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #94
        (
            "\x07\x05Estelle, Joshua and Tita peered intently\x01",
            "at the black orbment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #95
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x107,
        "#065FThere's not even a scratch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#104FThe frame is made from some\x01",
            "type of metal that I've never\x01",
            "before encountered.\x02\x03",

            "Opening it up for a closer look\x01",
            "is going to be quite the task,\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#002FTh-That's just crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x102,
        (
            "#013FIf we can't find some way to\x01",
            "open it, we'll be right back\x01",
            "to square one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#102FWell, I can certainly spend\x01",
            "some time on trying...\x02\x03",

            "But first, I think that maybe we\x01",
            "should put it under a measurement\x01",
            "scan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#004FA what, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x107,
        (
            "#560FThat huge piece of equipment\x01",
            "you saw when we were working\x01",
            "on the experiment.\x02\x03",

            "It can gauge orbal energy\x01",
            "activity in real time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#006F...You're making my head hurt with\x01",
            "your techno-babble. Just tell me\x01",
            "what using that thing'll accomplish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "#102FTo put it in layman's terms, it'll allow us to\x01",
            "see just what this orbment does.\x02\x03",

            "We won't be able to draw any definitive\x01",
            "conclusions just from measuring what kind of\x01",
            "orbal activity is occurring, but it's a start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x102,
        (
            "#0102FAnd that should give us a\x01",
            "major clue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "#104FIndeed.\x02\x03",

            "So, without further ado...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x107,
        (
            "#060FGrandpa... Shouldn't we have\x01",
            "lunch, first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        "#103FSure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x107,
        (
            "#067FEstelle and Joshua, you're\x01",
            "both welcome to join us.\x02\x03",

            "I can't promise it'll be\x01",
            "anything special, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#001FSounds great to me!♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        "#010FWe'll even help with prep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "#101FAll right. Come on, then.\x02\x03",

            "I've got a bit to do while\x01",
            "lunch is prepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x107,
        (
            "#062FNoooooo!\x01",
            "I wanna see it, too.\x02\x03",

            "No fair working when\x01",
            "I'm not around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        "#104FMy house, my rules!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x101,
        "#509F(What is UP with these two...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        "#019F(Now I see where she gets it...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3133   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2877")

    Return()

    # Function_7_D15 end

    def Function_8_2878(): pass

    label("Function_8_2878")

    OP_8E(0xFE, 0x7850, 0xFFFFFC18, 0x1CC, 0x1388, 0x0)
    OP_8E(0xFE, 0x5B90, 0x0, 0xBE, 0x1388, 0x0)
    OP_44(0x101, 0xFF)
    OP_8E(0xFE, 0x5A3C, 0x7D0, 0x22F6, 0x1388, 0x0)

    def lambda_28BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28BE)
    OP_8E(0xFE, 0x659A, 0xFA0, 0x23A0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_8_2878 end

    def Function_9_28E4(): pass

    label("Function_9_28E4")

    OP_A6(0x1)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    OP_A3(0x1)
    Return()

    # Function_9_28E4 end

    def Function_10_28F6(): pass

    label("Function_10_28F6")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(32860, -1000, 8930, 0)
    SetChrPos(0x107, 32509, -1000, 10550, 180)
    SetChrPos(0x8, 34450, -1000, 8450, 270)
    SetChrPos(0x101, 31580, -1000, 8390, 45)
    SetChrPos(0x102, 32080, -1000, 7470, 45)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #118
        0x8,
        (
            "#104FAhem!\x02\x03",

            "Now, if everyone is ready,\x01",
            "let's get this started.\x02\x03",

            "#102FEstelle, if you'll put the\x01",
            "orbment on the stand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#002FOkay...\x02",
    )

    CloseMessageWindow()

    def lambda_29F5():
        OP_6D(33550, -1000, 9600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29F5)
    SetChrFlags(0x101, 0x4)

    def lambda_2A12():
        OP_8E(0xFE, 0x811A, 0xFFFFFC18, 0x279C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A12)
    Sleep(300)

    def lambda_2A32():

        label("loc_2A32")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2A32")

    QueueWorkItem2(0x107, 2, lambda_2A32)

    def lambda_2A43():

        label("loc_2A43")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2A43")

    QueueWorkItem2(0x8, 2, lambda_2A43)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 90, 400)
    WaitChrThread(0x101, 0x2)
    Fade(500)
    OP_22(0x82, 0x0, 0x64)
    SetChrPos(0xA, 34310, -270, 10390, 0)
    ClearChrFlags(0xA, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #120
        0x101,
        "#501FLike this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        "#102FYes, thank you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)
    OP_44(0x107, 0xFF)
    OP_44(0x8, 0xFF)

    def lambda_2AC9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2AC9)

    def lambda_2AD7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2AD7)
    OP_8E(0x101, 0x7B5C, 0xFFFFFC18, 0x20C6, 0xBB8, 0x0)
    OP_8C(0x101, 45, 400)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(    #122
        0x8,
        "#100FAre you ready, Tita?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x107,
        "#061FAll set.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "#104FGood, good.\x02\x03",

            "#102FNow commencing orbal force \x01",
            "measurement test on...the\x01",
            "Black Orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#014F'Black Orbment'? So that's going to be\x01",
            "the official name after all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#000FBut using it officially is so boring and...simple.\x01",
            "Why not something cool like...\x01",
            "Dark Thingy of Impending DOOM?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x8,
        (
            "#100FNo, no. Simple is best.\x02\x03",

            "Anything longer than 'Black Orbment'\x01",
            "would just be annoying to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x107,
        "#560F*fidget* *fidget*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#506FAwww... Look at her.\x01",
            "She's all anxious to start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x107,
        (
            "#067FHuh...?\x01",
            "Oh, hee hee...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "#102FAll right. Let's begin.\x02\x03",

            "Tita, if you'll activate\x01",
            "the scanner, please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x107,
        "#062FOkay.\x02",
    )

    CloseMessageWindow()

    def lambda_2DA1():
        OP_6D(34330, -1000, 10370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2DA1)
    OP_20(0x3E8)
    OP_8C(0x107, 0, 400)
    OP_8C(0x8, 90, 400)
    OP_21()
    OP_22(0x9D, 0x0, 0x64)
    OP_1D(0x57)
    LoadEffect(0x3, "map\\\\mp029_00.eff")
    LoadEffect(0x4, "map\\\\mp029_01.eff")
    LoadEffect(0x5, "map\\\\mp029_02.eff")
    PlayEffect(0x3, 0x3, 0xFF, 33570, -400, 9620, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0xFF, 31600, -500, 11150, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #133
        0x8,
        (
            "#102FOutput set at 45..\x02\x03",

            "Put all measuring equipment\x01",
            "on standby...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x107,
        "#062FRoger...\x02",
    )

    CloseMessageWindow()
    OP_22(0x9E, 0x1, 0x64)
    Sleep(200)
    PlayEffect(0x4, 0x5, 0xFF, 35680, 750, 10480, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0x6, 0xFF, 35820, 750, 9630, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0x7, 0xFF, 35390, 930, 7320, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0x2, 0xFF, 35360, 930, 6080, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #135
        0x107,
        (
            "#560FDone. All measuring equipment\x01",
            "is calibrated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "#102FOkay, from here on out\x01",
            "is the real deal.\x02\x03",

            "Since no direct input or output was\x01",
            "detected, all we can do is measure how\x01",
            "the central crystal circuit responds...\x02\x03",

            "#101FNow let's see just how much\x01",
            "this contraption is really worth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#506FYou're sure in a good mood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        "#102FAaaaand CLICK!\x02",
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    OP_8C(0x8, 0, 300)
    OP_22(0xC9, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp025_00.eff")
    PlayEffect(0x0, 0x0, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #139
        0x101,
        (
            "#501FNeat...\x01",
            "It's all glowing and stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x102,
        (
            "#010FI get it. It's putting a major\x01",
            "strain on the crystal circuit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        "#101FThere, there...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 300)

    ChrTalk(    #142
        0x8,
        "#100FTita! Any readings?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x107,
        (
            "#063FY-Yes...\x02\x03",

            "But they're kind of weird...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        "#103FHmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x107,
        (
            "#063FThe tachometer needle's\x01",
            "shaking like crazy.\x02\x03",

            "#065FAh...\x02\x03",

            "N-Now it's spinning around\x01",
            "the dial!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        "#102FWhat?!\x02",
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_1D(0x5C)
    OP_77(0x82, 0xFF, 0xFF, 0x138800, 0x0)

    def lambda_3308():
        OP_6D(34810, -500, 10930, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3308)

    def lambda_3320():
        OP_6B(3160, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3320)

    def lambda_3330():
        OP_67(0, 3400, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3330)
    Sleep(1000)
    OP_23(0x9E)
    OP_23(0xC9)
    OP_22(0x90, 0x0, 0x64)
    LoadEffect(0x0, "map\\\\mp007_00.eff")
    PlayEffect(0x0, 0x1, 0xA, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x8, 0, 400)
    OP_8C(0x107, 90, 400)
    WaitChrThread(0x101, 0x3)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_33D8():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_33D8)
    Sleep(100)

    def lambda_33F3():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_33F3)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #147
        0x107,
        "#068FEek!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        "#102FWhat's going on here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#005F#1PJoshua...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#016F#2PIt's that same black light\x01",
            "from before!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x91, 0x0, 0x64)
    LoadEffect(0x2, "map\\\\mp015_00.eff")
    PlayEffect(0x2, 0xFF, 0xA, 0, 300, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xA, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    OP_82(0x3, 0x0)
    Sleep(50)
    OP_82(0x5, 0x0)
    Sleep(50)
    OP_82(0x6, 0x0)
    Sleep(50)
    OP_82(0x4, 0x0)
    Sleep(50)
    OP_82(0x7, 0x0)
    Sleep(50)
    OP_82(0x2, 0x0)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 270, 400)

    ChrTalk(    #151
        0x8,
        "#103FWHAT?! \x02",
    )

    CloseMessageWindow()
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_28F6 end

    def Function_11_357F(): pass

    label("Function_11_357F")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(34700, -1000, 10700, 0)
    OP_77(0x82, 0xFF, 0xFF, 0x0, 0x0)
    LoadEffect(0x0, "map\\\\mp025_00.eff")
    PlayEffect(0x0, 0x0, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x90, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp007_00.eff")
    PlayEffect(0x1, 0x1, 0xA, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x8, 255)
    SetChrPos(0x8, 34400, -1000, 8900, 0)
    SetChrPos(0x107, 32759, -1000, 8640, 90)
    SetChrPos(0x101, 26210, 0, -230, 78)
    SetChrPos(0x102, 26210, 0, -230, 78)
    SetChrPos(0xA, 34310, -270, 10390, 0)
    ClearChrFlags(0xA, 0x80)
    OP_6D(34810, -500, 10930, 0)
    OP_6B(3160, 0)
    OP_67(0, 3400, -10000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #152
        0x107,
        (
            "#068FGr-Grandpa! It won't take\x01",
            "much more of this!\x02\x03",

            "We have to shut it down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x8,
        (
            "#102FDon't you dare!\x02\x03",

            "Just a little longer and\x01",
            "we'll have something...!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x101, 0x765C, 0xFFFFFC18, 0x384, 0x1770, 0x0)
    OP_8E(0x101, 0x8278, 0xFFFFFC18, 0x1900, 0x1770, 0x0)
    OP_8C(0x101, 0, 800)

    ChrTalk(    #154
        0x101,
        (
            "#005FWait a second! All the lights\x01",
            "in town are going out!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 800)

    ChrTalk(    #155
        0x107,
        "#065FHuh?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 800)

    ChrTalk(    #156
        0x8,
        (
            "#103FWhat in...\x02\x03",

            "#102FBah! We have no choice, then!\x01",
            "Terminating the experiment!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x86B0, 0xFFFFFC18, 0x20C6, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)
    Sleep(500)
    OP_22(0xE1, 0x0, 0x64)
    Sleep(500)
    OP_20(0xBB8)
    OP_77(0xFF, 0xFF, 0xFF, 0x138800, 0x0)

    def lambda_3899():
        OP_6D(34330, -1000, 10370, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3899)

    def lambda_38B1():
        OP_6B(2750, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_38B1)

    def lambda_38C1():
        OP_67(0, 6150, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_38C1)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0x90)
    LoadEffect(0x3, "map\\\\mp029_00.eff")
    LoadEffect(0x4, "map\\\\mp029_01.eff")
    LoadEffect(0x5, "map\\\\mp029_02.eff")
    Sleep(300)
    Sleep(300)
    PlayEffect(0x4, 0xFF, 0xFF, 31600, -500, 11150, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x4, 0xFF, 0xFF, 35680, 750, 10480, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x4, 0xFF, 0xFF, 35820, 750, 9630, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x4, 0xFF, 0xFF, 35390, 930, 7320, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x4, 0xFF, 0xFF, 35360, 930, 6080, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8C(0x8, 0, 400)
    OP_8C(0x107, 45, 400)
    WaitChrThread(0x101, 0x3)
    OP_21()
    OP_1D(0x54)

    ChrTalk(    #157
        0x101,
        (
            "#004FOh...\x02\x03",

            "Th-They're back on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x107,
        "#561F#1PWhew...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    ChrTalk(    #159
        0x8,
        (
            "#102FLet's see the readout...\x02\x03",

            "...Nothing.\x01",
            "It didn't record anything.\x02\x03",

            "And the only thing that kept working\x01",
            "was the scanner on which the Black\x01",
            "Orbment sat, but even that, well...\x02\x03",

            "As for everything else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x102,
        (
            "#2PGood... It looks like the\x01",
            "experiment's finished.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BAF():

        label("loc_3BAF")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_3BAF")

    QueueWorkItem2(0x101, 1, lambda_3BAF)

    def lambda_3BC0():

        label("loc_3BC0")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_3BC0")

    QueueWorkItem2(0x107, 1, lambda_3BC0)

    def lambda_3BD1():

        label("loc_3BD1")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_3BD1")

    QueueWorkItem2(0x8, 1, lambda_3BD1)

    def lambda_3BE2():
        OP_6D(32900, -1000, 8060, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BE2)
    OP_8E(0x102, 0x765C, 0xFFFFFC18, 0x384, 0xFA0, 0x0)
    OP_8E(0x102, 0x7B0C, 0xFFFFFC18, 0x17D4, 0xFA0, 0x0)
    OP_8C(0x102, 45, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x8, 0xFF)

    ChrTalk(    #161
        0x101,
        "#002FHow's it outside?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x102,
        (
            "#010FFine... All the lights are back,\x01",
            "like nothing happened.\x02\x03",

            "There's still a lot of people panicking though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#007FOkay...\x02\x03",

            "#505FBut just what the hell was\x01",
            "all that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "#104FThat...\x02\x03",

            "#102F...was what I would dub the \x01",
            "'Orbal Shutdown Phenomenon.'\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D53():
        TurnDirection(0x102, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D53)

    def lambda_3D61():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3D61)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #165
        0x101,
        "#004FThe what-down?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x102,
        (
            "#012FYou mean how everything inside \x01",
            "all the orbments just stopped\x01",
            "working at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x107,
        "#063FSo the Black Orbment did this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x8,
        (
            "#104FYes, I've no doubt.\x02\x03",

            "#102FBut I would never have dared\x01",
            "to guess that its effect would\x01",
            "be so extensive.\x02\x03",

            "Hmm... There's definitely\x01",
            "more to this than I expected.\x02\x03",

            "#101FInteresting! Most interesting,\x01",
            "indeed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#509FOnly YOU would think causing\x01",
            "a blackout over an entire city\x01",
            "is 'interesting'...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 26210, 0, -230, 78)

    NpcTalk(    #170
        0x9,
        "Man's Voice",
        "#2PPROFESSOOOOOORR!!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)

    def lambda_3FD0():

        label("loc_3FD0")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3FD0")

    QueueWorkItem2(0x101, 1, lambda_3FD0)

    def lambda_3FE1():

        label("loc_3FE1")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3FE1")

    QueueWorkItem2(0x107, 1, lambda_3FE1)

    def lambda_3FF2():

        label("loc_3FF2")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3FF2")

    QueueWorkItem2(0x102, 1, lambda_3FF2)

    def lambda_4003():

        label("loc_4003")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_4003")

    QueueWorkItem2(0x8, 1, lambda_4003)
    OP_8E(0x9, 0x765C, 0xFFFFFC18, 0x384, 0x1770, 0x0)
    OP_8E(0x9, 0x7E68, 0xFFFFFC18, 0x1900, 0x1770, 0x0)
    OP_8E(0x9, 0x817E, 0xFFFFFC18, 0x1D24, 0x1770, 0x0)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(    #171
        0x8,
        (
            "#103FAhh, Murdock. Just the\x01",
            "man I wanted to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x9,
        (
            "#804F#6PThe feeling is NOT mutual!\x02\x03",

            "Every single time you invent\x01",
            "something, it means trouble\x01",
            "for ME.\x02\x03",

            "What the hell were you up to\x01",
            "that would cause all of the\x01",
            "power downtown to go out?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#104FHow rude. It's not even\x01",
            "my fault this time.\x02\x03",

            "See that, there? That's the\x01",
            "Black Orbment, and IT caused\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        (
            "#802F#6PIs that the...\x02\x03",

            "#803FOkay, I get it. If that's the\x01",
            "root of this, then it's genuine\x01",
            "extenuating circumstances.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x9)

    ChrTalk(    #175
        0x9,
        (
            "#804F#6P#3SBut it still means that\x01",
            "this was your fault!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#102FAhh, nuts.\x01",
            "You got me...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #177
        0x101,
        (
            "#006FThat's it?\x01",
            "They're just okay again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        "#010FAre they always like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x107,
        "#067FThis is so embarrassing...\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(    #180
        "\x07\x05And so, the first day in Zeiss kept everyone busy.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #181
        "\x07\x05Due to how late it was, Estelle and Joshua stayed at the lab for the night.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xD, 0x0, 0x64)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Sleep(5000)
    OP_A2(0x511)
    OP_28(0x3F, 0x1, 0x10)
    OP_28(0x3F, 0x1, 0x20)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_357F end

    def Function_12_4479(): pass

    label("Function_12_4479")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-2900, 0, 34200, 0)
    SetChrPos(0x102, -4100, 0, 33700, 180)
    SetChrPos(0x101, -5000, 0, 31300, 0)
    SetChrPos(0x107, -5900, -2000, 39200, 0)
    SetChrFlags(0x107, 0x80)

    ChrTalk(    #182
        0x101,
        (
            "#000FMan... Yesterday was such\x01",
            "a crazy day.\x02\x03",

            "I was surprised enough at the town,\x01",
            "but I really wasn't expecting to\x01",
            "deal with anything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        (
            "#010FHa ha. No kidding.\x02\x03",

            "But back on the subject\x01",
            "of the black orbment...\x02\x03",

            "It's much more powerful than\x01",
            "I'd ever imagined possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#000FYeah...\x02\x03",

            "What's the professor gonna do,\x01",
            "now that his equipment's gone\x01",
            "all kerflooey?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x107,
        "#060FGood morning, guys!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)
    ClearChrFlags(0x107, 0x80)

    def lambda_4675():

        label("loc_4675")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_4675")

    QueueWorkItem2(0x101, 1, lambda_4675)

    def lambda_4686():

        label("loc_4686")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_4686")

    QueueWorkItem2(0x102, 1, lambda_4686)
    OP_8E(0x107, 0xFFFFF8F8, 0x0, 0x9858, 0xBB8, 0x0)
    OP_8E(0x107, 0xFFFFF8F8, 0x0, 0x8E30, 0x7D0, 0x0)
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #186
        0x101,
        "#000FMorning, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x102,
        (
            "#010FGood morning...\x01",
            "Quite a big day yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x107,
        (
            "#060FHee hee, no kidding!\x02\x03",

            "Did you guys sleep okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#000FYep, like babies. ㈱\x02\x03",

            "Is the professor already up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x107,
        (
            "#060FOh, he left for the central factory early this\x01",
            "morning.\x02\x03",

            "He said something about how he was going to\x01",
            "expose all the Black Orbment's secrets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#000FWow. Looks like getting roared at over and\x01",
            "over by the factory chief yesterday didn't\x01",
            "even put a dent in him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x102,
        (
            "#010FWe really appreciate both of you taking the\x01",
            "time just to look over something a couple\x01",
            "of relative strangers brought you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x107,
        (
            "#060FOh, it's fine, really.\x02\x03",

            "Grandpa's investigating it out of pure\x01",
            "curiosity more than anything.\x02\x03",

            "I should go to the factory myself,\x01",
            "once I'm done with breakfast.\x02\x03",

            "What do you plan to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        "#000FNaturally, we'll be coming with you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x102,
        (
            "#010FMaybe there's something\x01",
            "we can do to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x107,
        (
            "#060FYay! Then you can come\x01",
            "with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x107,
        (
            "#060FUh-oh! I almost forgot about\x01",
            "the soup!\x02\x03",

            "Just a second, you two! I'll bring\x01",
            "you breakfast as soon as I make sure\x01",
            "it's edible, and not on fire!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x107, 0xFFFFF8F8, 0x0, 0x9858, 0x1770, 0x0)
    OP_8E(0x107, 0xFFFFE8F4, 0xFFFFF830, 0x9920, 0x1770, 0x0)
    SetChrFlags(0x107, 0x80)

    ChrTalk(    #198
        0x101,
        (
            "#000FI guess that's what that smell is...\x01",
            "But man, what a cutie! I wish we could\x01",
            "take her back with us to Rolent.\x02\x03",

            "She could be like a pet, cheering\x01",
            "us up whenever we're feeling down!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #199
        0x102,
        "#010FThat's...kind of creepy, Estelle.\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_4479 end

    def Function_13_4C37(): pass

    label("Function_13_4C37")

    EventBegin(0x0)
    OP_6D(-1780, 0, -950, 0)
    SetChrPos(0x107, -2009, 0, -2300, 0)
    SetChrPos(0x101, -1530, 0, -3110, 0)
    SetChrPos(0x102, -3180, 0, -3090, 0)
    SetChrPos(0x106, -2410, 0, -3780, 0)
    OP_0D()

    ChrTalk(    #200
        0x101,
        (
            "#000FNow...where is that thing?\x02\x03",

            "It's gotta be here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4CD9():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4CD9)

    def lambda_4CE7():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CE7)

    def lambda_4CF5():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4CF5)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #201
        0x107,
        (
            "#060FUmm...maybe in a corner\x01",
            "of the lab or the second\x01",
            "floor archives?\x02\x03",

            "Those are where Grandpa\x01",
            "usually tosses stuff from\x01",
            "his old inventions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x106,
        (
            "#050FEccentric old coot...\x02\x03",

            "But whatever. Let's just\x01",
            "find the damn thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x43, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_13_4C37 end

    def Function_14_4DEE(): pass

    label("Function_14_4DEE")

    EventBegin(0x0)
    OP_6D(25700, -60, 31320, 1000)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #203
        "\x07\x05Found Detector Jammer.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x55F)
    OP_28(0x43, 0x1, 0x100)

    ChrTalk(    #204
        0x101,
        "#000FFound it! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#010FThat's the orbment that was\x01",
            "in our experiment, all right.\x02\x03",

            "So...can we use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x107,
        (
            "#060FI think so.\x02\x03",

            "If everything performs to specs,\x01",
            "then it'll keep a biosensor from\x01",
            "working right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x106,
        (
            "#050FAll right. Back to the guild, then.\x02\x03",

            "Kilika's probably finished collecting\x01",
            "intel on Leiston Fortress by now.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_14_4DEE end

    SaveToFile()

Try(main)
