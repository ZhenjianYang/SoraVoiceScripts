from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4143   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4143.x',
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
        'Target Camera',                        # 9
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
        "Function_0_CA",           # 00, 0
        "Function_1_107",          # 01, 1
        "Function_2_108",          # 02, 2
        "Function_3_1477",         # 03, 3
        "Function_4_1509",         # 04, 4
        "Function_5_150F",         # 05, 5
        "Function_6_157B",         # 06, 6
        "Function_7_1603",         # 07, 7
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_F5")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_106")

    label("loc_F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_106")

    Return()

    # Function_0_CA end

    def Function_1_107(): pass

    label("Function_1_107")

    Return()

    # Function_1_107 end

    def Function_2_108(): pass

    label("Function_2_108")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x103, 540, -250, -3300, 180)
    SetChrPos(0x151, -540, -250, -3100, 180)
    OP_6D(760, -250, -5360, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)

    def lambda_179():
        OP_6D(1760, -250, -1360, 4000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_179)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    OP_63(0x103)
    OP_63(0x151)
    Sleep(500)

    ChrTalk(    #0
        0x103,
        (
            "#1642F#2PCome ON... Why're there still so many\x01",
            "of them going around?\x02\x03",

            "#1647FHow can we get to the guild like this?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x151,
        (
            "#1654FI think we're going to have to spend the rest\x01",
            "of the night here, unfortunately.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2A8():
        TurnDirection(0xFE, 0x151, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2A8)
    Sleep(100)

    def lambda_2BB():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_2BB)
    Sleep(300)

    ChrTalk(    #2
        0x103,
        (
            "#1642F#2PIt won't need to come to that. I think if I can find\x01",
            "a good opening, we can force our way through.\x02\x03",

            "It's just a case of finding one...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x151,
        (
            "#1652FI don't think that's a good idea. We need to be\x01",
            "careful and rest while we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        (
            "#1647F#2P(...As logical as that sounds, I'm not buying\x01",
            "it's her real reason.)\x02\x03",

            "#1646F(Get a grip, Schera! I can't let my emotions\x01",
            "get the better of me!)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x151, 0x3, 0x0, 0x3)
    OP_8C(0x103, 180, 400)
    Sleep(300)
    OP_43(0x103, 0x3, 0x0, 0x4)

    ChrTalk(    #5
        0x103,
        (
            "#1646F#2PThere's no guarantee we're even safe here,\x01",
            "you know.\x02\x03",

            "#1642FI still think the safest option in the long run is\x01",
            "to get to the guild--no matter what we have to\x01",
            "do to get there.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    WaitChrThread(0x103, 0x3)
    OP_8C(0x103, 270, 400)
    OP_62(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    def lambda_55C():
        OP_6D(400, 2500, 1060, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_55C)

    def lambda_574():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_574)
    Sleep(1000)
    OP_8C(0x103, 0, 400)
    WaitChrThread(0x10, 0x0)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x151, 0x3)

    ChrTalk(    #6
        0x103,
        "#1644FH-Hey! Where do you think you're going?!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x103, 0x3, 0x0, 0x6)
    Sleep(1000)
    OP_43(0x151, 0x3, 0x0, 0x5)

    def lambda_5FE():
        OP_6D(1220, 4000, 5340, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_5FE)
    WaitChrThread(0x151, 0x3)

    ChrTalk(    #7
        0x151,
        (
            "#1650FI think the second floor is a better place\x01",
            "to rest than the first.\x02\x03",

            "We'll find it easier to escape from here\x01",
            "than we would from below.\x02\x03",

            "This should be a good spot.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x3)

    ChrTalk(    #8
        0x103,
        (
            "#1642F#1PWait one damn minute.\x02\x03",

            "#1642FThis is your safety we're talking about, here!\x01",
            "You could stand to listen to me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)
    Sleep(300)

    ChrTalk(    #9
        0x151,
        (
            "#1654FThose men will be patrolling carefully for the\x01",
            "rest of the night. \x02\x03",

            "They aren't going to give you the opening you\x01",
            "want...or at least I don't believe they will.\x02\x03",

            "#1650FWe've made it this far, so I think it would be\x01",
            "best for us to rest tonight and resume trying\x01",
            "tomorrow. Don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        (
            "#1646F#1P...\x02\x03",

            "#1648FTrying to do what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x151,
        "#1653FPardon?\x02",
    )

    CloseMessageWindow()

    def lambda_8B9():

        label("loc_8B9")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_8B9")

    QueueWorkItem2(0x151, 2, lambda_8B9)

    def lambda_8CA():
        OP_8E(0xFE, 0xFFFFFFC4, 0xFA0, 0xDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8CA)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 500)
    Sleep(300)

    ChrTalk(    #12
        0x103,
        (
            "#1646F#3PYou're still hiding something, aren't you?\x02\x03",

            "For one thing, you're aaawfully familiar with\x01",
            "this city for someone who claims it's her first\x01",
            "time here.\x02\x03",

            "You also seem to know a lot about those men\x01",
            "and what they will and won't do, too...\x02\x03",

            "#1648FWhat exactly are you really after?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Sleep(500)
    OP_44(0x151, 0x2)
    OP_8C(0x103, 135, 400)

    def lambda_A2D():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0x9B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A2D)
    WaitChrThread(0x103, 0x1)

    def lambda_A4D():
        OP_8E(0xFE, 0x7F8, 0xFA0, 0x9B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A4D)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    ChrTalk(    #13
        0x103,
        (
            "#1646FIt's plain as day at this point that you want\x01",
            "more than just not to be caught by them.\x02\x03",

            "If that wasn't the case, you wouldn't have\x01",
            "asked to be shown around the capital. Not\x01",
            "that I think that's what you want, either.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 500)
    Sleep(300)

    ChrTalk(    #14
        0x103,
        "#1648FWhat's your real goal?\x02",
    )

    CloseMessageWindow()

    def lambda_B83():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0x9B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B83)
    WaitChrThread(0x103, 0x1)
    Sleep(300)

    def lambda_BA8():
        OP_6D(2120, 4000, 3940, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_BA8)

    def lambda_BC0():
        OP_6B(2700, 1500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_BC0)

    def lambda_BD0():
        OP_6C(50000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_BD0)
    OP_8C(0x103, 0, 400)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #15
        0x103,
        "#1648F#4P...Well? No answer?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x151,
        "#1656F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#1646F#4PThe work we do is based around trust.\x02\x03",

            "We can't accept requests from people who won't\x01",
            "tell us what they're up to, or who knows what\x01",
            "kinds of crimes we could be abetting?\x02\x03",

            "#1642FGo on. The whole thing about that inheritance\x01",
            "was all a big, fat lie, wasn't it?\x02\x03",

            "Something about you'd been setting off alarms\x01",
            "since we started running around together.\x01",
            "Strike that--since you first came to the guild.\x02\x03",

            "#1648FWhy did you lie to me?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(500)

    ChrTalk(    #18
        0x151,
        (
            "#1654F#5PU-Umm...\x02\x03",

            "The story about the inheritance is true.\x01",
            "I swear it.\x02\x03",

            "#1652FI... I want to go to Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x151)
    Sleep(200)
    OP_1D(0xB2)
    Sleep(500)

    ChrTalk(    #19
        0x151,
        (
            "#1652F#5PI really am the one to whom my grandfather gave\x01",
            "his fortune.\x02\x03",

            "But I haven't finished the necessary procedures\x01",
            "to truly inherit it yet.\x02\x03",

            "#1654FUntil I complete the required paperwork in Grancel\x01",
            "Castle's administrative room, I'm not legally allowed\x01",
            "anything.\x02\x03",

            "And that's why there are so many of those men in\x01",
            "black around that area.\x02\x03",

            "#1656FAll of my relatives know exactly what I need to do,\x01",
            "you see.\x02\x03",

            "So they're...trying to make sure I can't do it.\x02\x03",

            "...\x02\x03",

            "#1652FStill, if I don't keep trying to move forward,\x01",
            "I'll...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x103,
        (
            "#1648F#4PWhat a mess...\x02\x03",

            "Well, okay. For argument's sake, let's assume\x01",
            "that I believe all of what you just said.\x02\x03",

            "#1646FWhy am I only hearing about it now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x151,
        (
            "#1656F#5PUmm...\x02\x03",

            "#1655FTh-That is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x103,
        (
            "#1646F#4PYou thought I'd want in on that money,\x01",
            "didn't you?\x02\x03",

            "If I did and I knew everything, I'd have all the\x01",
            "opportunities a greedy girl could dream of to\x01",
            "take it when together with you.\x02\x03",

            "#1642FThat's what you thought I'd do, isn't it? I'd play\x01",
            "along and then steal it all for myself the second\x01",
            "a chance presented itself.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)

    ChrTalk(    #23
        0x103,
        (
            "#1644F#4P#3SDo I look like THAT much of a scumbag\x01",
            "to you?!#2S\x02",
        )
    )

    OP_7C(0x96, 0x96, 0xBB8, 0xC8)
    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 500)

    ChrTalk(    #24
        0x151,
        "#1652F#3S#5PN-No! You don't!#2S\x02",
    )

    OP_7C(0x96, 0x96, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_59()
    Sleep(500)

    ChrTalk(    #25
        0x151,
        (
            "#1652F#5PThat's not it at all.\x02\x03",

            "After I lost Grandfather, I lived all on my own.\x02\x03",

            "#1654FBut the second his will became public, I had\x01",
            "crowds of people descending upon me.\x02\x03",

            "#1656FPeople who, like you said, were interested only\x01",
            "in claiming his fortune for themselves.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1455():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1455)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4152   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_2_108 end

    def Function_3_1477(): pass

    label("Function_3_1477")

    Sleep(1000)
    OP_8C(0x151, 0, 400)
    Sleep(300)

    def lambda_148E():
        OP_8E(0xFE, 0xFFFFFDE4, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_148E)
    WaitChrThread(0x151, 0x1)

    def lambda_14AE():
        OP_8E(0xFE, 0xFFFFF164, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_14AE)
    WaitChrThread(0x151, 0x1)

    def lambda_14CE():
        OP_8E(0xFE, 0xFFFFF164, 0x7D0, 0x12C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_14CE)
    WaitChrThread(0x151, 0x1)

    def lambda_14EE():
        OP_8E(0xFE, 0xFFFFFDA8, 0xFA0, 0x12C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_14EE)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_3_1477 end

    def Function_4_1509(): pass

    label("Function_4_1509")

    Sleep(5000)
    Return()

    # Function_4_1509 end

    def Function_5_150F(): pass

    label("Function_5_150F")

    OP_8C(0x151, 0, 400)
    Sleep(500)
    OP_8C(0x151, 180, 400)
    Sleep(500)
    OP_8C(0x151, 90, 400)
    Sleep(200)

    def lambda_1539():
        OP_8E(0xFE, 0x208, 0xFA0, 0x13B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1539)
    WaitChrThread(0x151, 0x1)

    def lambda_1559():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0xDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1559)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x151, 180, 400)
    Return()

    # Function_5_150F end

    def Function_6_157B(): pass

    label("Function_6_157B")


    def lambda_1581():
        OP_8E(0xFE, 0xFFFFFF74, 0x0, 0xFFFFFC18, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1581)
    WaitChrThread(0x103, 0x1)

    def lambda_15A1():
        OP_8E(0xFE, 0xFFFFF164, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15A1)
    WaitChrThread(0x103, 0x1)

    def lambda_15C1():
        OP_8E(0xFE, 0xFFFFF164, 0x7D0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15C1)
    WaitChrThread(0x103, 0x1)

    def lambda_15E1():
        OP_8E(0xFE, 0xFFFFFFC4, 0xFA0, 0x1388, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_15E1)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 180, 400)
    Return()

    # Function_6_157B end

    def Function_7_1603(): pass

    label("Function_7_1603")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(2120, 4000, 3940, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrPos(0x103, 1000, 4000, 2480, 0)
    SetChrPos(0x151, 1000, 4000, 3540, 180)

    def lambda_1674():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1674)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #26
        0x151,
        (
            "#1652F#5PThat was why I decided to try and get an escort\x01",
            "from someone I COULD trust.\x02\x03",

            "So it's not that I don't think I can trust you.\x01",
            "Not at all.\x02\x03",

            "#1656FA-And, erm...\x02\x03",

            "#1655F...I will admit that wanting to explore the capital\x01",
            "was a lie. I'm sorry for deceiving you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0x103)

    ChrTalk(    #27
        0x103,
        "#1645F*sigh* You're a grade-A moron...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x151,
        "#1656F#5P...I'm sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        (
            "#1642FYou could've said all of this from the beginning\x01",
            "and saved us a lot headache.\x02\x03",

            "If I'd known what you were trying to do, I would\x01",
            "have been able to formally escort you where you\x01",
            "want to go to.\x02\x03",

            "And the guild would've been the safest place for\x01",
            "you to hide out, too. We wouldn't have ended up\x01",
            "in this dump instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x151,
        (
            "#1653F#5PI...suppose you're right.\x02\x03",

            "...\x02\x03",

            "#1656FI... I was just...scared.\x02\x03",

            "I'll never be able to forget what I saw that day.\x02\x03",

            "What I saw in the eyes of everyone who gathered\x01",
            "to hear that will read.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x151, 0, 400)
    Sleep(300)

    def lambda_1A1E():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0x11BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1A1E)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #31
        0x151,
        (
            "#1654F#5PThe horror I felt when I saw it.\x02\x03",

            "Madness. Insanity. Cold, murderous light...\x02\x03",

            "Emotions that no one can explain. That no one\x01",
            "can put into words...\x02\x03",

            "It wasn't visible for long before they managed to\x01",
            "push it back below the surface and out of sight...\x02\x03",

            "...but it was still there.\x02\x03",

            "#1656FBecause now, I believe that's something that all\x01",
            "of us possess naturally.\x02\x03",

            "Human beings are capable of limitless cruelty.\x01",
            "Every one of us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #32
        0x151,
        (
            "#1654F#5PAnd that realization's left me terrified of us all.\x02\x03",

            "It's not that I don't trust bracers...\x02\x03",

            "#1656FIt's just that...\x02\x03",

            "...I've been so scared...\x02\x03",

            "#1654F...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8C(0x151, 180, 500)
    Sleep(300)

    ChrTalk(    #33
        0x151,
        (
            "#1652F#5PI-I'm so sorry!\x02\x03",

            "#1656FI know I shouldn't have wasted your\x01",
            "time with any of this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x103,
        "#1646F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x151,
        (
            "#1656F#5PUmm... I...\x02\x03",

            "#1655FI should never have gotten you caught up in all\x01",
            "of this when you were busy enough already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x151,
        "#1655F#5PJust forget that I--\x02",
    )

    Sleep(200)

    ChrTalk(    #37
        0x103,
        "#1646FListen.\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #38
        0x151,
        "#1653F#5P...Huh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 270, 400)
    Sleep(300)

    ChrTalk(    #39
        0x103,
        (
            "#1646FIt's my policy to give 100% to all work \x01",
            "I undertake.\x02\x03",

            "Don't underestimate me.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_62(0x151, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x151)
    Sleep(500)

    def lambda_1E82():
        OP_8E(0xFE, 0x3E8, 0xFA0, 0xDD4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1E82)
    WaitChrThread(0x151, 0x1)
    OP_62(0x151, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 180, 400)
    Sleep(1000)

    def lambda_1ECA():

        label("loc_1ECA")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_1ECA")

    QueueWorkItem2(0x151, 2, lambda_1ECA)

    def lambda_1EDB():
        OP_8F(0xFE, 0x794, 0xFA0, 0x9B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1EDB)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x103, 275, 400)
    Sleep(800)

    def lambda_1F07():
        OP_8F(0xFE, 0x3E8, 0xFA0, 0xDD4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1F07)
    WaitChrThread(0x151, 0x1)

    def lambda_1F27():
        OP_8F(0xFE, 0xFFFFFFC4, 0xFA0, 0x9B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_1F27)
    WaitChrThread(0x151, 0x1)
    OP_8C(0x103, 95, 400)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_63(0x103)
    OP_0D()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #40
        "\x18\x07\x0CI'm the one who should be apologizing to you.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #41
        (
            "\x18\x07\x0CI've wanted to be strong and to live with my\x01",
            "head held high.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x18\x07\x0CI still believe I was right to feel that way,\x01",
            "and yes, I've lived my hardest until now...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #43
        (
            "\x18\x07\x0C...but you've made me notice that there's\x01",
            "something wrong with my attitude. I'm not\x01",
            "going about it the right way.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "\x18\x07\x0CAnd it's made me realize anew that I want to be\x01",
            "able to keep living with pride in my every step.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #45
        (
            "\x18\x07\x0CSo no more saying sorry, okay? I want to see\x01",
            "this job through to the very end.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    OP_A2(0x2507)
    OP_A2(0x2F50)
    NewScene("ED6_DT21/T4102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1603 end

    SaveToFile()

Try(main)
