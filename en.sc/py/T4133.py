from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4133   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4133.x',
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
        'Fritz',                                # 9
        'Tita',                                 # 10
        'Renne',                                # 11
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT27/CH03510 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT27/CH03510P._CP',             # 02
    )

    DeclNpc(
        X                   = 7410,
        Z                   = 0,
        Y                   = 3300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 7200,
        TriggerZ            = 0,
        TriggerY            = 1690,
        TriggerRange        = 800,
        ActorX              = 7410,
        ActorZ              = 1500,
        ActorY              = 3300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7000,
        TriggerZ            = 0,
        TriggerY            = 4890,
        TriggerRange        = 800,
        ActorX              = 7000,
        ActorZ              = 1000,
        ActorY              = 4890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_17E",          # 01, 1
        "Function_2_17F",          # 02, 2
        "Function_3_2FC",          # 03, 3
        "Function_4_301",          # 04, 4
        "Function_5_31C",          # 05, 5
        "Function_6_1CFD",         # 06, 6
        "Function_7_1D95",         # 07, 7
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_17D")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_17D")

    Return()

    # Function_0_16A end

    def Function_1_17E(): pass

    label("Function_1_17E")

    Return()

    # Function_1_17E end

    def Function_2_17F(): pass

    label("Function_2_17F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2E6")

    label("loc_1A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BD")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2E6")

    label("loc_1BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2E6")

    label("loc_1D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2E6")

    label("loc_1EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_208")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2E6")

    label("loc_208")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2E6")

    label("loc_221")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2E6")

    label("loc_23A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2E6")

    label("loc_253")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2E6")

    label("loc_26C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2E6")

    label("loc_285")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2E6")

    label("loc_29E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2E6")

    label("loc_2B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D0")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2E6")

    label("loc_2D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2E6")

    label("loc_2FB")

    Return()

    # Function_2_17F end

    def Function_3_2FC(): pass

    label("Function_3_2FC")

    Call(0, 4)
    Return()

    # Function_3_2FC end

    def Function_4_301(): pass

    label("Function_4_301")

    TalkBegin(0x8)

    ChrTalk(    #0
        0x8,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_4_301 end

    def Function_5_31C(): pass

    label("Function_5_31C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32F")
    Call(0, 6)

    label("loc_32F")

    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x101, 6950, 0, 1690, 0)
    SetChrPos(0xF7, 8109, 0, 1700, 0)
    SetChrPos(0xA, 7130, 0, 450, 0)
    SetChrPos(0x9, 8039, 0, 590, 0)
    OP_6D(7310, 0, 2300, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(309000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #1
        0x8,
        (
            "Pardon, are you the bracers and\x01",
            "company we are expecting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Forgive me, but we were unable to\x01",
            "secure a four-person room for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Would you be willing to accept a pair\x01",
            "of two-person rooms?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_542")

    ChrTalk(    #4
        0x101,
        "#1004F#6POh, sure.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #5
        0x101,
        (
            "#1015F#6PHow do you want to split\x01",
            "them up, Agate?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #6
        0x106,
        (
            "#051F#4PAh, I don't care too much.\x02\x03",

            "Set it up however you want.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F0")

    label("loc_542")


    ChrTalk(    #7
        0x101,
        "#1004F#6POh, sure.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(500)

    ChrTalk(    #8
        0x101,
        (
            "#1015F#6PHow do you want to split\x01",
            "them up, Schera?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #9
        0x103,
        (
            "#027F#4PI'm fine with any arrangement.\x02\x03",

            "Set it up however you please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F0")


    ChrTalk(    #10
        0xA,
        (
            "#265F#6PI want to be with Miss Estelle!\x02\x03",

            "You've been busy with work,\x01",
            "so we haven't had any time to\x01",
            "talk at all.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_66B():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_66B)

    def lambda_679():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_679)
    TurnDirection(0x101, 0xA, 400)
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(    #11
        0x9,
        (
            "#065F#2PNo fair, Renne!\x02\x03",

            "I wanted to be with Estelle, too...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x9, 400)

    ChrTalk(    #12
        0xA,
        (
            "#263F#1PThen you should've said so sooner,\x01",
            "slowpoke!\x02\x03",

            "#260FI know! What if all three of us stayed\x01",
            "in the same room? We could share a\x01",
            "bed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "#061F#2PN-No, that's okay, ahaha...\x02\x03",

            "I'll let you borrow Estelle for tonight,\x01",
            "Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        "#261F#1PHeehee! Thank you, Tita!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1016F#6PUm... I think I just got horse-traded.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8FF")

    ChrTalk(    #16
        0x106,
        (
            "#051F#4PThen I'll be with you, kiddo.\x02\x03",

            "Hah, this reminds me of when we\x01",
            "were hiding out with Gramps.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #17
        0x9,
        (
            "#560F#5PNow that you mention it...\x02\x03",

            "#067FYeah, it does!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CF")

    label("loc_8FF")


    ChrTalk(    #18
        0x103,
        (
            "#021F#4PYou do have a way with the ladies,\x01",
            "Estelle.\x02\x03",

            "#027FWell, that leaves the two of us, Tita.\x02\x03",

            "How about I show you a few tarot card\x01",
            "games before we settle in for the night?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #19
        0x9,
        "#061F#5POkay!\x02",
    )

    CloseMessageWindow()

    label("loc_9CF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x101, 35000, 0, 106370, 0)
    SetChrPos(0xA, 35000, 0, 106370, 0)
    OP_6D(35000, 0, 113130, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(239, 0)
    OP_6B(1890, 0)
    OP_6C(315000, 0)
    OP_6E(437, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0xA, 0x80)

    def lambda_A9D():
        OP_6D(34540, 0, 115470, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_A9D)

    def lambda_AB5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_AB5)

    def lambda_AC7():
        OP_8E(0xFE, 0x8674, 0x0, 0x1BD5A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AC7)
    Sleep(600)
    ClearChrFlags(0x101, 0x80)

    def lambda_AEC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AEC)

    def lambda_AFE():
        OP_8E(0xFE, 0x8BBA, 0x0, 0x1BDAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFE)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #20
        0xA,
        (
            "#265F#6POh, wow! This room isn't like the\x01",
            "one I stayed in with Papa and Mama!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 45, 400)
    Sleep(500)
    OP_8C(0xA, 0, 400)
    OP_8C(0xA, 270, 400)
    Sleep(500)
    OP_8C(0xA, 0, 400)

    ChrTalk(    #21
        0xA,
        (
            "#261F#6PThere's a big building outside the\x01",
            "window!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1026F#5POh...\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400C2, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1500)
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #23
        0xA,
        "#264F#6PMiss Estelle? What's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #24
        0x101,
        (
            "#1016F#2PEr, nothing, really.\x02\x03",

            "#1025FMore importantly... I'm sorry, Renne.\x02\x03",

            "We couldn't find your papa or mama\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        (
            "#260F#6PIt's okay.\x02\x03",

            "Papa and Mama promised they'd\x01",
            "come get me.\x02\x03",

            "You don't need to search so hard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1026F#2PBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#263F#6PPapa and Mama are veeery\x01",
            "good at hide and seek.\x02\x03",

            "Not as good as me, of course!\x01",
            "But still good.\x02\x03",

            "So I don't think you'll find them\x01",
            "very easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1016F#2PHaha. Is that right?\x02\x03",

            "#1006FWell, I won't try so hard to find them,\x01",
            "but only if you're okay with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "#261F#6PYeah, it's okay! It's for the best.\x02\x03",

            "#260FBut never mind that right now.\x01",
            "I have two big favors to ask of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1004F#2POh? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "#1306F#6PAh-ah-ahh!\x02\x03",

            "I can't tell you unless you promise\x01",
            "to do them ahead of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016F#2PYikes... Did your papa teach you to\x01",
            "drive a bargain like that?\x02\x03",

            "#1006FOkay, sure. If it's something I can do,\x01",
            "I promise I will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#261F#6PReally? Yay!\x02\x03",

            "#260FThe first thing is...\x01",
            "Can I call you 'Estelle' from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1015F#2PHuh? Call me...?\x02\x03",

            "#1004FOh! You mean drop the whole 'Miss'\x01",
            "part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "#260F#6PYeah!\x02\x03",

            "#266FTita gets to call you Estelle all\x01",
            "the time, so I don't wanna have\x01",
            "to call you 'Miss Estelle'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1016F#2PAhaha... Is that right?\x02\x03",

            "#1011FAll right, I don't mind.\x02\x03",

            "I never stood that much on formality,\x01",
            "anyway. And it's not like I'm your teacher\x01",
            "or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        (
            "#264F#6PSo you really don't mind?\x02\x03",

            "#267FEstelle... Estelle...\x02\x03",

            "#261FOh, I love it! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1016F#2PHaha, glad you like it.\x02\x03",

            "#1006FCall me Estelle as much as you\x01",
            "want, Renne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xA,
        (
            "#265F#6POkay, Estelle!\x02\x03",

            "#261FHeehee... That makes me happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1017F#2PD'aww. That's good.\x02\x03",

            "So what was the other thing, Renne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "#267F#6POh, yeah! Well...\x02\x03",

            "Can you tell me why you were\x01",
            "so surprised when we came in\x01",
            "the room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1026F#2PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#268F#6PYou had this really sad, lonely look\x01",
            "on your face.\x02\x03",

            "I wanna know why. Is that okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1003F#2P...Yeah, it's okay.\x02\x03",

            "#1025FSee, I've actually stayed in this very\x01",
            "room before, with someone else.\x02\x03",

            "Stepping in here just reminded me\x01",
            "of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#265F#6PReally?! Was it your looover?\x01",
            "Was this your love nest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1017F#2PHa...haha... Ah, not quite.\x02\x03",

            "He's someone I've known for a really\x01",
            "long time, and we've gotten very close,\x01",
            "but...well, it's complicated.\x02\x03",

            "We're not together right now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "#264F#6POoooh!\x02\x03",

            "#265FWell, what kind of man is he? Huh?\x02\x03",

            "What's his name? What does he\x01",
            "look like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1025F#2PYikes, questions... His name is Joshua.\x02\x03",

            "He has black hair and amber eyes...\x01",
            "and he's pretty handsome, I guess.\x02\x03",

            "#1015FActually, you'd really call him more\x01",
            "'beautiful' than handsome, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        "#264F#6PHuh? 'Beautiful'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1016F#2PHaha, let's just say he made a\x01",
            "GREAT princess in a certain play.\x02\x03",

            "In fact, it looked amazing on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#261F#6PWow, that sounds fun!\x02\x03",

            "Can I meet him?\x02\x03",

            "When are you seeing\x01",
            "him again? Huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1025F#2PI...don't really know, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#267F#6POh...\x02\x03",

            "You don't know when you'll\x01",
            "see him again, and that's why\x01",
            "you looked sad, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1006F#2PSort of...but I'm okay.\x02\x03",

            "I'm going to find him and drag\x01",
            "him back home, even if it takes\x01",
            "years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        "#264F#6PBut why did you seem so sad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1025F#2PWell...because I'm sure Joshua's off\x01",
            "somewhere, in way over his head...\x02\x03",

            "#1003FAnd I can't do anything to help him.\x01",
            "That makes me sad, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        "#262F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1016F#2PHaha... Sorry, Renne.\x02\x03",

            "#1025FThis must be pretty boring since\x01",
            "you don't know Joshua at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#263F#6PNo way! It's neat.\x02\x03",

            "#260FJoshua was a really wonderful\x01",
            "person, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1007F#2PWonderful...? Actually, right now\x01",
            "I think he's a bit of a jerk.\x02\x03",

            "#1013FI mean, talk about selfish ways of\x01",
            "saying goodbye, taking my f-first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "#264F#6PHm? First what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1004F#2PWaaah, uh, nothing at all!\x02\x03",

            "#1016FOkay, yep, I'm all tired.\x01",
            "Time to go to sleep!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#1301F#6PHeeeeeey, no fair!\x02\x03",

            "#266FI'm not going to sleep until\x01",
            "I hear the whooole thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1015F#2PBoy, I messed that one up...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x07\x05After that, Estelle and Renne went to bed, but remained\x01",
            "awake for a little while talking about various things.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05Eventually, once she could hear nothing but Renne's\x01",
            "slow, peaceful breathing...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #67
        (
            "\x07\x05Estelle gave in to the exhaustion which had been piling\x01",
            "up on her eyelids and fell into sleep herself.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1504   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_31C end

    def Function_6_1CFD(): pass

    label("Function_6_1CFD")

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
        (0, "loc_1D76"),
        (1, "loc_1D7C"),
        (SWITCH_DEFAULT, "loc_1D82"),
    )


    label("loc_1D76")

    OP_A2(0x1200)
    Jump("loc_1D82")

    label("loc_1D7C")

    OP_A2(0x1201)
    Jump("loc_1D82")

    label("loc_1D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1D90")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1D94")

    label("loc_1D90")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1D94")

    Return()

    # Function_6_1CFD end

    def Function_7_1D95(): pass

    label("Function_7_1D95")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #68
        (
            "\x07\x05Office\x01",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_1D95 end

    SaveToFile()

Try(main)
