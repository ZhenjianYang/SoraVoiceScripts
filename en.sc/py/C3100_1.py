from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C3100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3100_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_6CB",          # 01, 1
        "Function_2_81C",          # 02, 2
        "Function_3_1B1B",         # 03, 3
        "Function_4_22F0",         # 04, 4
        "Function_5_2313",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, -70, 0, -5570, 0)
    SetChrPos(0xF7, 880, 150, -6000, 0)
    SetChrPos(0xF8, -320, 200, -7040, 0)
    SetChrPos(0xF9, 1170, 210, -7190, 0)
    OP_6D(570, 0, -3460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0xFE,
        (
            "This is Leiston Fortress, headquarters\x01",
            "of Her Majesty's Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Civilians are currently barred from entry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000F#2POh, but, um, we're here about the\x01",
            "request you posted on the guild\x01",
            "board.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_283")

    ChrTalk(    #3
        0x106,
        (
            "#050F#2PYeah, the one about 'special training'\x01",
            "or somethin'.\x02\x03",

            "Ain't you heard from your officers about\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD")

    label("loc_283")


    ChrTalk(    #4
        0x103,
        (
            "#020F#2PYes, the one which requested\x01",
            "help for 'special training.'\x02\x03",

            "Did your commander not inform\x01",
            "you we were coming?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD")


    ChrTalk(    #5
        0xFE,
        "Ah, that, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Command did say something about\x01",
            "that, now that you mention it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Not even a soldier and they've roped\x01",
            "you into helping with the training,\x01",
            "huh? I certainly don't envy you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1015F#2PUm... Well, it's part of the job.\x02\x03",

            "#1006FAnyway, could you get whoever's in charge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "Certainly, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Are you sure you're ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1011F#2PReady? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "We've been engaged in a rigorous\x01",
            "training program for some time now.\x01",
            "With no significant rest breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "They're probably going to toss you into\x01",
            "the meat grinder as soon as you go in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "So if you need to change equipment\x01",
            "or get anything, you should take care\x01",
            "of that before going in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1000F#2PI see. Okay.\x02\x03",

            "Could we get a little bit of time, then?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_628")

    ChrTalk(    #16
        0x106,
        (
            "#050F#2PGood idea.\x02\x03",

            "Could you wait a bit?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_666")

    label("loc_628")


    ChrTalk(    #17
        0x103,
        (
            "#020F#2PDuly noted.\x02\x03",

            "Would you mind waiting a bit, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_666")


    ChrTalk(    #18
        0xFE,
        "Not a problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Once you're ready, just say the\x01",
            "word and I'll let you in.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    OP_28(0x6D, 0x1, 0x1)
    OP_28(0x6D, 0x4, 0x4)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_6CB(): pass

    label("Function_1_6CB")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, -70, 0, -5570, 0)
    SetChrPos(0xF7, 880, 150, -6000, 0)
    SetChrPos(0xF8, -320, 200, -7040, 0)
    SetChrPos(0xF9, 1170, 210, -7190, 0)
    OP_6D(570, 0, -3460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #20
        0xFE,
        "You folks ready?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CA")
    OP_28(0x6D, 0x1, 0x2)
    OP_28(0x6D, 0x4, 0x8)
    Call(1, 2)
    Jump("loc_81B")

    label("loc_7CA")


    ChrTalk(    #21
        0xFE,
        "Still not ready?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "You'd best hurry, or you won't\x01",
            "make it in time.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0x9, 255)

    label("loc_81B")

    Return()

    # Function_1_6CB end

    def Function_2_81C(): pass

    label("Function_2_81C")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, -690, 0, 7060, 180)
    SetChrPos(0xD, 870, 0, 7440, 180)
    SetChrPos(0xE, -1090, 0, 8810, 180)
    SetChrPos(0xF, -290, 0, 8810, 180)
    SetChrPos(0x10, 510, 0, 8810, 180)
    SetChrPos(0x11, 1300, 0, 8810, 180)

    ChrTalk(    #23
        0xFE,
        (
            "All right, then.\x01",
            "Let me get the training comman--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    OP_8C(0xFE, 0, 400)

    ChrTalk(    #24
        0xFE,
        (
            "Well, never mind, here he is now.\x01",
            "Sir!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1004F#2PHuh?\x02",
    )

    CloseMessageWindow()
    OP_70(0x0, 0x1C2)
    Sleep(1000)
    Fade(1000)
    OP_6D(-240, 9150, -5410, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x9, 0, 0, -3780, 0)
    SetChrPos(0x101, -540, 0, -5810, 0)
    SetChrPos(0xF7, 660, 0, -5820, 0)
    SetChrPos(0xF8, -670, 220, -7420, 0)
    SetChrPos(0xF9, 820, 230, -7580, 0)
    OP_0D()
    OP_43(0x9, 0x1, 0x1, 0x4)

    def lambda_9ED():
        OP_67(0, 6930, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9ED)

    def lambda_A05():
        OP_6D(0, 0, -4270, 8000)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_A05)

    def lambda_A1D():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_A1D)
    Sleep(2000)

    def lambda_A32():

        label("loc_A32")

        TurnDirection(0x101, 0xB, 400)
        OP_48()
        Jump("loc_A32")

    QueueWorkItem2(0x101, 1, lambda_A32)

    def lambda_A43():

        label("loc_A43")

        TurnDirection(0xF7, 0xB, 400)
        OP_48()
        Jump("loc_A43")

    QueueWorkItem2(0xF7, 1, lambda_A43)
    OP_43(0xB, 0x0, 0x0, 0x2)
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0xE, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)

    def lambda_A7E():
        OP_8E(0xB, 0xFFFFFD4E, 0x0, 0xFFFFF088, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A7E)

    def lambda_A99():
        OP_8E(0xD, 0x366, 0x0, 0xFFFFF204, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A99)

    def lambda_AB4():
        OP_8E(0x10, 0x1FE, 0x0, 0xFFFFF772, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AB4)
    Sleep(35)

    def lambda_AD4():
        OP_8E(0xE, 0xFFFFFBBE, 0x0, 0xFFFFF772, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_AD4)
    Sleep(25)

    def lambda_AF4():
        OP_8E(0xF, 0xFFFFFEDE, 0x0, 0xFFFFF772, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_AF4)

    def lambda_B0F():
        OP_8E(0x11, 0x514, 0x0, 0xFFFFF772, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B0F)
    OP_44(0xFE, 0x1)
    WaitChrThread(0xB, 0x1)
    OP_44(0xB, 0x0)
    OP_4A(0xB, 0)
    WaitChrThread(0xD, 0x1)
    OP_44(0xD, 0x0)
    OP_4A(0xD, 0)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0x0)
    OP_4A(0x10, 0)
    WaitChrThread(0xE, 0x1)
    OP_44(0xE, 0x0)
    OP_4A(0xE, 0)
    WaitChrThread(0xF, 0x1)
    OP_44(0xF, 0x0)
    OP_4A(0xF, 0)
    OP_44(0x11, 0x0)
    OP_4A(0x11, 0)
    WaitChrThread(0xF8, 0x0)
    OP_73(0x0)
    OP_44(0xF7, 0x1)
    OP_44(0x101, 0x1)

    ChrTalk(    #26
        0x101,
        (
            "#1004FMajor Cid!\x01",
            "I haven't seen you in ages!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE3")

    ChrTalk(    #27
        0x106,
        "#052FHey. Been a while, Cid.\x02",
    )

    CloseMessageWindow()

    label("loc_BE3")


    NpcTalk(    #28
        0xB,
        "Cid",
        (
            "#701FHaha. It's nice to see you again.\x02\x03",

            "My apologies for all the trouble we caused you\x01",
            "during the kidnapping of Professor Russell.\x02\x03",

            "You really deserve a much more formal\x01",
            "apology at some point, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1016FHaha, no, no, it's okay.\x01",
            "I mean, you let us get away.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #30
        0xB,
        "Cid",
        (
            "#703FMmm... Your gratitude does me more\x01",
            "credit than I deserve, Miss Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1006FAnyway, we saw your posting on\x01",
            "the board at the guild.\x02\x03",

            "You're doing some kind of special\x01",
            "training, right?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #32
        0xB,
        "Cid",
        (
            "#701FYes. I'd intended for it to be a simple,\x01",
            "standard training session...\x02\x03",

            "...but General Morgan is due to\x01",
            "arrive at the base shortly.\x02\x03",

            "I thought I'd give the men an extra-vigorous\x01",
            "workout to make sure they're ready to show\x01",
            "off, as it were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1007FYeah, that makes sense.\x02\x03",

            "He's got such a booming voice, you have\x01",
            "to be ready for it or else it'll totally\x01",
            "throw you off.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6A")

    ChrTalk(    #34
        0x103,
        "#021FHeehee! Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB3")

    label("loc_F6A")


    ChrTalk(    #35
        0x105,
        (
            "#041FHaha. Yes, General Morgan can be\x01",
            "a bit frightening when angry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB3")


    NpcTalk(    #36
        0xB,
        "Cid",
        (
            "#703FNormally, General Bright would be\x01",
            "in charge of this sort of thing...\x02\x03",

            "However, he's not present at the\x01",
            "moment, so I'm in command for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1011FOh, I see.\x02\x03",

            "#1015FSo Dad's usually here, huh?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0xB,
        "Cid",
        (
            "#701FAccording to the schedule, he should\x01",
            "actually be returning soon.\x02\x03",

            "If you'll be in Zeiss for a while, Miss Bright,\x01",
            "you'll likely have a chance to meet up with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1017FYeah... I might.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 225, 400)

    ChrTalk(    #40
        0xD,
        "Colonel Cid. It's time, sir.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 45, 400)

    NpcTalk(    #41
        0xB,
        "Cid",
        (
            "#700FAh, right. We have been talking a bit\x01",
            "too long, haven't we?\x02\x03",

            "#703FOfficer Belc, if you would please\x01",
            "give the rundown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1015FCOLONEL Cid, huh?\x02\x03",

            "Weren't you Major Cid before?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 180, 400)

    ChrTalk(    #43
        0xB,
        (
            "#702FAh, yes...\x02\x03",

            "I actually got the notice just a little while ago.\x01",
            "I've been promoted to lieutenant colonel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1011FOh, neat!\x02\x03",

            "#1001FWell, congratulations, Lieutenant Colonel Cid!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1368")

    ChrTalk(    #45
        0x106,
        (
            "#051FHeh. Congrats.\x02\x03",

            "Nice to see a good man getting\x01",
            "the respect he deserves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1368")


    ChrTalk(    #46
        0xB,
        (
            "#701FI...thank you.\x02\x03",

            "To be honest, though, it's a bit embarrassing.\x01",
            "I only did what my country and duty asked of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1006FHey, there's no need to be humble.\x01",
            "You earned it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xD,
        "I agree, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xD,
        (
            "We'll be relying on you even\x01",
            "more in the days to come!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 45, 400)

    ChrTalk(    #50
        0xB,
        "#700FOfficer Belc, I believe I gave you an order.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        "Er, sorry, sir.\x02",
    )

    CloseMessageWindow()

    def lambda_14C7():
        OP_8C(0xD, 180, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_14C7)
    Sleep(250)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #52
        0xD,
        (
            "Let me explain the subject of\x01",
            "our request, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_157C")

    ChrTalk(    #53
        0x106,
        (
            "#050FYou want us to take part in training, right?\x02\x03",

            "What exactly do you have in mind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DF")

    label("loc_157C")


    ChrTalk(    #54
        0x103,
        (
            "#020FYou want us to assist with training,\x01",
            "correct?\x02\x03",

            "What, specifically, did you have in mind?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15DF")


    ChrTalk(    #55
        0xD,
        (
            "The idea is to have you participate in\x01",
            "some staged battles against the soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xD,
        (
            "You'll be fighting two back-to-back\x01",
            "matches, with no time in between\x01",
            "whatsoever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xD,
        (
            "You'll need to consider your pace,\x01",
            "so you don't wear yourselves out\x01",
            "completely.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #58
        0x101,
        (
            "#1015FNonstop combat with no breaks?\x01",
            "Umm... This sounds like it's gonna\x01",
            "be kinda hard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xD,
        "It'll be rough. I can't deny that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xD,
        (
            "Your role is to go through both battles and\x01",
            "not just test, but provide a model for our\x01",
            "soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xD,
        (
            "So don't hold back.\x01",
            "Fight both battles to win.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1002F...Understood.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_186B")

    ChrTalk(    #63
        0x106,
        (
            "#051FYou don't need to tell US not to\x01",
            "hold back, trust me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_186B")


    ChrTalk(    #64
        0x103,
        (
            "#525FOh, don't worry.\x01",
            "We won't be gentle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189A")


    ChrTalk(    #65
        0xB,
        (
            "#701FHaha. Well, this is sounding promising.\x02\x03",

            "All right. Officer Belc!\x01",
            "Lead the bracers to the training grounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xD,
        "Yes, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        "#700FI'll see you there, everyone!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 0, 400)

    def lambda_1954():
        TurnDirection(0x101, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1954)

    def lambda_1962():
        OP_8C(0xE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1962)
    OP_8C(0xF, 0, 400)
    WaitChrThread(0xE, 0x1)

    def lambda_197C():
        OP_8E(0xB, 0xFFFFFD4E, 0x0, 0x1B94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_197C)
    Sleep(20)

    def lambda_199C():
        OP_8E(0xE, 0xFFFFFBBE, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_199C)
    Sleep(30)

    def lambda_19BC():
        OP_8E(0xF, 0xFFFFFEDE, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_19BC)
    Sleep(2000)
    OP_8E(0xD, 0x366, 0x0, 0xFFFFF038, 0x7D0, 0x0)

    ChrTalk(    #68
        0xD,
        "Follow me, if you would.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)

    def lambda_1A15():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A15)
    OP_8C(0x11, 0, 400)
    OP_44(0x10, 0x1)

    def lambda_1A2E():
        OP_8E(0xD, 0x366, 0x0, 0x1D10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1A2E)
    Sleep(30)

    def lambda_1A4E():
        OP_8E(0x10, 0x1FE, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1A4E)
    Sleep(20)

    def lambda_1A6E():
        OP_8E(0x11, 0x514, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A6E)
    Sleep(1000)

    def lambda_1A8E():
        OP_8E(0x101, 0xFFFFFDE4, 0x0, 0x169E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A8E)
    Sleep(150)

    def lambda_1AAE():
        OP_8E(0xF7, 0x294, 0x0, 0x169E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1AAE)
    Sleep(250)

    def lambda_1ACE():
        OP_8E(0xF8, 0xFFFFFD62, 0x0, 0x1C02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1ACE)

    def lambda_1AE9():
        OP_8E(0xF9, 0x334, 0x0, 0x1C02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1AE9)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C3101   ._SN", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_81C end

    def Function_3_1B1B(): pass

    label("Function_3_1B1B")

    EventBegin(0x0)
    OP_6D(500, 80, -3600, 0)
    OP_67(0, 8080, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -70, 0, -5570, 0)
    SetChrPos(0xF7, 880, 150, -6000, 0)
    SetChrPos(0xF8, -320, 200, -7040, 0)
    SetChrPos(0xF9, 1170, 210, -7190, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xB, -540, 0, -3960, 180)
    SetChrPos(0xD, 820, 0, -3580, 180)
    SetChrPos(0xE, -1300, 0, -2190, 180)
    SetChrPos(0xF, -400, 0, -2190, 180)
    SetChrPos(0x10, 400, 0, -2190, 180)
    SetChrPos(0x11, 1300, 0, -2190, 180)
    SetChrPos(0x9, 2440, 0, -4250, 180)
    OP_4A(0x9, 255)
    OP_6F(0x0, 450)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_1D07")

    ChrTalk(    #69
        0xB,
        (
            "#701F#3PFriends, thank you for coming out \x01",
            "here today.\x02\x03",

            "I'm sure we'll have more to ask\x01",
            "of you in the future.\x02\x03",

            "I hope we can expect similar results\x01",
            "when that time comes!\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6D, 0x1, 0x80)
    OP_28(0x6D, 0x4, 0x10)
    Jump("loc_1E03")

    label("loc_1D07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1E03")

    ChrTalk(    #70
        0xB,
        (
            "#703F#3PBracers, thank you for coming out today.\x02\x03",

            "Even if the results were not quite what\x01",
            "we hoped for...\x02\x03",

            "#701FI still suspect we'll be asking more of\x01",
            "you in the future.\x02\x03",

            "I hope we can rely on you when that\x01",
            "time comes.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6D, 0x1, 0x100)
    OP_28(0x6D, 0x4, 0x80)
    OP_28(0x6D, 0x4, 0x40)

    label("loc_1E03")


    ChrTalk(    #71
        0x101,
        "#1006F#2PYou bet, Colonel Cid.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1EBE")

    ChrTalk(    #72
        0x106,
        (
            "#050F#2PWe were planning on helping out you army\x01",
            "guys as much as possible anyway.\x02\x03",

            "You need anything, just contact the guild,\x01",
            "any time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F47")

    label("loc_1EBE")


    ChrTalk(    #73
        0x103,
        (
            "#020F#2PWe intend to support the military to the\x01",
            "utmost of our ability.\x02\x03",

            "If you need anything, don't hesitate to\x01",
            "contact the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_2187")

    ChrTalk(    #74
        0xB,
        (
            "#701F#3PI will, thank you.\x02\x03",

            "As a parting gift, let me offer you this.\x02\x03",

            "Officer Belc?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xD,
        "Sir!\x02",
    )

    CloseMessageWindow()
    OP_94(0x1, 0xD, 0x0, 0x3E8, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #76
        "\x07\x00Received #326i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x146, 1)
    Sleep(500)
    OP_94(0x1, 0xD, 0xB4, 0x3E8, 0x7D0, 0x0)

    ChrTalk(    #77
        0xB,
        (
            "#701F#3PIt may not be much, but it should come\x01",
            "in handy at some point.\x02\x03",

            "I hope you'll accept it as thanks for\x01",
            "your assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1001F#2PThanks, Colonel Cid.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_210C")

    ChrTalk(    #79
        0x106,
        (
            "#051F#2PHey, you didn't need to do that.\x01",
            "But thanks.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2141")

    label("loc_210C")


    ChrTalk(    #80
        0x103,
        (
            "#021F#2PGoodness!\x01",
            "Thank you very much, Colonel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2141")


    ChrTalk(    #81
        0xB,
        (
            "#701F#3PNow, if you'll pardon me.\x02\x03",

            "I hope we meet again soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C3")

    label("loc_2187")


    ChrTalk(    #82
        0xB,
        (
            "#701F#3PYou have my thanks.\x02\x03",

            "Now, if you'll pardon me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C3")


    def lambda_21C9():
        OP_8C(0xE, 0, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_21C9)

    def lambda_21D7():
        OP_8C(0xF, 0, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_21D7)

    def lambda_21E5():
        OP_8C(0x10, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21E5)

    def lambda_21F3():
        OP_8C(0x11, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21F3)
    WaitChrThread(0x11, 0x1)

    def lambda_2206():
        OP_8C(0xB, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2206)
    Sleep(250)
    OP_8C(0xD, 180, 400)
    WaitChrThread(0xB, 0x1)

    def lambda_2225():
        OP_8E(0xB, 0xFFFFFDE4, 0x0, 0x1B94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2225)

    def lambda_2240():
        OP_8E(0xD, 0x334, 0x0, 0x1D10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2240)

    def lambda_225B():
        OP_8E(0xE, 0xFFFFFAEC, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_225B)

    def lambda_2276():
        OP_8E(0xF, 0xFFFFFE70, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2276)

    def lambda_2291():
        OP_8E(0x10, 0x190, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2291)

    def lambda_22AC():
        OP_8E(0x11, 0x514, 0x0, 0x226A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_22AC)
    Sleep(1000)
    OP_70(0x0, 0x0)
    Sleep(350)
    OP_43(0x9, 0x1, 0x1, 0x5)
    OP_73(0x0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_A2(0x1)
    EventEnd(0x0)
    OP_4B(0x9, 255)
    Return()

    # Function_3_1B1B end

    def Function_4_22F0(): pass

    label("Function_4_22F0")

    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0x992, 0x0, 0xFFFFF13C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_4_22F0 end

    def Function_5_2313(): pass

    label("Function_5_2313")

    OP_8C(0xFE, 270, 400)
    OP_8E(0x9, 0x0, 0x0, 0xFFFFF13C, 0x7D0, 0x0)
    OP_8E(0x9, 0x0, 0x0, 0xFFFFF362, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    Return()

    # Function_5_2313 end

    SaveToFile()

Try(main)
