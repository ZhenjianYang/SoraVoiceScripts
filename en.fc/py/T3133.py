from ED6ScenarioHelper import *

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
        'Black Orbment',                        # 11
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
        'ED6_DT07/CH01250 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
        'ED6_DT07/CH00003 ._CH',             # 03
        'ED6_DT07/CH00013 ._CH',             # 04
        'ED6_DT07/CH00063 ._CH',             # 05
        'ED6_DT06/CH20130 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH01250P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
        'ED6_DT07/CH00003P._CP',             # 03
        'ED6_DT07/CH00013P._CP',             # 04
        'ED6_DT07/CH00063P._CP',             # 05
        'ED6_DT06/CH20130P._CP',             # 06
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


    DeclActor(
        TriggerX            = 31850,
        TriggerZ            = 0,
        TriggerY            = 30290,
        TriggerRange        = 800,
        ActorX              = 31850,
        ActorZ              = 500,
        ActorY              = 30290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_2FA",          # 01, 1
        "Function_2_339",          # 02, 2
        "Function_3_34F",          # 03, 3
        "Function_4_4AD",          # 04, 4
        "Function_5_644",          # 05, 5
        "Function_6_D9D",          # 06, 6
        "Function_7_E67",          # 07, 7
        "Function_8_1A90",         # 08, 8
        "Function_9_2BFF",         # 09, 9
        "Function_10_2C6B",        # 0A, 10
        "Function_11_2C7D",        # 0B, 11
        "Function_12_336E",        # 0C, 12
        "Function_13_3DFD",        # 0D, 13
        "Function_14_46B0",        # 0E, 14
        "Function_15_487B",        # 0F, 15
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1B4")
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_1C2")
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_1D0")
    OP_A3(0x3FC)
    Event(0, 13)

    label("loc_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_1E7")
    OP_A3(0x3FD)
    Event(0, 8)
    OP_B1("t3133_y")

    label("loc_1E7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1F7"),
        (106, "loc_225"),
        (SWITCH_DEFAULT, "loc_238"),
    )


    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A")
    OP_A2(0x50F)
    Event(0, 4)

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_222")
    SetMapFlags(0x10000000)
    OP_A2(0x55E)
    Event(0, 14)

    label("loc_222")

    Jump("loc_238")

    label("loc_225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_235")
    Event(0, 5)

    label("loc_235")

    Jump("loc_238")

    label("loc_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_END)), "loc_242")
    Jump("loc_27F")

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_262")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 31850, 0, 30290, 0)
    Jump("loc_27F")

    label("loc_262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_27F")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 34470, -300, 10490, 0)

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_289")
    Jump("loc_2F9")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_END)), "loc_2B0")
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrPos(0x8, 30000, -1000, 8900, 270)
    Jump("loc_2F9")

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_2D0")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 28000, 0, 31400, 180)
    Jump("loc_2F9")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F9")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 29950, -1000, 8090, 269)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrFlags(0x8, 0x10)

    label("loc_2F9")

    Return()

    # Function_0_1A6 end

    def Function_1_2FA(): pass

    label("Function_1_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_312")
    OP_B1("t3133_y")
    Jump("loc_31B")

    label("loc_312")

    OP_B1("t3133_n")

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_32B")
    OP_64(0x0, 0x1)

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_338")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)

    label("loc_338")

    Return()

    # Function_1_2FA end

    def Function_2_339(): pass

    label("Function_2_339")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_339")

    label("loc_34E")

    Return()

    # Function_2_339 end

    def Function_3_34F(): pass

    label("Function_3_34F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_467")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC")

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
    Jump("loc_464")

    label("loc_3FC")


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

    label("loc_464")

    Jump("loc_4A9")

    label("loc_467")

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

    label("loc_4A9")

    TalkEnd(0xFE)
    Return()

    # Function_3_34F end

    def Function_4_4AD(): pass

    label("Function_4_4AD")

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
            "#067F#4PHee hee...\x01",
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
        "#060F#4PNo, I think he's in the workshop.\x02",
    )

    CloseMessageWindow()

    def lambda_5CA():
        OP_6D(1070, 0, -1350, 1500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_5CA)
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

    # Function_4_4AD end

    def Function_5_644(): pass

    label("Function_5_644")

    EventBegin(0x0)
    OP_6D(31150, 0, 36720, 0)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x107, 30900, 0, 36300, 225)
    SetChrPos(0x101, 29800, 0, 37500, 180)
    SetChrPos(0x102, 31000, 0, 37400, 225)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 27800, 500, 31400, 180)
    SetChrChipByIndex(0x8, 6)

    def lambda_6BF():

        label("loc_6BF")

        OP_99(0xFE, 0x1, 0x2, 0x3E8)
        OP_48()
        Jump("loc_6BF")

    QueueWorkItem2(0x8, 1, lambda_6BF)
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
            "#102F#5PGrrrr...\x02\x03",

            "Okay, maybe this way...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_760():

        label("loc_760")

        OP_99(0xFE, 0x1, 0x2, 0x5DC)
        OP_48()
        Jump("loc_760")

    QueueWorkItem2(0x8, 1, lambda_760)
    Sleep(200)

    ChrTalk(    #21
        0x8,
        "#102F#5PGRRRRRR...!!\x02",
    )

    OP_9E(0x8, 0x1E, 0x0, 0x190, 0x1388)
    CloseMessageWindow()

    def lambda_7A5():

        label("loc_7A5")

        OP_99(0xFE, 0x1, 0x2, 0x7D0)
        OP_48()
        Jump("loc_7A5")

    QueueWorkItem2(0x8, 1, lambda_7A5)
    Sleep(200)

    ChrTalk(    #22
        0x8,
        "#102F#5PAAAAAARRRRGGGGGHHHH...!!\x02",
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
    SetChrFlags(0x101, 0x4)

    def lambda_835():
        OP_6D(29760, 0, 33950, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_835)

    def lambda_84D():
        OP_8E(0xFE, 0x7468, 0x0, 0x846C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_84D)
    Sleep(800)

    def lambda_86D():
        OP_8E(0xFE, 0x797C, 0x0, 0x84D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_86D)
    Sleep(200)

    def lambda_88D():
        OP_8E(0xFE, 0x78B4, 0x0, 0x891C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88D)
    WaitChrThread(0x101, 0x1)
    ClearChrFlags(0x101, 0x4)

    def lambda_8B2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B2)
    WaitChrThread(0x107, 0x1)

    def lambda_8C5():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_8C5)
    WaitChrThread(0x102, 0x1)

    def lambda_8D8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D8)
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

    def lambda_971():

        label("loc_971")

        OP_99(0xFE, 0x0, 0x2, 0xBB8)
        OP_48()
        Jump("loc_971")

    QueueWorkItem2(0x8, 1, lambda_971)

    ChrTalk(    #26
        0x8,
        "#102F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#002FUm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_44(0x8, 0xFF)
    SetChrSubChip(0x8, 0)
    OP_9E(0x8, 0x32, 0x0, 0x3E8, 0x1770)
    OP_63(0x8)
    SetChrSubChip(0x8, 3)

    ChrTalk(    #28
        0x8,
        "#103F#5S#5PGOT IT!!!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x12C, 0xFA0)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #29
        0x101,
        "#004FEek!\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0x1E, 0x0, 0x1F4, 0x1770)

    ChrTalk(    #30
        0x8,
        (
            "#101F#5PAh ha ha! I did it!\x01",
            "It's finally complete!\x02\x03",

            "That's right! Who's the man?\x01",
            "I'm the man!\x02\x03",

            "Yes, I should start testing\x01",
            "it at once!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ADD():

        label("loc_ADD")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_ADD")

    QueueWorkItem2(0x102, 1, lambda_ADD)

    def lambda_AEE():

        label("loc_AEE")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_AEE")

    QueueWorkItem2(0x107, 1, lambda_AEE)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrChipByIndex(0x8, 0)
    OP_8C(0x8, 90, 0)
    OP_96(0x8, 0x70A8, 0x0, 0x7CCE, 0x1F4, 0x1770)

    def lambda_B2C():
        OP_6D(29900, 0, 34680, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B2C)

    def lambda_B44():
        OP_8E(0xFE, 0x7486, 0x0, 0x90BA, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B44)
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

    def lambda_BA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_BA3)
    OP_8E(0x8, 0x63B0, 0xFFFFF6A0, 0x8778, 0x1F40, 0x0)
    OP_44(0x102, 0xFF)
    OP_44(0x107, 0xFF)
    SetChrPos(0x8, 30000, -1000, 8900, 270)

    def lambda_BE2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BE2)
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
        "#562FI'm so embarrassed...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x510)
    EventEnd(0x0)
    Return()

    # Function_5_644 end

    def Function_6_D9D(): pass

    label("Function_6_D9D")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0x7D, 0x0, 0x64)
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

    # Function_6_D9D end

    def Function_7_E67(): pass

    label("Function_7_E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A8F")
    EventBegin(0x0)
    SetMapFlags(0x10000000)
    Fade(1000)
    OP_4A(0x8, 255)
    OP_6D(32000, -1000, 10100, 0)
    SetChrPos(0x107, 31500, -1000, 200, 0)
    SetChrPos(0x101, 30600, -1000, -800, 0)
    SetChrPos(0x102, 31800, -1000, -1000, 0)
    OP_0D()

    def lambda_ECE():

        label("loc_ECE")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_ECE")

    QueueWorkItem2(0x101, 1, lambda_ECE)

    def lambda_EDF():

        label("loc_EDF")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EDF")

    QueueWorkItem2(0x102, 1, lambda_EDF)

    def lambda_EF0():

        label("loc_EF0")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EF0")

    QueueWorkItem2(0x107, 1, lambda_EF0)

    def lambda_F01():
        OP_8E(0xFE, 0x7A44, 0xFFFFFC18, 0x1DB0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_F01)
    Sleep(100)

    def lambda_F21():
        OP_8E(0xFE, 0x7788, 0xFFFFFC18, 0x1838, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F21)
    Sleep(100)

    def lambda_F41():
        OP_8E(0xFE, 0x7C38, 0xFFFFFC18, 0x189C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F41)
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
    SetChrFlags(0x8, 0x4)

    def lambda_11CC():
        OP_6D(32910, -1000, 8880, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11CC)

    def lambda_11E4():
        OP_8E(0xFE, 0x7EFD, 0xFFFFFC18, 0x2936, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11E4)
    Sleep(300)

    def lambda_1204():
        OP_8E(0xFE, 0x8692, 0xFFFFFC18, 0x2102, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1204)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 90, 400)
    WaitChrThread(0x8, 0x2)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #45
        (
            "\x07\x05Professor Russell and Tita began working with some complex-looking\x01",
            "equipment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    LoadEffect(0x0, "map\\\\mp029_00.eff")
    LoadEffect(0x1, "map\\\\mp029_01.eff")
    LoadEffect(0x2, "map\\\\mp029_02.eff")
    PlayEffect(0x1, 0x4, 0xFF, 31600, -500, 11150, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, 33570, -400, 9620, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #46
        0x101,
        "#509FHey, now...\x02",
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
    TurnDirection(0x8, 0x102, 800)

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

    def lambda_14FB():

        label("loc_14FB")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_14FB")

    QueueWorkItem2(0x101, 1, lambda_14FB)
    OP_8C(0x102, 180, 600)
    OP_43(0x102, 0x1, 0x0, 0x9)
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
        "#509F#2PA-Antenna...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 800)

    ChrTalk(    #55
        0x101,
        "#005F#2POh, no, you didn't!\x02",
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
            "#009F#2PWhy should I have to\x01",
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
            "#509F#2PYou're not hearing a word\x01",
            "I say...\x02\x03",

            "#007F*sigh*\x01",
            "Fine. Whatever!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 800)
    OP_8E(0x101, 0x797C, 0xFFFFFC18, 0x3E8, 0x1770, 0x0)

    def lambda_16E0():
        OP_8E(0xFE, 0x51A4, 0x0, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16E0)
    OP_6D(34600, -1000, 10700, 2000)
    OP_22(0x9E, 0x1, 0x64)
    Sleep(200)
    PlayEffect(0x1, 0x0, 0xFF, 35680, 750, 10480, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0x1, 0xFF, 35820, 750, 9630, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0x2, 0xFF, 35390, 930, 7320, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x1, 0x3, 0xFF, 35360, 930, 6080, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(600)

    ChrTalk(    #60
        0x107,
        "#061F#2P...Yep, perfect! ♪\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 315, 400)

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

            "Murdock sent along some fresh\x01",
            "faces, then, I presume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x107,
        "#562F#2PG-Grandpa...\x02",
    )

    CloseMessageWindow()
    OP_23(0x9E)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)

    AnonymousTalk(    #67
        (
            "\x07\x05And so, Estelle and Joshua inadvertently wound up as assistants in the\x01",
            "experiment.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #68
        (
            "\x07\x05After many small (but relatively harmless) explosions and some singeing of\x01",
            "the eyebrows, the day gave way to evening...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FD)
    NewScene("ED6_DT01/T3133   ._SN", 100, 0, 1)
    IdleLoop()

    label("loc_1A8F")

    Return()

    # Function_7_E67 end

    def Function_8_1A90(): pass

    label("Function_8_1A90")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x4)
    SetChrFlags(0x1, 0x4)
    SetChrFlags(0x2, 0x4)
    OP_6D(-300, 0, 2200, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_44(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 300, 0, 500, 270)
    SetChrPos(0x107, 300, 200, 1700, 270)
    SetChrPos(0x101, -2300, 200, 500, 90)
    SetChrPos(0x102, -2300, 200, 1700, 90)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x102, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 4)
    SetChrChipByIndex(0x107, 5)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrSubChip(0x102, 2)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #69
        0x8,
        (
            "#101F#4PHa ha ha!\x01",
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
            "#509FGrr...\x01",
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
            "#103F#4PWell, now. You're a bright lad,\x01",
            "then, aren't you?\x02\x03",

            "#101FWant to give up this bracer \x01",
            "nonsense and start up in the\x01",
            "field of orbal engineering?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 1)

    ChrTalk(    #73
        0x107,
        (
            "#063FGrandpa!\x02\x03",

            "#562FI'm really sorry, guys...\x02\x03",

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
            "#101F#4PHa ha ha!\x01",
            "Please, you're too kind.\x02\x03",

            "#100FMoving on! So I'm being paid a\x01",
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
            "#100F#4PYes, from way back when.\x02\x03",

            "I've known him since his army\x01",
            "days, some 20 years or so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x107,
        (
            "#061FI've met him, too.\x02\x03",

            "He had the really nice\x01",
            "mustache, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#007FWeeeell... I don't know if I'd call it 'nice,'\x01",
            "so much as 'suspicious-looking.'\x02\x03",

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
            "#103F#4PWhat are you talking about?\x02\x03",

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
            "\x07\x05Estelle explained to the professor the whole sequence of events surrounding\x01",
            "the black orbment.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3F(0x35B, 1)
    Fade(500)
    OP_22(0x82, 0x0, 0x64)
    SetChrPos(0xA, -900, 800, 270, 0)
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
        "#103F#4P...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x107,
        "#064FWow... A pitch-black orbment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#102F#4PYes. Most intriguing.\x02\x03",

            "And with no inscribed caliber\x01",
            "or seams...\x02\x03",

            "Look at that frame, too...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #88
        "\x07\x05Professor Russell produced a cutting tool from his belt.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "\x07\x05Without a word, he pushed the blade's edge against the outer shell of the\x01",
            "orbment.\x02",
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
            "#102F#4P...\x02\x03",

            "#104FJust as I thought...\x02\x03",

            "#100FHere, take a look.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        "#002FO-Okay...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #94
        "\x07\x05Estelle, Joshua and Tita peered intently at the black orbment.\x02",
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
        "#064FThere's not even a scratch...\x02",
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
            "#102F#4PThe frame is made from some\x01",
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
        "#505FTh-That's just crazy...\x02",
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
            "#104F#4PWell, I can certainly spend\x01",
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
            "#060FThat huge piece of equipment\x01",
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
            "#506F...You're making my head hurt with\x01",
            "your techno-babble. Just tell me\x01",
            "what using that thing'll accomplish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "#102F#4PTo put it in layman's terms, it'll allow us to\x01",
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
            "#012FAnd that should give us a\x01",
            "major clue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x8,
        (
            "#102F#4PIndeed.\x02\x03",

            "#101FSo, without further ado...\x02",
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
        "#103F#4PSure.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 0)

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
        "#001FSounds great to me! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        "#019FWe'll even help with prep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "#101F#4PAll right. Come on, then.\x02\x03",

            "I've got a bit to do while\x01",
            "lunch is prepared.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x107, 1)

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
        "#102F#4PMy house, my rules!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x101,
        "#007F(What is UP with these two...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        "#010F(Now I see where she gets it...)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3172   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1A90 end

    def Function_9_2BFF(): pass

    label("Function_9_2BFF")

    OP_8E(0xFE, 0x7850, 0xFFFFFC18, 0x1CC, 0x1388, 0x0)
    OP_8E(0xFE, 0x5B90, 0x0, 0xBE, 0x1388, 0x0)
    OP_44(0x101, 0xFF)
    OP_8E(0xFE, 0x5A3C, 0x7D0, 0x22F6, 0x1388, 0x0)

    def lambda_2C45():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C45)
    OP_8E(0xFE, 0x659A, 0xFA0, 0x23A0, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_9_2BFF end

    def Function_10_2C6B(): pass

    label("Function_10_2C6B")

    OP_A6(0x1)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    OP_A3(0x1)
    Return()

    # Function_10_2C6B end

    def Function_11_2C7D(): pass

    label("Function_11_2C7D")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(34700, -1000, 10700, 0)
    SetChrPos(0x8, 34400, -1000, 8900, 0)
    SetChrPos(0x107, 32299, -1000, 10400, 0)
    SetChrPos(0x101, 32299, -1000, 8400, 45)
    SetChrPos(0x102, 32800, -1000, 7400, 45)

    ChrTalk(    #118
        0x101,
        "#008F夜のラッセル工房映す予定（※仮）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "#100Fコホン……\x02\x03",

            "腹もふくれたことじゃし、\x01",
            "さっそく始めるとしようかの。\x02\x03",

            "それでは、エステル。\x01",
            "例のオーブメントを台の上へ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#000Fう、うん……\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x8084, 0xFFFFFC18, 0x283C, 0x7D0, 0x0)
    OP_8C(0x101, 90, 400)
    Sleep(1000)

    ChrTalk(    #121
        0x101,
        "#000Fこれでいいの？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        "#100Fうむ、ごくろう。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "#100Fティータや。\x01",
            "そちらの用意はどうじゃ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x107,
        "#060Fうん、バッチリだよー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x8,
        (
            "#100Fよろしい。\x02\x03",

            "それでは《黒の導力器》の\x01",
            "導力波測定実験を開始する。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        "#010F《黒の導力器（オーブメント）》？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#000Fなんか、\x01",
            "まんまなネーミングねぇ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x8,
        (
            "#100Fシンプル・イズ・ベストじゃ。\x02\x03",

            "とりあえず\x01",
            "名前がないのは不便じゃからの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x107,
        "#060Fドキドキ、ワクワク……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#000Fあー、この子はこの子で\x01",
            "すっかりやる気満々だし。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x107,
        "#060Fあ……てへへ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        (
            "#100Fよし、それでは始めるぞ。\x02\x03",

            "ティータ。\x01",
            "装置の起動を頼む。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        "#060Fうんっ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        "#100F出力を４５％に固定……各種測定器のスタンバイ開始。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x107,
        (
            "#060F了解……\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x107,
        (
            "#060Fうんっ。\x01",
            "各種測定器、準備完了だよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x8,
        (
            "#100Fさーて、ここからが本番じゃ。\x02\x03",

            "入出力が見当たらない以上、\x01",
            "中の結晶回路に導力波をぶつけて\x01",
            "反応を探るしかないわけじゃが……\x02\x03",

            "そこで、この測定装置の\x01",
            "真価が発揮されるというわけじゃ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#000Fノ、ノリノリねぇ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        "#100Fポチっとな。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#000Fま、まぶし……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x102,
        (
            "#010Fなるほど、ああやって\x01",
            "結晶回路に負荷をかけるのか……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x8,
        (
            "#100Fよしよし……\x02\x03",

            "ティータや。\x01",
            "測定器の反応はどうじゃ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x107,
        (
            "#060Fう、うん……\x02\x03",

            "なんだか、ヘンかも……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        "#100Fなぬ？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x107,
        (
            "#060Fタコメーターの針が\x01",
            "ぶるぶる震えちゃって……\x02\x03",

            "あっ……\x02\x03",

            "ぐ、ぐるぐる回り始めたよ！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x8,
        "#100Fなんじゃと！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x107,
        "#060Fきゃあっ！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        "#100Fな、なんじゃこれは！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#000Fヨシュア、これ……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        "#010Fあの時の黒い光……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        "#100Fなんじゃと！？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3106   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2C7D end

    def Function_12_336E(): pass

    label("Function_12_336E")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(34700, -1000, 10700, 0)
    SetChrPos(0x8, 34400, -1000, 8900, 0)
    SetChrPos(0x107, 32299, -1000, 10400, 0)
    SetChrPos(0x101, 23400, 0, 100, 0)
    SetChrPos(0x102, 23400, 0, 100, 0)

    ChrTalk(    #152
        0x101,
        (
            "#005F夜のラッセル工房を起点に、\x01",
            "次々と照明が消えていく。（※仮）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x107,
        (
            "#060Fお、おじいちゃん、\x01",
            "これ以上はダメだよぉ！\x02\x03",

            "測定装置を止めなくっちゃ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "#100Fええい、止めてくれるな！\x02\x03",

            "あと少しで何かが掴めそう……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x765C, 0xFFFFFC18, 0x384, 0x32C8, 0x0)
    OP_8E(0x101, 0x8278, 0xFFFFFC18, 0x1900, 0x2710, 0x0)

    ChrTalk(    #155
        0x101,
        (
            "#000Fちょ、ちょっと！\x01",
            "町中の照明が消えてるわよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 800)

    ChrTalk(    #156
        0x107,
        "#060Fふえっ！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 800)

    ChrTalk(    #157
        0x8,
        (
            "#100Fなんと……\x02\x03",

            "ええい、仕方ない！\x01",
            "これにて実験終了じゃああっ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_356E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_356E)
    OP_8C(0x8, 0, 400)

    ChrTalk(    #158
        0x101,
        (
            "#000Fあ……\x02\x03",

            "も、元に戻った……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x107,
        "#060Fはうううう～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#100F計器の方は……\x02\x03",

            "ダメじゃ、何も記録しておらん。\x02\x03",

            "ということは、生きていたのは\x01",
            "《黒の導力器》が乗った本体のみ。\x02\x03",

            "あとは根こそぎということか……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_365B():
        OP_6D(33400, -1000, 10200, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_365B)
    OP_8E(0x102, 0x765C, 0xFFFFFC18, 0x384, 0x32C8, 0x0)
    OP_8E(0x102, 0x7A44, 0xFFFFFC18, 0x12C0, 0x1770, 0x0)

    ChrTalk(    #161
        0x102,
        (
            "#010Fよかった……\x01",
            "実験を中止したみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36CD():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36CD)

    def lambda_36DB():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_36DB)

    def lambda_36E9():

        label("loc_36E9")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_36E9")

    QueueWorkItem2(0x101, 1, lambda_36E9)

    ChrTalk(    #162
        0x101,
        (
            "#000Fあ、ヨシュア！\x01",
            "外の様子はどうなの？\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x7B0C, 0xFFFFFC18, 0x17D4, 0xBB8, 0x0)

    ChrTalk(    #163
        0x102,
        (
            "#010Fうん……\x01",
            "照明は元通りになったみたいだ。\x02\x03",

            "まだ騒ぎは収まっていないけどね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#000Fそっか……\x02\x03",

            "でも、一体全体、\x01",
            "何が起こっちゃったってわけ？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x8,
        (
            "#100Fそうじゃな……\x02\x03",

            "あえて表現するならば\x01",
            "『導力停止現象』と言うべきか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#000F導力停止現象……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        (
            "#010Fオーブメント内を走る導力が\x01",
            "働かなくなったということですね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x107,
        (
            "#060Fやっぱり《黒の導力器》が\x01",
            "原因なのかな……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x8,
        (
            "#100Fうむ、間違いあるまい。\x02\x03",

            "しかし、これほど広範囲の\x01",
            "オーブメントを停止させるとは。\x02\x03",

            "むむむむむむむむむ……\x01",
            "こいつは予想以上の代物じゃぞ。\x02\x03",

            "面白い、すこぶる面白いわい！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#000Fお、面白がってる場合じゃ\x01",
            "ないと思うんですけど～……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 23400, 0, 100, 0)

    NpcTalk(    #171
        0x9,
        "男性の声",
        "ハ～カ～セ～ッ！！\x02",
    )

    CloseMessageWindow()

    def lambda_39DD():

        label("loc_39DD")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_39DD")

    QueueWorkItem2(0x101, 1, lambda_39DD)

    def lambda_39EE():

        label("loc_39EE")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_39EE")

    QueueWorkItem2(0x107, 1, lambda_39EE)

    def lambda_39FF():

        label("loc_39FF")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_39FF")

    QueueWorkItem2(0x102, 1, lambda_39FF)

    def lambda_3A10():

        label("loc_3A10")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3A10")

    QueueWorkItem2(0x8, 1, lambda_3A10)
    OP_8E(0x9, 0x765C, 0xFFFFFC18, 0x384, 0x1770, 0x0)
    OP_8E(0x9, 0x7724, 0xFFFFFC18, 0x1C20, 0x1770, 0x0)
    OP_8E(0x9, 0x7F58, 0xFFFFFC18, 0x1E78, 0x1770, 0x0)
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(    #172
        0x8,
        (
            "#100Fおお、マードック。\x01",
            "いいところに来たじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x9,
        (
            "#800Fいいところ、じゃありません！\x02\x03",

            "毎回毎回、新発明のたびに\x01",
            "とんでもない騒ぎを起こして！\x02\x03",

            "町中の照明を消すなんて\x01",
            "今度は何をやったんですかッ！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B33():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B33)

    def lambda_3B41():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3B41)

    def lambda_3B4F():

        label("loc_3B4F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3B4F")

    QueueWorkItem2(0x102, 1, lambda_3B4F)

    ChrTalk(    #174
        0x8,
        (
            "#100F失敬な。\x01",
            "今回はわしは無関係じゃぞ。\x02\x03",

            "そこに置いてある\x01",
            "《黒の導力器》の仕業じゃ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BBB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BBB)

    def lambda_3BC9():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3BC9)

    def lambda_3BD7():

        label("loc_3BD7")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3BD7")

    QueueWorkItem2(0x102, 1, lambda_3BD7)

    ChrTalk(    #175
        0x9,
        (
            "#800Fそ、それは例の……\x02\x03",

            "なるほど、それが原因なら\x01",
            "この異常事態もうなずける……\x02\x03",

            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "#800Fだ、だからといってアンタが\x01",
            "無関係ということがあるかあっ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C98():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C98)

    def lambda_3CA6():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3CA6)

    def lambda_3CB4():

        label("loc_3CB4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3CB4")

    QueueWorkItem2(0x102, 1, lambda_3CB4)

    ChrTalk(    #177
        0x8,
        "#100Fちっ、バレたか……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#000Fなんかやたらと\x01",
            "息が合ってるわね～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        "#010Fいつもあんな感じなんだ？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x107,
        "#060Fあう……恥ずかしながら……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #181
        (
            "\x07\x05こうしてツァイス地方での\x01",
            "最初の日は慌だしく過ぎていった。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #182
        (
            "\x07\x05エステルとヨシュアは、夜も遅いため\x01",
            "ラッセル工房に泊めてもらうことにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x511)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_336E end

    def Function_13_3DFD(): pass

    label("Function_13_3DFD")

    EventBegin(0x0)
    OP_6D(-2860, 0, 35210, 0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -2950, 0, 35300, 225)
    SetChrPos(0x101, -4360, 0, 33690, 45)
    SetChrPos(0x107, -5900, -2000, 39200, 0)
    SetChrFlags(0x107, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #183
        0x101,
        (
            "#006F#5PMan... Yesterday was such\x01",
            "a crazy day.\x02\x03",

            "I was surprised enough at the town,\x01",
            "but I really wasn't expecting to\x01",
            "deal with anything like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x102,
        (
            "#019F#6PHa ha. No kidding.\x02\x03",

            "#013FBut back on the subject\x01",
            "of the black orbment...\x02\x03",

            "It's much more powerful than\x01",
            "I'd ever imagined possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#002F#5PYeah...\x02\x03",

            "What's the prof gonna do,\x01",
            "now that his equipment's\x01",
            "gone all kerflooey?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x107,
        "#2PGood morning, guys!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x107, 400)
    ClearChrFlags(0x107, 0x80)

    def lambda_400A():

        label("loc_400A")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_400A")

    QueueWorkItem2(0x101, 1, lambda_400A)

    def lambda_401B():

        label("loc_401B")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_401B")

    QueueWorkItem2(0x102, 1, lambda_401B)

    def lambda_402C():
        OP_6D(-2280, 0, 36270, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_402C)
    OP_8E(0x107, 0xFFFFF8F8, 0x0, 0x9858, 0xBB8, 0x0)
    OP_8E(0x107, 0xFFFFF736, 0x0, 0x9042, 0x7D0, 0x0)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #187
        0x101,
        "#501F#2PMorning, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x102,
        (
            "#019F#4PGood morning...\x01",
            "Quite a big day yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x107,
        (
            "#067FHee hee, no kidding!\x02\x03",

            "#560FDid you guys sleep okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#001F#2PYep, like babies. ㈱\x02\x03",

            "#000FIs the professor already up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x107,
        (
            "#060FOh, he left for the central\x01",
            "factory early this morning.\x02\x03",

            "#061FHe said something about how he was going to\x01",
            "expose all the Black Orbment's secrets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#505F#2PWow. Looks like getting roared at over and\x01",
            "over by the factory chief yesterday didn't\x01",
            "even put a dent in him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x102,
        (
            "#015F#4PWe really appreciate both of you taking the\x01",
            "time just to look over something a couple\x01",
            "of relative strangers brought you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x107,
        (
            "#067FOh, it's fine, really.\x02\x03",

            "Grandpa's investigating it out of pure\x01",
            "curiosity more than anything.\x02\x03",

            "#560FI should go to the factory myself,\x01",
            "once I'm done with breakfast.\x02\x03",

            "What do you plan to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#006F#2PNaturally, we'll be coming with you!\x02\x03",

            "I wanna know what's really going on with that\x01",
            "orbment, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        (
            "#010F#4PMaybe there's something\x01",
            "we can do to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x107,
        (
            "#061FYay! Then you can come\x01",
            "with me!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #198
        0x107,
        (
            "#065FUh-oh! I almost forgot about\x01",
            "the soup!\x02\x03",

            "#067FJust a second, you two! I'll bring\x01",
            "you breakfast as soon as I make sure\x01",
            "it's edible, and not on fire!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x107, 0xFFFFF8F8, 0x0, 0x9858, 0x1388, 0x0)
    OP_8E(0x107, 0xFFFFE8F4, 0xFFFFF830, 0x9920, 0x1388, 0x0)
    SetChrFlags(0x107, 0x80)
    OP_6D(-2860, 0, 35210, 1000)
    OP_63(0x101)

    ChrTalk(    #199
        0x101,
        (
            "#008F#2PI guess that's what that smell is...\x01",
            "but man, what a cutie! I wish we could\x01",
            "take her back with us to Rolent.\x02\x03",

            "She could be like a pet, cheering\x01",
            "us up whenever we're feeling down!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #200
        0x102,
        "#018F#6PThat's...kind of creepy, Estelle.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_3DFD end

    def Function_14_46B0(): pass

    label("Function_14_46B0")

    ClearMapFlags(0x10000000)
    EventBegin(0x0)
    OP_6D(-1580, 0, -710, 0)
    SetChrPos(0x107, -1130, 0, -1640, 0)
    SetChrPos(0x102, -2660, 0, -2900, 0)
    SetChrPos(0x101, -2530, 0, -1500, 0)
    SetChrPos(0x106, -1330, 0, -3040, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #201
        0x101,
        (
            "#006F#6PNow...where is that thing?\x02\x03",

            "It's gotta be here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4763():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4763)

    def lambda_4771():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4771)

    def lambda_477F():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_477F)
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #202
        0x107,
        (
            "#560F#4PUmm...maybe in a corner\x01",
            "of the lab or the second\x01",
            "floor archives?\x02\x03",

            "Those are where Grandpa\x01",
            "usually tosses stuff from\x01",
            "his old inventions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x106,
        (
            "#051FEccentric old coot...\x02\x03",

            "But whatever. Let's just\x01",
            "find the damn thing.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x43, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_14_46B0 end

    def Function_15_487B(): pass

    label("Function_15_487B")

    EventBegin(0x0)
    OP_A2(0x55F)
    OP_28(0x43, 0x1, 0x100)

    ChrTalk(    #204
        0x101,
        "#006FFound it! ♪\x02",
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
            "#560FI think so.\x02\x03",

            "If everything performs to specs,\x01",
            "then it'll keep a biosensor from\x01",
            "working right.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xB, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #207
        "\x07\x00Found \x07\x02Detector Jammer\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x362, 1)

    ChrTalk(    #208
        0x106,
        (
            "#051FAll right. Back to the guild, then.\x02\x03",

            "Kilika's probably finished collecting\x01",
            "intel on Fort Leiston by now.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x0, 0x1)
    EventEnd(0x1)
    Return()

    # Function_15_487B end

    SaveToFile()

Try(main)
