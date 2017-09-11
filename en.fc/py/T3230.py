from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3230   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3230.x',
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
        'Tita',                                 # 9
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
        'ED6_DT07/CH00060 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH00060P._CP',             # 00
    )

    DeclNpc(
        X                   = 160,
        Z                   = 250,
        Y                   = 8840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_130",          # 01, 1
        "Function_2_157",          # 02, 2
        "Function_3_16D",          # 03, 3
        "Function_4_260",          # 04, 4
        "Function_5_2B8",          # 05, 5
        "Function_6_97D",          # 06, 6
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_DE"),
        (SWITCH_DEFAULT, "loc_106"),
    )


    label("loc_DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE")
    Event(0, 5)

    label("loc_EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_103")

    Jump("loc_106")

    label("loc_106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F")
    SetChrPos(0x8, 160, 250, 8840, 0)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x3)

    label("loc_12F")

    Return()

    # Function_0_D2 end

    def Function_1_130(): pass

    label("Function_1_130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148")
    OP_B1("t3230_y")
    Jump("loc_151")

    label("loc_148")

    OP_B1("t3230_n")

    label("loc_151")

    OP_22(0xA1, 0x1, 0x64)
    Return()

    # Function_1_130 end

    def Function_2_157(): pass

    label("Function_2_157")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_16C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_157")

    label("loc_16C")

    Return()

    # Function_2_157 end

    def Function_3_16D(): pass

    label("Function_3_16D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25F")
    OP_8E(0xFE, 0xFFFFFABA, 0xFA, 0x1ED2, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 300)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    OP_8E(0xFE, 0xFFFFFA9C, 0xFA, 0x1A0E, 0xDAC, 0x0)
    OP_8C(0xFE, 270, 300)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)
    OP_8E(0xFE, 0x9C4, 0x0, 0x1612, 0xDAC, 0x0)
    OP_8C(0xFE, 90, 300)
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    OP_8E(0xFE, 0x226, 0xFA, 0x1946, 0xDAC, 0x0)
    OP_8E(0xFE, 0xA0, 0xFA, 0x2288, 0xDAC, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_62(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1500)
    Jump("Function_3_16D")

    label("loc_25F")

    Return()

    # Function_3_16D end

    def Function_4_260(): pass

    label("Function_4_260")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x8,
        (
            "#560FHmmhmmmhmmmmm...\x01",
            "Got my tools, got my kit...\x01",
            "Gonna fixy, fixy, fix it!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_260 end

    def Function_5_2B8(): pass

    label("Function_5_2B8")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(-1060, 250, 8880, 0)
    RemoveParty(0x6, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -150, 0, 2440, 0)
    SetChrPos(0x101, -740, 0, 1150, 0)
    SetChrPos(0x102, 500, 0, 690, 0)
    OP_4A(0x8, 255)
    FadeToBright(1000, 0)
    OP_6D(-1090, 0, 2630, 3000)

    ChrTalk(    #1
        0x101,
        (
            "#501FWow.\x01",
            "So this is the pump, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#010FYou'd never know it was so old,\x01",
            "from how well-maintained it is.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #3
        0x8,
        (
            "#067F#2PHee hee... Well, I think my grandpa\x01",
            "comes in at least once a year to\x01",
            "keep it running well.\x02\x03",

            "#060FForty years ago, people didn't\x01",
            "really know much about orbments...\x02\x03",

            "And so Grandpa created this orbal pump to show\x01",
            "people what a difference orbal technology could\x01",
            "make to their lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#006FAh, okay. So this place probably\x01",
            "has some sentimental value for\x01",
            "your grandfather, then, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#019FAnd that's why it's kept\x01",
            "in such good condition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "#061F#2PRight!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_58F():
        OP_6D(-320, 250, 8880, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_58F)

    def lambda_5A7():

        label("loc_5A7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5A7")

    QueueWorkItem2(0x101, 2, lambda_5A7)

    def lambda_5B8():

        label("loc_5B8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_5B8")

    QueueWorkItem2(0x102, 2, lambda_5B8)

    def lambda_5C9():
        OP_8E(0xFE, 0x4B0, 0xFA, 0x1E64, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C9)
    Sleep(1000)

    def lambda_5E9():
        OP_8E(0xFE, 0xFFFFFF56, 0x0, 0x1342, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E9)
    Sleep(500)

    def lambda_609():
        OP_8E(0xFE, 0x4EC, 0x0, 0x1144, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_609)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #7
        0x8,
        (
            "#064FLet's see... First up is a\x01",
            "systems check...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x262, 0xFA, 0x2274, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)

    ChrTalk(    #8
        0x8,
        (
            "#062FAnd if that's okay, then we make\x01",
            "sure there are no problems with\x01",
            "the impeller or pipes.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFFAD8, 0xFA, 0x1F18, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)

    ChrTalk(    #9
        0x101,
        (
            "#501FUmm...\x01",
            "Can we do anything to help?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #10
        0x8,
        (
            "#560FOh, it's fine. This is a\x01",
            "one-person job, anyway.\x02\x03",

            "You guys should just go\x01",
            "to the inn and relax.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    ChrTalk(    #11
        0x8,
        (
            "#064FIt might be the cavitation and\x01",
            "water hammer...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFF9F2, 0xFA, 0x18EC, 0xBB8, 0x0)
    OP_8C(0x8, 270, 400)

    ChrTalk(    #12
        0x8,
        (
            "#063F#1PHmmm...\x01",
            "What to check next...?\x02\x03",

            "#065F#1PAh-ha! It's a surging problem!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    def lambda_87E():
        OP_6D(-490, 0, 6860, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_87E)
    OP_8E(0x8, 0xA0, 0xFA, 0x2288, 0xFA0, 0x0)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #13
        0x101,
        (
            "#506FI figured we wouldn't be\x01",
            "of any use...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#010FApparently not.\x02\x03",

            "Maybe we should take her advice\x01",
            "and wait at the inn.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_4B(0x8, 255)
    OP_A2(0x51F)
    OP_28(0x40, 0x1, 0x10)
    OP_28(0x28, 0x4, 0x40)
    OP_28(0x29, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2A, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_960")
    OP_28(0x2A, 0x4, 0x40)

    label("loc_960")

    OP_28(0x2C, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_975")
    OP_28(0x31, 0x4, 0x40)

    label("loc_975")

    OP_28(0x32, 0x4, 0x40)
    EventEnd(0x0)
    Return()

    # Function_5_2B8 end

    def Function_6_97D(): pass

    label("Function_6_97D")

    EventBegin(0x0)
    OP_44(0x8, 0xFF)
    ClearMapFlags(0x1)
    OP_6D(-10, 250, 8880, 0)
    SetChrFlags(0x8, 0x80)
    AddParty(0x6, 0xFF)
    SetChrPos(0x107, 160, 250, 8840, 0)
    SetChrPos(0x101, -490, 0, 870, 0)
    SetChrPos(0x102, 670, 0, 620, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #15
        0x107,
        "#063F...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_9F7():
        OP_8E(0xFE, 0xFFFFFE02, 0x0, 0x13CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F7)
    Sleep(500)

    def lambda_A17():
        OP_8E(0xFE, 0x276, 0x0, 0x1298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A17)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x107, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x107, 400)

    ChrTalk(    #16
        0x101,
        "#501FAre you done with the repairs?\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x107, 180, 800)

    ChrTalk(    #17
        0x107,
        "#064F#4POh... Hi, guys.\x02",
    )

    CloseMessageWindow()

    def lambda_AC5():
        OP_6D(-80, 250, 7500, 1500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AC5)
    OP_8E(0x107, 0x96, 0xFA, 0x190A, 0x7D0, 0x0)
    WaitChrThread(0x107, 0x1)

    ChrTalk(    #18
        0x107,
        (
            "#067F#2PHee hee...\x01",
            "Yeah, I just finished.\x02\x03",

            "I just have to make sure that\x01",
            "the hot water's going where\x01",
            "it's supposed to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#006FIt's okay. The well in the\x01",
            "plaza has hot water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#010FSo, what was the problem?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x107,
        (
            "#560F#2PWell... The pump itself\x01",
            "wasn't the issue...\x02\x03",

            "The crankshaft on the impeller\x01",
            "had corroded and broken.\x02\x03",

            "I switched it out with a rust-\x01",
            "resistant one, so everything\x01",
            "should be fine now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#001FCool. Nice work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#019FShall we return to the inn\x01",
            "and let the hostess know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x107,
        "#061F#2POkay.\x02",
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    OP_A2(0x524)
    OP_28(0x40, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_6_97D end

    SaveToFile()

Try(main)
