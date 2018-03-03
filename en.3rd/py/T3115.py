from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3115   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3115.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Professor Russell',                    # 9
        'Erika',                                # 10
        'Prometheus',                           # 11
        'Constance',                            # 12
        'Hugo',                                 # 13
        'Igor',                                 # 14
        'Target Camera',                        # 15
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
        'ED6_DT07/CH02620 ._CH',             # 00
        'ED6_DT07/CH02623 ._CH',             # 01
        'ED6_DT07/CH01230 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
        'ED6_DT07/CH02440 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH01100 ._CH',             # 06
        'ED6_DT07/CH02020 ._CH',             # 07
        'ED6_DT07/CH01430 ._CH',             # 08
        'ED6_DT27/CH03970 ._CH',             # 09
        'ED6_DT07/CH01250 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02620P._CP',             # 00
        'ED6_DT07/CH02623P._CP',             # 01
        'ED6_DT07/CH01230P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
        'ED6_DT07/CH02440P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH01100P._CP',             # 06
        'ED6_DT07/CH02020P._CP',             # 07
        'ED6_DT07/CH01430P._CP',             # 08
        'ED6_DT27/CH03970P._CP',             # 09
        'ED6_DT07/CH01250P._CP',             # 0A
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2350,
        Z                   = 0,
        Y                   = 2800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -107400,
        Z                   = 0,
        Y                   = -90,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -103500,
        Z                   = 0,
        Y                   = 108340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -102790,
        Z                   = 0,
        Y                   = 98030,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_222",          # 01, 1
        "Function_2_226",          # 02, 2
        "Function_3_372",          # 03, 3
        "Function_4_556",          # 04, 4
        "Function_5_701",          # 05, 5
        "Function_6_877",          # 06, 6
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)

    label("loc_202")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_221")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_221")

    Return()

    # Function_0_1E2 end

    def Function_1_222(): pass

    label("Function_1_222")

    OP_82(0x80, 0x0)
    Return()

    # Function_1_222 end

    def Function_2_226(): pass

    label("Function_2_226")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_36E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2E5")

    ChrTalk(    #0
        0xFE,
        "I think I picked a bit of a bad time to come.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I was hoping to have these documents signed\x01",
            "before the factory ship departs, but fat chance\x01",
            "of that happening now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E")

    label("loc_2E5")


    ChrTalk(    #2
        0xFE,
        (
            "The factory chief seems to be out...but I have\x01",
            "no idea where he could have gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "I need him to sign these documents, too...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_36E")

    TalkEnd(0xFE)
    Return()

    # Function_2_226 end

    def Function_3_372(): pass

    label("Function_3_372")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_552")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4A9")

    ChrTalk(    #4
        0xFE,
        (
            "I've got a lazy one who's always skipping work\x01",
            "at the moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "...but young people do all the manual labor here,\x01",
            "that's just how it is. Decided by me, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "No matter how dirty this room gets, I am determined\x01",
            "to do absolutely nothing to resolve the problem! Not\x01",
            "my job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_552")

    label("loc_4A9")


    ChrTalk(    #7
        0xFE,
        "MY job involves training new people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "How do I do this? Get them to clean up this\x01",
            "room for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Which means I don't have to lift a finger.\x01",
            "Smart, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_552")

    TalkEnd(0xFE)
    Return()

    # Function_3_372 end

    def Function_4_556(): pass

    label("Function_4_556")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_6FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5EB")

    ChrTalk(    #10
        0xFE,
        "On an unrelated note...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "...this place feels awfully...quiet, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Maybe I'm just feeling uneasy over nothing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6FD")

    label("loc_5EB")


    ChrTalk(    #13
        0xFE,
        (
            "Whew... It's so good to finally be done with\x01",
            "all the repair work on the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "It feels like forever since I was last back here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Although thinking about it, there's still\x01",
            "the adjustments to be made to the engines,\x01",
            "so our work may not be quite done yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_6FD")

    TalkEnd(0xFE)
    Return()

    # Function_4_556 end

    def Function_5_701(): pass

    label("Function_5_701")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_873")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_78B")
    OP_8C(0xFE, 270, 0)

    ChrTalk(    #16
        0xFE,
        "Wh-What are these?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "I know these plans aren't Russell's work...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "They're way too clean for that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_873")

    label("loc_78B")


    ChrTalk(    #19
        0xFE,
        "I wonder how Freddy's doing right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I haven't heard from him since he went back\x01",
            "to Rolent. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "He was a hell of a kid for one so young. \x01",
            "He's gonna shake things up as a real\x01",
            "skilled artisan one day, if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_873")

    TalkEnd(0xFE)
    Return()

    # Function_5_701 end

    def Function_6_877(): pass

    label("Function_6_877")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-101240, 0, 100160, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, -102660, 0, 97700, 270)
    SetChrPos(0x11, -103650, 0, 99100, 180)
    SetChrPos(0x107, -98510, 0, 101000, 270)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x10,
        (
            "#100FWhat are these wires here for, Erika?\x02\x03",

            "They look completely unnecessary to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x11,
        (
            "#1456FThey're to deal with noise.\x02\x03",

            "This design requires a very high degree of\x01",
            "precision, so it was a necessary addition.\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_70(0x2, 0x1E)
    OP_73(0x2)

    def lambda_A05():
        OP_8E(0xFE, 0xFFFE76D6, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A05)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 225, 400)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    Sleep(300)

    ChrTalk(    #24
        0x107,
        "#060F#5PMom?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x11,
        (
            "#1456FSo the orbal pressure changes get absorbed\x01",
            "into here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "#100FHmm... I see...\x02",
    )

    CloseMessageWindow()

    def lambda_AAA():
        OP_8E(0xFE, 0xFFFE6B50, 0x0, 0x18A88, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AAA)
    WaitChrThread(0x107, 0x1)
    OP_8C(0x107, 180, 500)
    Sleep(300)

    ChrTalk(    #27
        0x107,
        "#0560F#3S#1PMom!#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(900)

    def lambda_B38():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_B38)
    Sleep(100)

    def lambda_B4B():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_B4B)
    Sleep(300)

    ChrTalk(    #28
        0x11,
        "#1454F#6POh, Tita. What are you doing there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        (
            "#560F#5PW-Well...\x02\x03",

            "...I was wondering if, you know, there was\x01",
            "anything I could do to help.\x02\x03",

            "I want to do something for Renne, too...\x02\x03",

            "#561FI'm just not sure what I can actually do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#1454F#6PHmm? What you can do?\x02\x03",

            "#1450FWell, if you want to help me out, there IS\x01",
            "one thing you could do for me.\x02\x03",

            "It's an annoying job, but if you're up for it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x107,
        (
            "#064F#5PAn annoying job?\x02\x03",

            "#061FO-Okay... I'll do anything I can to help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        (
            "#1451F#6PIt's nothing that important, really, but I appreciate\x01",
            "it all the same.\x02\x03",

            "I need you to go talk to Murdock and get him\x01",
            "to sort out the paperwork for our return to\x01",
            "Liberl.\x02\x03",

            "#1450FThe way we returned home was kinda, uh, \x01",
            "borderline illegal. So no official paperwork's\x01",
            "been filed or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        "#064F#5PU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        (
            "#1458F#6PI'm cool with it, but Dan's brought it up a few\x01",
            "times, so it'd be good if someone could get it\x01",
            "taken care of.\x02\x03",

            "#1456FSo, thanks!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F14():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_F14)
    Sleep(300)

    def lambda_F27():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_F27)
    Sleep(300)

    ChrTalk(    #35
        0x107,
        (
            "#560F#1PO-Okay...\x02\x03",

            "...\x02\x03",

            "#561F(This wasn't what I had in mind when I said\x01",
            "I wanted to help...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x107)

    ChrTalk(    #36
        0x107,
        (
            "#060F#1P(Oh, well. I guess I am still helping her by\x01",
            "doing this.)\x02\x03",

            "(I'll just have to get it sorted out quickly so\x01",
            "I can get back and help with the real work!)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 500)

    def lambda_1063():
        OP_8E(0xFE, 0xFFFE76D6, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1063)
    WaitChrThread(0x107, 0x1)
    OP_70(0x2, 0x1E)
    OP_73(0x2)

    def lambda_108D():
        OP_8E(0xFE, 0xFFFE7F32, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_108D)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_877 end

    SaveToFile()

Try(main)
