from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2600_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_B0F",          # 01, 1
        "Function_2_B34",          # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2000)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_83")
    Return()

    label("loc_83")

    EventBegin(0x0)
    Fade(1000)
    OP_6C(45000, 0)
    OP_6D(200, 0, 3500, 0)
    SetChrPos(0x101, 200, 0, 3500, 0)
    SetChrPos(0x105, -600, 0, 2500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5")
    SetChrPos(0x13B, 1000, 0, 1500, 0)

    label("loc_E5")

    OP_0D()
    WaitChrThread(0x9, 0x1)

    def lambda_F1():
        OP_6D(-180, 1000, 7200, 1500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_160")
    Sleep(150)
    OP_62(0x13B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_160")

    WaitChrThread(0x9, 0x1)
    SetChrPos(0x9, 20, 1000, 12000, 180)
    ClearChrFlags(0x9, 0x80)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x2D)
    OP_73(0x0)

    def lambda_192():
        OP_8F(0x9, 0x50, 0x3E8, 0x2A30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_192)
    OP_8C(0x9, 0, 800)
    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 45)
    OP_70(0x0, 0x0)
    WaitChrThread(0x9, 0x2)
    OP_94(0x1, 0x9, 0xB4, 0x578, 0x1770, 0x0)
    OP_73(0x0)
    OP_71(0x0, 0x800)
    OP_43(0x9, 0x1, 0x1, 0x1)
    OP_97(0x9, 0xFFFFFD12, 0x2508, 0x2BF20, 0x1388, 0x1)
    OP_8C(0x9, 45, 400)
    OP_44(0x9, 0x1)
    Sleep(400)

    ChrTalk(    #0
        0x9,
        "*huff* *puff* *pant* *wheeze*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        "Holy...freaking...crap...\x02",
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #2
        0x101,
        "#002F...What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        (
            "#045FWhat's up indeed!\x02\x03",

            "He seems...really, really\x01",
            "scared!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_6A(0x101)

    def lambda_2E1():
        OP_91(0x101, 0x0, 0x0, 0xA8C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E1)
    Sleep(150)

    def lambda_301():
        OP_91(0x105, 0x0, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_301)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33B")
    OP_91(0x13B, 0x0, 0x0, 0xA28, 0x7D0, 0x0)
    Jump("loc_340")

    label("loc_33B")

    WaitChrThread(0x105, 0x1)

    label("loc_340")

    TurnDirection(0x101, 0x9, 400)
    ClearMapFlags(0x1)

    ChrTalk(    #4
        0x101,
        "#002FWell? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x9, 0x101, 400)
    Sleep(400)

    ChrTalk(    #5
        0x9,
        (
            "H-Hey. You shouldn't stand\x01",
            "right in front of the door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "You never know when a ghost\x01",
            "or something might come\x01",
            "flying out.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #7
        0x101,
        (
            "#004FA...a ghost?\x02\x03",

            "Are there monsters in this\x01",
            "building?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "Yeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "Enormous suckers, swarms of 'em.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #10
        0x105,
        (
            "#042FThis used to be one of\x01",
            "the school buildings.\x02\x03",

            "But it's always locked\x01",
            "up these days.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 400)

    ChrTalk(    #11
        0x9,
        (
            "I borrowed the key from\x01",
            "Mr. Effort.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55C")

    def lambda_54F():
        TurnDirection(0x13B, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_54F)
    Sleep(100)

    label("loc_55C")

    TurnDirection(0x105, 0x9, 400)

    ChrTalk(    #12
        0x9,
        (
            "The regular school buildings are\x01",
            "all noisy lately. I just wanted a\x01",
            "quiet place to sleep.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72E")

    ChrTalk(    #13
        0x101,
        "#004F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13B,
        (
            "#647FWhich is, of course, just another\x01",
            "way of saying that you're ditching.\x02\x03",

            "#659FI gotta say, Mickey, you've got\x01",
            "some nerve.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x13B, 400)

    ChrTalk(    #15
        0x9,
        (
            "Hey, I never wanted anything\x01",
            "to do with the festival in the\x01",
            "first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "Why should I be forced to do\x01",
            "anything for some lame play?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "It's boring, and I ain't messing\x01",
            "with it any more.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A4")

    label("loc_72E")


    ChrTalk(    #18
        0x101,
        (
            "#004F...\x02\x03",

            "So you're not even going\x01",
            "to help?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #19
        0x9,
        (
            "It's boring. Let the ones who\x01",
            "wanna help do the helping.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A4")

    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #20
        0x101,
        (
            "#009FWhat's with your attitude?\x02\x03",

            "Pretty arrogant of you, considering\x01",
            "everyone ELSE is pitching in.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #21
        0x105,
        (
            "#045FNow, now, Estelle...\x02\x03",

            "For now, let's just focus on\x01",
            "checking into these supposed\x01",
            "monsters in here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #22
        0x101,
        (
            "#004FWell, I... Oh, okay.\x02\x03",

            "#002FIf there really are monsters,\x01",
            "I guess we can't just let them\x01",
            "stay in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x105,
        "#043FRight. The festival is tomorrow...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x105, 400)

    ChrTalk(    #24
        0x9,
        "But what can WE do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "I was just planning to go give the key\x01",
            "back to Mr. Effort, tell him the place\x01",
            "is haunted, and NEVER SPEAK OF IT AGAIN.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)
    TurnDirection(0x9, 0x101, 400)

    def lambda_A00():

        label("loc_A00")

        TurnDirection(0x101, 0x9, 0)
        OP_48()
        Jump("loc_A00")

    QueueWorkItem2(0x101, 1, lambda_A00)

    def lambda_A11():

        label("loc_A11")

        TurnDirection(0x105, 0x9, 0)
        OP_48()
        Jump("loc_A11")

    QueueWorkItem2(0x105, 1, lambda_A11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A3B")

    def lambda_A30():

        label("loc_A30")

        TurnDirection(0x13B, 0x9, 0)
        OP_48()
        Jump("loc_A30")

    QueueWorkItem2(0x13B, 1, lambda_A30)

    label("loc_A3B")


    ChrTalk(    #26
        0x9,
        (
            "It's really dangerous in there.\x01",
            "I wouldn't even get close to\x01",
            "the door, if I were you!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFFFB6E, 0x3E8, 0x1A54, 0x1388, 0x0)

    def lambda_AB0():
        OP_91(0x105, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AB0)
    OP_8E(0x9, 0x82, 0x3E8, 0xFFFFEF8E, 0x1388, 0x0)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x40)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFD")
    OP_44(0x13B, 0x1)

    label("loc_AFD")

    OP_28(0x27, 0x1, 0x2000)
    OP_64(0x0, 0x1)
    OP_71(0x0, 0x10)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    def Function_1_B0F(): pass

    label("Function_1_B0F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B33")
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_48()
    Jump("Function_1_B0F")

    label("loc_B33")

    Return()

    # Function_1_B0F end

    def Function_2_B34(): pass

    label("Function_2_B34")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B53")
    SetChrFlags(0x13B, 0x80)

    label("loc_B53")

    SetMapFlags(0x400000)
    SetChrPos(0x101, -500, 1000, 11470, 96)
    SetChrPos(0x105, 500, 1000, 11470, 96)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B99")
    SetChrPos(0x13B, 0, 1000, 11470, 96)

    label("loc_B99")

    OP_6C(45000, 0)
    OP_6D(0, 1000, 6110, 0)
    OP_6F(0x0, 60)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD7")
    ClearChrFlags(0x13B, 0x80)

    label("loc_BD7")


    def lambda_BDD():
        OP_8E(0x101, 0xFFFFFE0C, 0x3E8, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDD)
    Sleep(200)

    def lambda_BFD():
        OP_8E(0x105, 0x226, 0x3E8, 0x1838, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BFD)

    def lambda_C18():
        OP_8E(0xA, 0x12C, 0x1F4, 0x100E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C18)
    Sleep(400)
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C68")

    def lambda_C4B():
        OP_8E(0x13B, 0x12C, 0x3E8, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_C4B)
    WaitChrThread(0x13B, 0x1)
    Jump("loc_C6D")

    label("loc_C68")

    WaitChrThread(0x105, 0x1)

    label("loc_C6D")

    OP_72(0x0, 0x800)
    OP_22(0xD3, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0xA, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBD")

    def lambda_CB5():
        TurnDirection(0x13B, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_CB5)

    label("loc_CBD")

    TurnDirection(0x105, 0xA, 400)
    OP_71(0x0, 0x800)

    ChrTalk(    #27
        0x105,
        "#040FMr. Effort...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x105, 400)

    ChrTalk(    #28
        0xA,
        "Are you kids all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "Mickey told me that monsters\x01",
            "had shown up in the old school\x01",
            "building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x105,
        "#040FApparently so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#000FNo need to worry. We've wiped\x01",
            "them all out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #32
        0xA,
        "Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "Oh, of course.\x01",
            "You're a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "Well, thank you for your help.\x01",
            "We can't have anything happen\x01",
            "to the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x105,
        "#040FIndeed.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0F")

    ChrTalk(    #36
        0x13B,
        (
            "#640FCome to think of it...\x02\x03",

            "Mickey's laziness actually\x01",
            "helped us out.\x02\x03",

            "In spite of his reasons, he did\x01",
            "find the monsters, at least.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EE3():
        TurnDirection(0x105, 0x13B, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_EE3)
    TurnDirection(0x101, 0x13B, 400)

    ChrTalk(    #37
        0x101,
        "#000FYeah, that's true.\x02",
    )

    CloseMessageWindow()

    label("loc_F0F")


    ChrTalk(    #38
        0xA,
        (
            "Just to be on the safe side, why\x01",
            "don't we lock the door again?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F59():
        TurnDirection(0x105, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F59)
    Sleep(100)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #39
        0xA,
        (
            "Better safe than sorry,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        "#040FYes, I agree.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)

    def lambda_FB8():

        label("loc_FB8")

        TurnDirection(0x101, 0xA, 0)
        OP_48()
        Jump("loc_FB8")

    QueueWorkItem2(0x101, 1, lambda_FB8)

    def lambda_FC9():

        label("loc_FC9")

        TurnDirection(0x105, 0xA, 0)
        OP_48()
        Jump("loc_FC9")

    QueueWorkItem2(0x105, 1, lambda_FC9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF3")

    def lambda_FE8():

        label("loc_FE8")

        TurnDirection(0x13B, 0xA, 0)
        OP_48()
        Jump("loc_FE8")

    QueueWorkItem2(0x13B, 1, lambda_FE8)

    label("loc_FF3")


    def lambda_FF9():
        OP_91(0x105, 0x2BC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FF9)

    def lambda_1014():
        OP_91(0x101, 0xFFFFFD44, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1014)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1052")

    def lambda_103D():
        OP_91(0x13B, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 2, lambda_103D)

    label("loc_1052")


    def lambda_1058():
        OP_6D(-20, 1000, 9150, 1500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1058)
    OP_8E(0xA, 0xFFFFFFEC, 0x3E8, 0x23BE, 0x7D0, 0x0)
    WaitChrThread(0xA, 0x1)
    Sleep(300)
    OP_22(0x73, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #41
        0xA,
        "That should take care of it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    ChrTalk(    #42
        0xA,
        (
            "Well, I should get back\x01",
            "to the night duty room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        "It'll be closing time fairly soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "You kids try not to stay\x01",
            "up too late.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116A")

    ChrTalk(    #45
        0x13B,
        "#640FWe're okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_119C")

    label("loc_116A")


    ChrTalk(    #46
        0x105,
        (
            "#040FYes, sir. We'll take care of\x01",
            "ourselves.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_119C")


    ChrTalk(    #47
        0x101,
        "#000FRoger that.\x02",
    )

    CloseMessageWindow()

    def lambda_11B8():
        OP_6D(0, 1000, 6110, 1500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_11B8)
    OP_8E(0xA, 0x12C, 0x0, 0xFFFFEF2A, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F8")
    OP_44(0x13B, 0x1)

    label("loc_11F8")

    ClearChrFlags(0xA, 0x40)
    SetChrFlags(0xA, 0x80)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #48
        (
            "\x07\x00Festival help quest \x07\x02[Clear Out the Old School Building]\x01\x07\x00",
            "completed!\x02",
        )
    )

    OP_83(0x2, 0x1)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    ClearMapFlags(0x400000)
    OP_65(0x0, 0x1)
    OP_72(0x0, 0x10)
    EventEnd(0x0)
    Return()

    # Function_2_B34 end

    SaveToFile()

Try(main)
