from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1501   ._SN',
        MapName             = 'Bose',
        Location            = 'T1501.x',
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
        'Boat',                                 # 9
        'Kyle',                                 # 10
        'Josette',                              # 11
        'Black-Clad Soldier',                   # 12
        'Special Ops Soldier',                  # 13
        'New Ansel Path',                       # 14
    )

    DeclEntryPoint(
        Unknown_00              = -7000,
        Unknown_04              = 0,
        Unknown_08              = 82000,
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
        Unknown_30              = 225,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 50,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02120 ._CH',             # 00
        'ED6_DT07/CH02130 ._CH',             # 01
        'ED6_DT07/CH02200 ._CH',             # 02
        'ED6_DT07/CH00444 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH02120P._CP',             # 00
        'ED6_DT07/CH02130P._CP',             # 01
        'ED6_DT07/CH02200P._CP',             # 02
        'ED6_DT07/CH00444P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8640,
        Z                   = 0,
        Y                   = 96040,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -8691,
        Y                   = 3000,
        Z                   = 54000,
        Range               = -10060,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xDEEE,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -29705,
        Y                   = -3000,
        Z                   = 53403,
        Range               = -31123,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xC4FE,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -4352,
        Y                   = -1000,
        Z                   = 81810,
        Range               = -10405,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x142A8,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -5850,
        Y                   = -1000,
        Z                   = 80880,
        Range               = -10140,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x14438,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -43330,
        Y                   = -3000,
        Z                   = 38850,
        Range               = -46440,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xA046,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )


    ScpFunction(
        "Function_0_22A",          # 00, 0
        "Function_1_23E",          # 01, 1
        "Function_2_25B",          # 02, 2
        "Function_3_271",          # 03, 3
        "Function_4_34E",          # 04, 4
        "Function_5_7AD",          # 05, 5
        "Function_6_7E2",          # 06, 6
        "Function_7_810",          # 07, 7
        "Function_8_834",          # 08, 8
        "Function_9_B79",          # 09, 9
        "Function_10_248C",        # 0A, 10
        "Function_11_252A",        # 0B, 11
        "Function_12_26A2",        # 0C, 12
    )


    def Function_0_22A(): pass

    label("Function_0_22A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_23D")
    OP_A3(0x3FA)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_23D")

    Return()

    # Function_0_22A end

    def Function_1_23E(): pass

    label("Function_1_23E")

    OP_16(0x2, 0xFA0, 0xFFFDC998, 0xFFFEE2D8, 0x30046)
    OP_71(0x1, 0x4)
    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_23E end

    def Function_2_25B(): pass

    label("Function_2_25B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_270")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_25B")

    label("loc_270")

    Return()

    # Function_2_25B end

    def Function_3_271(): pass

    label("Function_3_271")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    FadeToBright(2000, 0)
    OP_6D(-7046, 500, 43491, 0)
    OP_6B(5900, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, -9345, 0, 78200, 180)
    SetChrPos(0x102, -10370, 0, 78100, 180)
    SetChrPos(0x104, -8638, 0, 79300, 180)
    SetChrPos(0x103, -9788, 0, 79400, 180)

    def lambda_2EE():
        OP_6C(327000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EE)
    Sleep(1000)

    def lambda_303():
        OP_67(0, 4100, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_303)

    def lambda_31B():
        OP_6D(-12358, 3550, 46969, 7000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31B)
    OP_6B(3547, 7000)
    FadeToDark(1000, 0, -1)
    OP_A2(0x3FA)
    OP_0D()
    NewScene("ED6_DT01/T1511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_271 end

    def Function_4_34E(): pass

    label("Function_4_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AC")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x34F)
    OP_28(0x38, 0x1, 0x200)
    SetChrPos(0x9, -8576, 0, 86453, 0)
    SetChrPos(0xA, -7848, 0, 86453, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x0, 0, 400)
    OP_8C(0x1, 0, 400)
    OP_8C(0x2, 0, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB")

    ChrTalk(    #0
        0x101,
        "#004FH-Hey, what's that...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_457")

    label("loc_3FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42F")

    ChrTalk(    #1
        0x102,
        "#012FIt looks like they came...\x02",
    )

    CloseMessageWindow()
    Jump("loc_457")

    label("loc_42F")


    ChrTalk(    #2
        0x103,
        "#027FJust like the old man said...\x02",
    )

    CloseMessageWindow()

    label("loc_457")

    Sleep(100)
    Fade(1000)

    def lambda_467():
        OP_6D(-8786, 0, 78490, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_467)

    def lambda_47F():
        OP_6C(0, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_47F)
    OP_0D()

    def lambda_490():
        OP_8E(0xFE, 0xFFFFDE80, 0x0, 0x12D90, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_490)
    Sleep(600)
    OP_8E(0xA, 0xFFFFE158, 0x0, 0x13178, 0xBB8, 0x0)

    ChrTalk(    #3
        0x9,
        (
            "#200FWell...it looks like we're a little\x01",
            "early, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 400)

    ChrTalk(    #4
        0xA,
        (
            "#210F#4PYeah, it seems that way.\x02\x03",

            "You know, if this were the middle\x01",
            "of the day, we could have gotten\x01",
            "ourselves a bite to eat on the way.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 45, 400)

    ChrTalk(    #5
        0x9,
        (
            "#203FQuit talking nonsense.\x01",
            "We're outlaws, remember?\x02\x03",

            "#200FNow let's hurry up and get moving.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x5)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #6 op#A op#5
        0xA,
        "#213F#4P#15AAh, wait for me, Kyle.\x05\x02",
    )

    Sleep(1500)
    OP_43(0xA, 0x1, 0x0, 0x6)

    def lambda_64A():
        OP_6D(-15030, 0, 60460, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64A)

    def lambda_662():
        OP_6C(225000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_662)
    WaitChrThread(0xA, 0x1)
    Sleep(1000)
    SetChrPos(0x101, -12740, 4000, 55150, 315)
    SetChrPos(0x102, -11650, 4000, 55060, 315)
    SetChrPos(0x103, -10600, 4000, 55110, 270)
    OP_6D(-11630, 4000, 55050, 2000)

    ChrTalk(    #7
        0x101,
        "#002FI should have known it'd be them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#012FIt looks like they're headed for\x01",
            "the far pier.\x02\x03",

            "I wonder what they intend to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#027FShall we take a look and find out?\x02\x03",

            "Let's try to get as close as we can\x01",
            "without being noticed.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_7AC")

    Return()

    # Function_4_34E end

    def Function_5_7AD(): pass

    label("Function_5_7AD")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFD88C, 0x0, 0xFF78, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFAB46, 0x0, 0xD8C2, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_5_7AD end

    def Function_6_7E2(): pass

    label("Function_6_7E2")

    OP_8E(0xFE, 0xFFFFD88C, 0x0, 0xFF78, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFAB46, 0x0, 0xD8C2, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_7E2 end

    def Function_7_810(): pass

    label("Function_7_810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_823")
    Call(0, 9)
    Jump("loc_833")

    label("loc_823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_833")
    Call(0, 11)

    label("loc_833")

    Return()

    # Function_7_810 end

    def Function_8_834(): pass

    label("Function_8_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_END)), "loc_83E")
    Jump("loc_B78")

    label("loc_83E")

    OP_A2(0x36A)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -45460, -2000, 38500, 180)
    SetChrPos(0x102, -44530, -2000, 39140, 180)
    SetChrPos(0x103, -45500, -2000, 39550, 180)
    OP_6D(-45030, -2000, 38970, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #10
        0x101,
        (
            "#007F#6PUm, I don't see anyone.\x02\x03",

            "#505FI don't know what kind of business those\x01",
            "siblings could have here, but do you\x01",
            "think they'll really show up?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)

    ChrTalk(    #11
        0x102,
        (
            "#012F#4PThere's no guarantee of course, but...if\x01",
            "Lloyd's information has any truth to it,\x01",
            "my best guess is that they'll be here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 135, 400)

    ChrTalk(    #12
        0x103,
        (
            "#022FHowever, if we move around too much,\x01",
            "there's the possibility we'll be seen\x01",
            "and they'll take off.\x02\x03",

            "Since the sky bandits are supposed\x01",
            "to come from the road, it might be a\x01",
            "good idea to watch the area.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #13
        0x101,
        (
            "#006F#6PRight...so where should we watch\x01",
            "from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#015F#4PWe need a place where we can\x01",
            "see the road without being\x01",
            "noticed ourselves.\x02\x03",

            "#010FA place like that would be ideal.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x38, 0x1, 0x100)
    EventEnd(0x0)

    label("loc_B78")

    Return()

    # Function_8_834 end

    def Function_9_B79(): pass

    label("Function_9_B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_248B")
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_A2(0x350)
    OP_28(0x38, 0x1, 0x400)
    SetChrPos(0x9, -44910, -1970, 38660, 180)
    SetChrPos(0xA, -44520, -1970, 39860, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_BC7():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BC7)
    OP_6D(-44910, -1970, 38660, 3000)
    SetChrPos(0x101, -31171, 0, 56060, 180)
    SetChrPos(0x102, -32244, 0, 56400, 180)
    SetChrPos(0x103, -30520, 0, 55440, 180)

    ChrTalk(    #15
        0x9,
        (
            "#200FI should have figured they wouldn't\x01",
            "be here yet.\x02\x03",

            "They always come exactly on time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "#212FI really hate those guys.\x02\x03",

            "They act like they're so superior...and\x01",
            "to be honest, they're kinda scary.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #17
        0x9,
        (
            "#200FNo doubt about that... They are quite\x01",
            "the clandestine bunch.\x02\x03",

            "But there's not much we can do about\x01",
            "it. This is an order from Don.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6C(45000, 0)
    OP_6D(-30885, 0, 55794, 0)
    OP_0D()

    ChrTalk(    #18
        0x103,
        "#020F(This seems to be a good place...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#006F(Yeah, we can hear every word\x01",
            "they're saying, too...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6C(225000, 0)
    OP_6D(-44910, -1970, 38660, 0)
    OP_0D()

    ChrTalk(    #20
        0xA,
        (
            "#215F...\x02\x03",

            "Hey, Kyle...\x02\x03",

            "Don't you think Don's been acting\x01",
            "a bit strange recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        "#204F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "#212FIt's just not like him if you ask\x01",
            "me. You know...the whole hijacking\x01",
            "of airliners thing.\x02\x03",

            "While I admit it was lucrative,\x01",
            "now we've got the army clamping\x01",
            "down on us full scale...\x02\x03",

            "Not to mention those annoying\x01",
            "bracers are now involved...\x02\x03",

            "And he's gone and taken hostages,\x01",
            "and demanded a ransom in return...\x02\x03",

            "No matter how I think about it,\x01",
            "it seems like Don has gone way\x01",
            "overboard this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "#200FIn the end, you'll always be\x01",
            "just a girl...\x02\x03",

            "Deep down, you're just not cut out\x01",
            "to run with the bad crowd.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0xA,
        "#216FExcuse me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#202FOkay, maybe not the best wording...\x01",
            "but I meant it as a compliment.\x02\x03",

            "#200FIf things are getting too tough for\x01",
            "you, you're always welcome to\x01",
            "try salvaging a life back home.\x02\x03",

            "It shouldn't be too hard to get by\x01",
            "as long as you don't set your\x01",
            "sights too high.\x02\x03",

            "Although admittedly, it is a bit\x01",
            "colder than Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "#214FD-Do you think you can just treat\x01",
            "me like a kid and I'm not going\x01",
            "to get angry?\x02\x03",

            "I'd like to see you get by without me,\x01",
            "what with your crap cooking and all.\x01",
            "Not to mention the laundry!\x02\x03",

            "Do you really want to go back to\x01",
            "burnt toast and turning your\x01",
            "underwear inside out?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x9,
        (
            "#203FHa ha...okay, okay.\x01",
            "I see your point, and I really am\x01",
            "sick of toast, burnt or otherwise.\x02\x03",

            "#200FBut anyway, think about what\x01",
            "I said before it gets too late to\x01",
            "back out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xA,
        "#215F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        (
            "#203FNow getting back to what you\x01",
            "said earlier...\x02\x03",

            "I do have to agree that Don has\x01",
            "been acting pretty weird.\x02\x03",

            "Does he expect us to just keep\x01",
            "fishing for ransom? We should\x01",
            "take what we can get!\x02\x03",

            "And I'd like to believe that Don\x01",
            "is smart enough to see that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "#212FDon't you think he started acting\x01",
            "strange about the time that guy\x01",
            "showed up?\x02\x03",

            "That's the only thing I can think\x01",
            "of as to why he started acting\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "#200FYeah...he was the one who\x01",
            "introduced us to those other\x01",
            "guys, too.\x02\x03",

            "He might have even gotten Don\x01",
            "to buy into his ideas...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6C(45000, 0)
    OP_6D(-30885, 0, 55794, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #32
        0x101,
        "#505F(Who is 'that guy' and 'he'?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x103,
        (
            "#022F(That's certainly a good\x01",
            "question.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_20(0x5DC)
    Sleep(1000)

    ChrTalk(    #34
        0x102,
        "#014F(Huh? What's that over there...?)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #35
        0x101,
        "#004F(What's what?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#012F(It looks like whoever it was they\x01",
            "were waiting for finally showed up.)\x02",
        )
    )

    CloseMessageWindow()
    OP_21()
    OP_1D(0x51)
    Sleep(100)
    Fade(1000)
    OP_6C(225000, 0)
    OP_6D(-45040, -1970, 29060, 0)
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_8C(0x9, 180, 0)
    OP_8C(0xA, 180, 0)
    SetChrPos(0x8, -45110, -2700, 20060, 180)
    SetChrFlags(0x8, 0x40)
    OP_A1(0x8, 0x1)
    LoadEffect(0x4, "map\\\\mp013_00.eff")
    LoadEffect(0x5, "map\\\\mp013_01.eff")
    PlayEffect(0x4, 0x0, 0x8, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x8, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    OP_72(0x1, 0x4)
    OP_72(0x1, 0x2)
    OP_71(0x1, 0x400)
    OP_71(0x1, 0x40)
    OP_48()
    OP_89(0xB, -45060, -2000, 21500, 0)
    OP_89(0xC, -45060, -2000, 20000, 0)
    OP_22(0xD4, 0x0, 0x64)

    def lambda_18DC():
        OP_6D(-45380, -1970, 36390, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_18DC)

    def lambda_18F4():
        OP_91(0xFE, 0x0, 0x0, 0x11170, 0x960, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18F4)
    Sleep(2000)

    def lambda_1914():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1914)
    Sleep(800)

    def lambda_1934():
        OP_91(0xFE, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1934)
    Sleep(700)

    def lambda_1954():
        OP_91(0xFE, 0x0, 0x0, 0x124F8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1954)
    Sleep(600)
    OP_82(0x1, 0x2)

    def lambda_1977():
        OP_91(0xFE, 0x0, 0x0, 0x124F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1977)
    Sleep(500)

    def lambda_1997():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1997)
    Sleep(400)

    def lambda_19B7():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19B7)
    PlayEffect(0x4, 0x2, 0x8, 0, -300, 2400, 180, 0, 0, 1100, 100, 1600, 0xFF, 0, 0, 0, 0)
    Sleep(400)

    def lambda_1A0C():
        OP_91(0xFE, 0x0, 0x0, 0xC350, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A0C)
    Sleep(300)
    OP_82(0x0, 0x2)

    def lambda_1A2F():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A2F)
    Sleep(300)

    def lambda_1A4F():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A4F)
    Sleep(300)

    def lambda_1A6F():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A6F)
    Sleep(300)

    def lambda_1A8F():
        OP_91(0xFE, 0x0, 0x0, 0x3E8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A8F)
    OP_82(0x2, 0x2)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #37
        0x9,
        (
            "#200FIt looks like you made it.\x02\x03",

            "On time as usual, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "#210FHmph. You could have come a little early\x01",
            "for a change...or even late!\x02\x03",

            "Definitely not my type, that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "#280FSay what you will, but we're trained\x01",
            "to be punctual.\x02\x03",

            "Now if that displeases you, then let\x01",
            "me offer my sincerest apology.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0xA,
        (
            "#214FR-Relax!\x01",
            "I was just being sarcastic!\x02\x03",

            "(Now I KNOW you guys are definitely\x01",
            "not the type I want to be around...)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #41
        0x9,
        (
            "#201F#5PEnough, already! We don't have\x01",
            "time for that.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #42
        0x9,
        (
            "#200FNow...how about we get down to\x01",
            "business?\x02\x03",

            "Have there been any other developments\x01",
            "since last time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "#280FYes. In fact, Her Majesty has\x01",
            "finally made a move.\x02\x03",

            "She intends to contribute to the\x01",
            "ransom from her own assets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#202FS-Seriously...? We're going to\x01",
            "get paid out of the queen's own\x01",
            "pocket...?\x02\x03",

            "I guess we're pretty close to\x01",
            "getting the money then, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#210FHow about the Royal Army?\x02\x03",

            "Is there any indication that they've\x01",
            "figured out where our hideout is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xB,
        (
            "#280FNot yet, but it's only a matter of\x01",
            "time until they do.\x02\x03",

            "We've received reports that members\x01",
            "of the Bracer Guild are on the move\x01",
            "as well.\x02\x03",

            "At any rate, on the morning of the\x01",
            "payoff you'll need to leave your\x01",
            "hideout behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "#200FYeah...no problem there. We just\x01",
            "happened to run into the temporary\x01",
            "shelter by chance.\x02\x03",

            "Don shouldn't have any regrets\x01",
            "about it either.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(-30885, 0, 55794, 0)
    OP_8C(0x101, 180, 0)
    OP_6C(45000, 0)
    OP_0D()

    ChrTalk(    #48
        0x101,
        (
            "#002F(*sigh* There are WAY too many\x01",
            "suspicious types involved in this...)\x02\x03",

            "(What do you want to do, Schera?\x01",
            "Should we just storm in? Shoot 'em\x01",
            "all, let Aidios sort them out?)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)

    ChrTalk(    #49
        0x103,
        (
            "#026F(Hmm...I've got a much better\x01",
            "idea.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#004F(A better idea?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        (
            "#027F(These two siblings appearing here\x01",
            "means that the sky bandits' airship\x01",
            "is parked somewhere nearby.)\x02\x03",

            "#027F(There's not much we could do if they\x01",
            "got away again, so how about we try\x01",
            "taking that out first?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#006F(I see...take away their means of\x01",
            "escape, right?)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #53
        0x101,
        (
            "#006F(I'm down for that.\x01",
            "How about you, Joshua?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#510F(...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#505F(Joshua...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#014F(Oh, right...)\x02\x03",

            "(Take out the airship first, right?\x01",
            "Yeah, I think it's a good idea, too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#002F(What's wrong...?)\x02\x03",

            "(Your face looks really tense all\x01",
            "of a sudden...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#013F(It's nothing...)\x02\x03",

            "(Yeah, I'm sure it's just my mind\x01",
            "playing tricks on me.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#002F(...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x103,
        (
            "#020F(We don't have much time...)\x02\x03",

            "(We've got to get out onto the road\x01",
            "and start looking for that airship\x01",
            "before they finish their meeting.)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x5DC)
    Sleep(50)
    EventEnd(0x4)
    OP_21()
    OP_1E()

    label("loc_248B")

    Return()

    # Function_9_B79 end

    def Function_10_248C(): pass

    label("Function_10_248C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2529")
    EventBegin(0x0)
    OP_20(0x7D0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05The party took to the road in search of the location of the airship.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #62
        "\x07\x05And...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_28(0x38, 0x1, 0x800)
    OP_28(0x39, 0x4, 0x2)
    OP_28(0x39, 0x4, 0x4)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R1403   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2529")

    Return()

    # Function_10_248C end

    def Function_11_252A(): pass

    label("Function_11_252A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26A1")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25AA")

    ChrTalk(    #63
        0x101,
        (
            "#006F(We need to find that airship first.\x01",
            "Let's head up the road and start\x01",
            "searching for it.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2686")

    label("loc_25AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2634")

    ChrTalk(    #64
        0x102,
        (
            "#012F(Finding and taking out the airship\x01",
            "is our first priority...let's get on the\x01",
            "road and make a sweep of the area.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2686")

    label("loc_2634")


    ChrTalk(    #65
        0x103,
        (
            "#022F(We don't have much time...\x01",
            "Let's move out and search for\x01",
            "the airship.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2686")

    OP_8E(0x0, 0xFFFF8F8A, 0x0, 0xCB20, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_26A1")

    Return()

    # Function_11_252A end

    def Function_12_26A2(): pass

    label("Function_12_26A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27FD")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271A")

    ChrTalk(    #66
        0x101,
        (
            "#006F(This leads to the road, doesn't\x01",
            "it? Right now we need to head to\x01",
            "the far pier.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DF")

    label("loc_271A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_278A")

    ChrTalk(    #67
        0x102,
        (
            "#012F(Heading for the road isn't going\x01",
            "to do us much good...we'd better\x01",
            "hurry to the pier.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DF")

    label("loc_278A")


    ChrTalk(    #68
        0x103,
        (
            "#022F(This goes out onto the road...\x01",
            "The pier is our first priority\x01",
            "right now.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27DF")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_294D")

    label("loc_27FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_294D")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2821")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_2828")

    label("loc_2821")

    TurnDirection(0x103, 0x0, 400)

    label("loc_2828")


    def lambda_282E():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_282E)

    def lambda_283C():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_283C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 2)), scpexpr(EXPR_END)), "loc_28CA")

    ChrTalk(    #69
        0x103,
        (
            "#022FWe don't need to head to the\x01",
            "road right now.\x02\x03",

            "We should be looking for a place\x01",
            "where we can monitor it, instead...\x02",
        )
    )

    Jump("loc_2931")

    label("loc_28CA")


    ChrTalk(    #70
        0x103,
        (
            "#022FWe don't need to head to the\x01",
            "road just yet.\x02\x03",

            "Let's first start by heading around\x01",
            "to the pier.\x02",
        )
    )


    label("loc_2931")

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_294D")

    Return()

    # Function_12_26A2 end

    SaveToFile()

Try(main)
