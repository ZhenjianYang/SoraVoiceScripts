from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1501_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C1501.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60022",
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
        "Function_1_67",           # 01, 1
        "Function_2_21D1",         # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Return()

    # Function_0_66 end

    def Function_1_67(): pass

    label("Function_1_67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F")
    Return()

    label("loc_7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D0")
    OP_28(0x1F, 0x1, 0x4000)
    OP_28(0x1F, 0x4, 0x8)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB")
    TurnDirection(0x101, 0x8, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #0
        0x101,
        "#004FAh...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_177")

    label("loc_DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121")
    TurnDirection(0x102, 0x8, 0)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #1
        0x102,
        "#014FIsn't that...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_177")

    label("loc_121")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177")
    TurnDirection(0x105, 0x8, 0)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #2
        0x105,
        "#044FIs that who we're looking for...?\x02",
    )

    CloseMessageWindow()

    label("loc_177")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_191():
        OP_6D(-101100, 3350, 66300, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_191)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_1BB():
        OP_8E(0x8, 0xFFFE7514, 0xD16, 0x102FC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BB)

    def lambda_1D6():
        OP_8E(0x9, 0xFFFE744C, 0xD16, 0x10298, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D6)

    def lambda_1F1():
        OP_8E(0xA, 0xFFFE7514, 0xD16, 0x1016C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F1)

    def lambda_20C():
        OP_8E(0xB, 0xFFFE74B0, 0xD16, 0x103C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_20C)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x105, 0x40)

    def lambda_23B():
        OP_8E(0x101, 0xFFFE889C, 0xFA0, 0x11FE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23B)

    def lambda_256():
        OP_8E(0x102, 0xFFFE8C84, 0xFA0, 0x123CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_256)

    def lambda_271():
        OP_8E(0x105, 0xFFFE906C, 0xFA0, 0x127B4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_271)
    OP_8C(0x8, 0, 400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    OP_43(0x8, 0x1, 0x1, 0x2)
    WaitChrThread(0x9, 0x1)

    def lambda_2C7():
        OP_8E(0x9, 0xFFFE6A24, 0x834, 0xF8D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2C7)
    WaitChrThread(0xA, 0x1)

    def lambda_2E7():
        OP_8E(0xA, 0xFFFE7064, 0x9C4, 0xFA00, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2E7)
    WaitChrThread(0xB, 0x1)

    def lambda_307():
        OP_8E(0xB, 0xFFFE7578, 0xA5A, 0xF6E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_307)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0x9, 0x1)

    def lambda_32C():
        OP_8E(0x9, 0xFFFE6A24, 0x834, 0xE9FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_32C)

    def lambda_347():
        OP_8E(0x101, 0xFFFE72BC, 0x960, 0xF80C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_347)
    WaitChrThread(0xA, 0x1)

    def lambda_367():
        OP_8E(0xA, 0xFFFE6DA8, 0x834, 0xEF10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_367)

    def lambda_382():
        OP_8E(0x102, 0xFFFE6E70, 0xA28, 0xFC57, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_382)
    WaitChrThread(0xB, 0x1)

    def lambda_3A2():
        OP_8E(0xB, 0xFFFE7640, 0x8B6, 0xEE48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A2)

    def lambda_3BD():
        OP_8E(0x105, 0xFFFE74B0, 0xC1C, 0xFFDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3BD)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x8, 0)
    SetChrChipByIndex(0x101, 3)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_42D():
        OP_69(0xC, 0x320)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_42D)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0x8, 0)
    SetChrChipByIndex(0x102, 5)
    WaitChrThread(0x105, 0x1)
    TurnDirection(0x105, 0x8, 0)
    SetChrChipByIndex(0x105, 7)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #3
        0x8,
        "H-Hey there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "Help! I need help!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#005FCome on, Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#012FRight!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 8)

    def lambda_4D6():
        OP_94(0x1, 0x101, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D6)

    def lambda_4EC():
        OP_94(0x1, 0x102, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4EC)

    def lambda_502():
        OP_94(0x1, 0x105, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_502)
    Sleep(400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    Battle(0x3F4, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    OP_4A(0x8, 255)
    AddParty(0x36, 0x3)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    SetChrChipByIndex(0x105, 7)
    SetChrPos(0x101, -101700, 2400, 63500, 180)
    SetChrPos(0x102, -104300, 2000, 63100, 180)
    SetChrPos(0x105, -102900, 2500, 64200, 180)
    SetChrPos(0x137, -102260, 1950, 58980, 356)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xC, 0x0)
    OP_6C(265000, 0)
    OP_0D()
    SetChrChipByIndex(0x105, 65535)
    TurnDirection(0x105, 0x8, 400)

    ChrTalk(    #7
        0x105,
        (
            "#043FIt looks like we made it just\x01",
            "in time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)

    def lambda_658():
        TurnDirection(0x102, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_658)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #8
        0x101,
        "#002FMore like by a hair's breadth.\x02",
    )

    CloseMessageWindow()
    Sleep(800)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #9
        0x102,
        "#010FWere you hurt, sir?\x02",
    )

    CloseMessageWindow()

    def lambda_6C0():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C0)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #10
        0x8,
        "Not at all. I am quite all right.\x02",
    )

    CloseMessageWindow()
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_73B():
        OP_69(0xC, 0x320)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_73B)
    OP_8E(0x137, 0xFFFE6DA8, 0x834, 0xF0A0, 0x7D0, 0x0)
    WaitChrThread(0x137, 0x1)
    TalkBegin(0x137)
    TurnDirection(0x137, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1268")
    OP_28(0x1F, 0x1, 0x8)
    OP_28(0x1F, 0x1, 0x10)

    ChrTalk(    #11
        0x137,
        (
            "Thanks to you I came out with nothing\x01",
            "more than a few scratches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x137,
        "Hmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x137,
        (
            "Now I could almost swear I've seen you two\x01",
            "somewhere before... The girl's homely face\x01",
            "is especially familiar...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(    #14
        0x101,
        (
            "#000F...H-Homely? Hey...!\x01",
            "But now that you mention it...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x137, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #15
        0x137,
        "Oh, I remember now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x137,
        (
            "You're that country girl from\x01",
            "Rolent.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #17
        0x101,
        (
            "#004FYou!\x02\x03",

            "#005FYou're that conniving merchant\x01",
            "who was searching for those\x01",
            "toxic mushrooms!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #18
        0x102,
        (
            "#018FEstelle...he was a client, remember?\x01",
            "Tone it down a bit...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(    #19
        0x137,
        (
            "Hmph. It looks like even now you\x01",
            "still haven't learned how to show\x01",
            "the slightest courtesy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x137,
        (
            "It's exactly what I'd expect from\x01",
            "someone raised in the boonies.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #21
        0x101,
        (
            "#009FHow about you just shut up?\x01",
            "You nasty food maniac!\x02\x03",

            "No doubt you were out here hunting\x01",
            "for more bizarre ingredients, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x137,
        (
            "Hmph! I've already gathered the\x01",
            "valuable wild vegetables I came\x01",
            "here for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x137,
        (
            "These exotic delectables are FAR\x01",
            "more unique than even that Firefly\x01",
            "Fungus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x137,
        (
            "Heh heh... With these in hand,\x01",
            "my next business deal is sure\x01",
            "to be a success.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #25
        0x101,
        (
            "#004FBack up, buddy. What do you mean\x01",
            "by 'next business deal'?\x02\x03",

            "#507FHa! That Firefly Fungus didn't work\x01",
            "out for you, did it?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x137, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #26
        0x137,
        (
            "I'm not going to listen to any more\x01",
            "of this pessimism!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x137,
        (
            "There just happened to be no\x01",
            "demand for them at the time.\x01",
            "That's all. End of story.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #28
        0x105,
        (
            "#044FUm, Estelle.\x02\x03",

            "When he mentioned the wild vegetables,\x01",
            "did that bring anything to mind?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #29
        0x101,
        "#505FOh, right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(    #30
        0x102,
        (
            "#010FAmelia, who we met at Manoria\x01",
            "Village.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(    #31
        0x137,
        "Amelia, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x137,
        (
            "That's my niece, but what does she\x01",
            "have to do with any of this...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(    #33
        0x101,
        (
            "#004FEh...?\x02\x03",

            "Which means that you're her uncle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(    #34
        0x102,
        "#010FIt certainly looks that way.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x137, 400)

    ChrTalk(    #35
        0x137,
        "Why? Has she done something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        (
            "#010FActually, Amelia asked that we\x01",
            "provide your escort...\x02\x03",

            "But when we arrived in Manoria\x01",
            "you had already left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x137,
        (
            "Is that so? I guess it wasn't\x01",
            "very nice of me to take off like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x137,
        "But, it couldn't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x137,
        (
            "I had to come up with a real eye-catcher\x01",
            "before my next business deal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#002FAnd because of that, you almost\x01",
            "ended up being some monsters'\x01",
            "next meal.\x02\x03",

            "I'm pretty sure you can't do business\x01",
            "deals while in the belly of a monster.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x101, 400)

    ChrTalk(    #41
        0x137,
        "Mmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#002FOnce you get back, you should\x01",
            "apologize to Amelia.\x02\x03",

            "I'm sure she's worried sick about\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x137,
        "All right, fine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x137,
        (
            "I promise to talk to her after my next\x01",
            "business deal in Grancel is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#010FI think that would be a good\x01",
            "move on your part, too.\x02\x03",

            "Okay, let's get going.\x02\x03",

            "We'll escort you back to town.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(    #46
        0x137,
        "You have my thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x137,
        "I am in your hands.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B5")

    label("loc_1268")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_1B06")
    OP_28(0x1F, 0x1, 0x8)
    OP_28(0x1F, 0x1, 0x10)

    ChrTalk(    #48
        0x137,
        (
            "Thanks to you I came out with nothing\x01",
            "more than a few scratches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x137,
        "Hmm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x137,
        (
            "Now I could almost swear I've seen you two\x01",
            "somewhere before... The girl's homely face\x01",
            "is especially familiar...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1428")

    ChrTalk(    #51
        0x101,
        (
            "#004FYou!\x02\x03",

            "#005FYou're that conniving merchant\x01",
            "who was searching for those\x01",
            "toxic mushrooms!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #52
        0x102,
        (
            "#018FEstelle...he was a client, remember?\x01",
            "Tone it down a bit...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)
    Jump("loc_143E")

    label("loc_1428")


    ChrTalk(    #53
        0x101,
        "#004FOh, really?\x02",
    )

    CloseMessageWindow()

    label("loc_143E")

    OP_62(0x137, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #54
        0x137,
        "Well, bless my bones!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x137,
        "If it isn't the bracers I met in Rolent.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(    #56
        0x102,
        (
            "#010FIt's nice to see you again.\x02\x03",

            "How's your work treating you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(    #57
        0x137,
        (
            "Well, if you must know, I managed\x01",
            "to collect some more valuable wild\x01",
            "vegetables today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x137,
        (
            "These exotic delectables are far\x01",
            "more unique than even that Firefly\x01",
            "Fungus from before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x137,
        (
            "With these in hand, my next business\x01",
            "deal is sure to be a success.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #60
        0x105,
        (
            "#044FUm, Estelle.\x02\x03",

            "When he mentioned the wild vegetables,\x01",
            "did that bring anything to mind?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #61
        0x101,
        "#505FOh, right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(    #62
        0x102,
        (
            "#010FAmelia, who we met at Manoria\x01",
            "Village.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(    #63
        0x137,
        "Amelia, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x137,
        (
            "That's my niece, but what does she\x01",
            "have to do with any of this...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(    #65
        0x101,
        (
            "#004FEh...?\x02\x03",

            "Which means that you're her uncle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(    #66
        0x102,
        "#010FIt certainly looks that way.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x137, 400)

    ChrTalk(    #67
        0x137,
        "Why? Has she done something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#010FActually, Amelia asked that we\x01",
            "provide your escort...\x02\x03",

            "But when we arrived in Manoria\x01",
            "you had already left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x137,
        (
            "Is that so? I guess it wasn't\x01",
            "very nice of me to take off like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x137,
        "But, it couldn't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x137,
        (
            "I had to come up with a real eye-catcher\x01",
            "before my next business deal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#002FAnd because of that, you almost\x01",
            "ended up being some monsters'\x01",
            "next meal.\x02\x03",

            "I'm pretty sure you can't do business\x01",
            "deals while in the belly of a monster.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x101, 400)

    ChrTalk(    #73
        0x137,
        "Mmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#002FOnce you get back, you should\x01",
            "apologize to Amelia.\x02\x03",

            "I'm sure she's worried sick about\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x137,
        "All right, fine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x137,
        (
            "I promise to talk to her after my next\x01",
            "business deal in Grancel is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#010FI think that would be a good\x01",
            "move on your part, too.\x02\x03",

            "Okay, let's get going.\x02\x03",

            "We'll escort you back to town.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(    #78
        0x137,
        "You have my thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x137,
        "I am in your hands.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B5")

    label("loc_1B06")

    OP_28(0x1F, 0x1, 0x20)
    OP_28(0x1F, 0x1, 0x40)

    ChrTalk(    #80
        0x137,
        (
            "Thanks to you I came out with nothing\x01",
            "more than a few scratches...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x137,
        (
            "That was a masterful show of skill,\x01",
            "and I'd expect nothing less from a\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(    #82
        0x101,
        (
            "#501FMy question is: What were you doing\x01",
            "out on this trail in the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x137,
        (
            "I'm a merchant who specializes in\x01",
            "high-quality ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x137,
        (
            "Today, I came here in search of\x01",
            "some valuable wild vegetables.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #85
        0x105,
        (
            "#044FWild vegetables...?\x02\x03",

            "Umm, Estelle.\x02\x03",

            "When he mentioned the wild vegetables,\x01",
            "did that bring anything to mind?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #86
        0x101,
        "#505FOh, right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(    #87
        0x102,
        (
            "#010FAmelia, who we met at Manoria\x01",
            "Village.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(    #88
        0x137,
        "Amelia, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x137,
        (
            "That's my niece, but what does she\x01",
            "have to do with any of this...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x137, 400)

    ChrTalk(    #90
        0x101,
        (
            "#004FEh...?\x02\x03",

            "Which means that you're her uncle?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x137, 400)

    ChrTalk(    #91
        0x102,
        "#010FIt certainly looks that way.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x137, 400)

    ChrTalk(    #92
        0x137,
        "Why? Has she done something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#010FActually, Amelia asked that we\x01",
            "provide your escort...\x02\x03",

            "But when we arrived in Manoria\x01",
            "you had already left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x137,
        (
            "Is that so? I guess it wasn't\x01",
            "very nice of me to take off like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x137,
        "But, it couldn't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x137,
        (
            "I had to come up with a real eye-catcher\x01",
            "before my next business deal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#002FAnd because of that, you almost\x01",
            "ended up being some monsters'\x01",
            "next meal.\x02\x03",

            "I'm pretty sure you can't do business\x01",
            "deals while in the belly of a monster.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x101, 400)

    ChrTalk(    #98
        0x137,
        "Mmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        (
            "#002FOnce you get back, you should\x01",
            "apologize to Amelia.\x02\x03",

            "I'm sure she's worried sick about\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x137,
        "All right, fine...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x137,
        (
            "I promise to talk to her after my next\x01",
            "business deal in Grancel is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x102,
        (
            "#010FI think that would be a good\x01",
            "move on your part, too.\x02\x03",

            "Okay, let's get going.\x02\x03",

            "We'll escort you back to town.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x137, 0x102, 400)

    ChrTalk(    #103
        0x137,
        "You have my thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x137,
        "I am in your hands.\x02",
    )

    CloseMessageWindow()

    label("loc_21B5")

    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x137, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x137, 0x40)
    EventEnd(0x0)

    label("loc_21D0")

    Return()

    # Function_1_67 end

    def Function_2_21D1(): pass

    label("Function_2_21D1")

    OP_44(0xC, 0x1)

    def lambda_21DB():
        OP_6D(-102000, 1930, 59600, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_21DB)
    OP_8E(0x8, 0xFFFE70C8, 0x9C4, 0xF424, 0xBB8, 0x0)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x8, 0, 400)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x8, 0x4)
    OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
    Sleep(400)
    OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
    Sleep(400)
    OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
    Sleep(400)
    OP_8C(0x8, 180, 400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)
    OP_8C(0x8, 0, 400)
    Return()

    # Function_2_21D1 end

    SaveToFile()

Try(main)
